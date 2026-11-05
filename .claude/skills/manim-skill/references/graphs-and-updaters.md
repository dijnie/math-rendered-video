# Graphs, Plotting & Updaters

## Axes and plotting a function

```python
ax = Axes(
    x_range=[0, 10, 1], y_range=[0, 100, 10],
    axis_config={"include_tip": True},
)
labels = ax.get_axis_labels(x_label="x", y_label="f(x)")
curve  = ax.plot(lambda x: 2 * (x - 5) ** 2, color=MAROON)

self.play(Create(ax), Write(labels))
self.play(Create(curve))
```

- `ax.plot(fn, x_range=[a,b])` — graph a function; `ax.plot_line_graph(x_values, y_values)` for discrete data.
- `ax.c2p(x, y)` (coords→point) and `ax.p2c(point)` (point→coords) — **always** place objects on axes via `c2p`, never raw screen coords.
- `ax.get_area(curve, x_range=[a,b])` — shade under a curve; `ax.get_riemann_rectangles(curve, dx=0.5)` — Riemann sum.
- `NumberPlane()` for a full grid; `NumberLine()` for 1D.

## Moving a dot along the curve (ValueTracker)

`ValueTracker` holds an animatable scalar; updaters recompute dependent mobjects every frame.

```python
t = ValueTracker(0)
dot = always_redraw(
    lambda: Dot(ax.c2p(t.get_value(), (t.get_value() - 5) ** 2 * 2), color=YELLOW)
)
self.add(dot)
self.play(t.animate.set_value(10), run_time=4, rate_func=linear)
```

- `always_redraw(fn)` — rebuild the mobject from scratch each frame (simplest; fn returns a fresh mobject).
- `mob.add_updater(lambda m: m.move_to(ax.c2p(t.get_value(), ...)))` — mutate an existing mobject each frame.
- `mob.clear_updaters()` when finished, or later animations fight the updater.

## Animated counter / readout

```python
num = always_redraw(
    lambda: DecimalNumber(t.get_value(), num_decimal_places=1).next_to(dot, UR)
)
# or a value-driven label via t.get_value()
self.play(t.animate.set_value(10))
```

## Tangent / secant, derivatives

```python
tangent = always_redraw(lambda: ax.get_secant_slope_group(
    x=t.get_value(), graph=curve, dx=0.01, secant_line_color=GREEN
))
```

## Common patterns

- Reveal axes → write labels → `Create` the curve → run a `ValueTracker` to trace/scan.
- Pair `always_redraw` (recompute geometry) with `ValueTracker` (the single source of truth) — drive everything off one tracker so the scene stays consistent.
- For multiple curves, `VGroup(c1, c2)` and animate together; `ax.plot(...).set_color_by_gradient(...)`.

## Styling axes and planes

```python
ax = Axes(
    x_range=[-3, 3, 1], y_range=[-1, 9, 2], x_length=8, y_length=5,
    tips=False,
    axis_config={"color": MUTED, "stroke_width": 2, "include_ticks": True, "font_size": 24},
    x_axis_config={"numbers_to_include": [-2, -1, 1, 2]},
    y_axis_config={"numbers_to_include": [2, 4, 6, 8]},
)
curve = ax.plot(lambda x: x**2, color=ACCENT, stroke_width=4)
label = ax.get_graph_label(curve, MathTex("y=x^2"), x_val=2.2, direction=UR)
```

- Quiet axes (MUTED, thin, `tips=False`) + a bright, thicker curve: the data is the hero, not the frame.
- `ax.add_coordinates()` for all tick numbers; prefer a few chosen ones via `numbers_to_include`.
- `NumberPlane(background_line_style={"stroke_color": A2, "stroke_opacity": 0.35, "stroke_width": 1}, faded_line_ratio=2)` for a soft grid; `ComplexPlane().add_coordinates()` for complex numbers; `PolarPlane` for polar.
- Guides: `ax.get_vertical_line(ax.c2p(x, f(x)), line_func=DashedLine)`, `ax.get_lines_to_point(p)`, `ax.get_T_label(x, curve, label=MathTex("a"))`.
- More curves: `ax.plot_derivative_graph(curve)`, `ax.plot_parametric_curve(lambda t: [...], t_range=[0, TAU])`, `ax.plot_implicit_curve(lambda x, y: x**2 + y**2 - 4)`, `ax.plot_polar_graph(...)` on `PolarPlane`.
- Areas: `ax.get_area(curve, x_range=[0, 2], color=[A2, ACCENT], opacity=0.4)`; between curves `ax.get_area(c1, [a, b], bounded_graph=c2)`; Riemann sums `ax.get_riemann_rectangles(curve, x_range=[0, 2], dx=0.25, color=[A2, ACCENT], fill_opacity=0.6)` and animate `dx` shrinking with `Transform` between successive rectangle sets.
- Discontinuities: `ax.plot(f, discontinuities=[0], dt=0.01)` instead of a vertical line through a pole.

## Fields, charts, data

- `ArrowVectorField(lambda p: np.array([-p[1], p[0], 0]), colors=[A2, ACCENT])` — static field.
- `StreamLines(func, stroke_width=2, max_anchors_per_line=30)`, then `self.add(stream); stream.start_animation(warm_up=False, flow_speed=1.5); self.wait(3)` — flowing field.
- `BarChart(values=[3, 5, 2], bar_names=["A", "B", "C"], bar_colors=[A2, ACCENT, A3], y_range=[0, 6, 1])`; animate with `chart.animate.change_bar_values([...])`.
- `ax.plot_line_graph(xs, ys, line_color=A2, vertex_dot_style={"color": ACCENT})` for data points.

## Graph storytelling patterns

- Axes `Create` (quick, 1 s) → curve `Create` (slower, 1.5–2.5 s, `rate_func=linear` if it represents time) → label `FadeIn`.
- A `ValueTracker` sweeps `x`: dot rides the curve, dashed guides drop to the axes, a `DecimalNumber` readout follows — one tracker drives them all.
- Morph a curve when a parameter changes: `curve.add_updater(lambda c: c.become(ax.plot(lambda x: k.get_value() * x**2, color=ACCENT)))`, then animate `k`.
- Zoom into a local feature (tangent, limit) with `MovingCameraScene` rather than re-drawing axes at a new scale.

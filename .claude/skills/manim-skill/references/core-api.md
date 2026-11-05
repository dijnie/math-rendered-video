# Core API

Everything is **Scenes** (orchestration) acting on **Mobjects** (objects) via **Animations** (timed change). All motion lives inside `construct()`.

```python
class SquareToCircle(Scene):
    def construct(self):
        sq = Square().set_fill(BLUE, opacity=0.5)
        self.play(Create(sq), run_time=1)
        self.play(sq.animate.rotate(PI / 4), run_time=1)
        self.play(Transform(sq, Circle().set_fill(PINK, opacity=0.5)), run_time=1)
        self.wait(0.5)
```

## Mobjects

- Shapes: `Circle`, `Square`, `Rectangle`, `RoundedRectangle`, `Line`, `DashedLine`, `Arrow`, `CurvedArrow`, `Dot`, `LabeledDot`, `Polygon`, `Star`, `Arc`, `ArcBetweenPoints`, `CubicBezier`.
- Math & text: `MathTex`, `Tex`, `Text`, `MarkupText`, `DecimalNumber`, `Integer`, `Variable`, `Table`, `MathTable`, `Code` (see `math-and-text.md`).
- Coordinate systems: `Axes`, `NumberPlane`, `NumberLine`, `ComplexPlane`, `PolarPlane`, `ThreeDAxes` (see `graphs-and-updaters.md`).
- Grouping: `VGroup(a, b, c)`, then `.arrange(DOWN, buff=0.3)`, `.arrange_in_grid(rows, cols)`.
- Position: `.shift(UP*2)` (relative), `.move_to(ORIGIN)` (absolute), `.next_to(other, RIGHT, buff=0.5)`, `.align_to(other, LEFT)`, `.to_edge(UP)`, `.to_corner(UL)`. Directions: `UP DOWN LEFT RIGHT ORIGIN UL UR DL DR IN OUT`.
- Style: `.set_fill(color, opacity)`, `.set_stroke(color, width, opacity)`, `.set_color(c)`, `.set_opacity(x)`, `.set_z_index(n)`.
- `self.add(m)` shows instantly, `self.remove(m)` hides; later-added objects draw on top.

## Animations

- Construction: `Create`, `Write`, `DrawBorderThenFill`, `FadeIn`, `FadeOut`, `GrowFromCenter`, `GrowArrow`.
- Change: `Transform(a, b)`, `ReplacementTransform(a, b)`, `TransformMatchingTex`, `Rotate`, `MoveAlongPath`.
- Emphasis: `Indicate`, `Circumscribe`, `Flash`, `Wiggle` (full vocabulary in `effects-and-transitions.md`).
- `.animate` animates any method chain: `self.play(sq.animate.shift(UP).set_fill(RED))`.
- Several at once: `self.play(Create(a), FadeIn(b), run_time=2)`; staggered: `LaggedStart(*anims, lag_ratio=0.2)`.
- Every `play()` takes `run_time=` and `rate_func=`; `self.wait(t)` holds.

## Timing budgets

When the caller gives a duration per scene or per beat, the scheduled time must add up to it exactly:

```python
budget = 4.2                      # seconds given for this beat
used = 0
self.play(Write(eq), run_time=1.5); used += 1.5
self.play(Indicate(eq[2]), run_time=0.8); used += 0.8
self.wait(max(0, budget - used))
```

`wait()`, `move_camera()` and every `play()` count toward the budget.

## Quick reference

| Need | Use |
|---|---|
| Show instantly / animate on | `self.add(m)` / `self.play(Create(m))` |
| Animate a method | `self.play(m.animate.shift(UP))` |
| Morph / replace | `Transform(a, b)` / `ReplacementTransform(a, b)` |
| Typeset math | `MathTex(r"e^{i\pi}+1=0")`, animate with `Write` |
| Morph equations | `TransformMatchingTex(eq1, eq2)` with `{{ }}` groups |
| Plot a function | `ax = Axes(...); ax.plot(lambda x: x**2)` |
| Live / linked value | `ValueTracker` + `always_redraw(...)` |
| Position relative | `m.next_to(other, RIGHT, buff=0.3)` |
| Stagger a group | `LaggedStart(*anims, lag_ratio=0.2)` |
| 2D camera push | `MovingCameraScene` + `self.camera.frame.animate.scale(0.5).move_to(x)` |
| 3D view | `ThreeDScene` + `self.set_camera_orientation(phi=65*DEGREES, theta=-45*DEGREES)` |

## Gotchas

- **LaTeX is required** for `Tex`/`MathTex` (not for `Text`). A missing-glyph box or compile error means LaTeX is not installed or the TeX string is bad. Always raw strings `r"..."`.
- `Transform(a, b)` mutates `a` to look like `b` (`b` is never added); `ReplacementTransform(a, b)` leaves `b` on screen — pick based on which object you keep referencing.
- `.animate` interpolates start → end states, so rotations can take odd paths; use `Rotate` when the path matters.
- Updaters keep running — `mob.clear_updaters()` (or `remove_updater`) when done, or later animations fight them.
- `construct()` runs once to *script* the timeline; never use wall-clock time, and seed any randomness.
- `set_default` is per class; setting it on `VMobject` does not reach `Line`, `Circle`, … (see `style-and-color.md` §3).
- `Text` (Pango) can space letters oddly; prefer `Tex` for prose unless a specific font or Vietnamese text is needed.

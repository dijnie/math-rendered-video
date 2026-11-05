# Effects, emphasis & transitions

Every effect should *mean* something. Pick from the vocabulary below by intent, and use the same effect for the same intent throughout a video.

## 1. Entrances — "this is new"

| Effect | Reads as | Typical use |
|---|---|---|
| `Write(m)` | being written by hand | equations, text, chalkboard look |
| `Create(m)` | being drawn | lines, curves, shapes, axes |
| `DrawBorderThenFill(m)` | outline then body | filled shapes, icons, big glyphs |
| `FadeIn(m, shift=UP*0.3)` | arriving quietly | labels, secondary items |
| `FadeIn(m, scale=1.2)` / `GrowFromCenter(m)` | popping in | a result, a key point |
| `GrowFromPoint(m, point)` / `GrowFromEdge(m, LEFT)` | emerging from a source | a vector from the origin, a bar from the axis |
| `GrowArrow(arrow)` | pointing | arrows |
| `SpinInFromNothing(m)` | playful arrival | rare, light tone only |
| `AddTextLetterByLetter(Text(...))` / `TypeWithCursor` | typed | terminal, code, typewriter look (`Text` only) |

Exits mirror them: `Unwrite`, `Uncreate`, `FadeOut(m, shift=DOWN*0.3)`, `ShrinkToCenter`. Exit faster than entrance (≈0.5–0.7× the time).

## 2. Emphasis — "look here"

| Effect | Strength | Notes |
|---|---|---|
| `m.animate.set_color(ACCENT)` | soft, persistent | best for colour coding that stays |
| `Indicate(m, color=ACCENT, scale_factor=1.15)` | short pulse | one term in an equation |
| `Circumscribe(m, color=ACCENT, fade_out=True)` | draws a ring around | a result, a region |
| `Create(SurroundingRectangle(m, corner_radius=0.1))` | box stays | the boxed final answer |
| `Create(Underline(m))` | quiet | a word in a sentence |
| `Flash(point, color=ACCENT)` | spark | a point appears or two curves intersect |
| `FocusOn(point)` | spotlight closing in | where to look in a busy frame |
| `ShowPassingFlash(m.copy().set_stroke(ACCENT, 6), time_width=0.4)` | light travelling along a path | a path, a flow, a circuit |
| `ApplyWave(m)` / `Wiggle(m)` | shake | "this is unstable / wrong / alive" |
| `Broadcast(Circle(...), focal_point=p)` | rings spreading out | a source, a signal |
| `Create(Cross(m))` | strike | a wrong step |
| `Brace(m, DOWN)` + `BraceLabel` | naming a part | "this whole thing is the variance" |

**Dim the rest** is the strongest emphasis of all: `self.play(*[x.animate.set_opacity(0.25) for x in others], m.animate.set_color(ACCENT))`.

## 3. Transformations — "this becomes that"

| Need | Use |
|---|---|
| An equation changes step by step | `TransformMatchingTex(eq1, eq2)` (with `{{ }}` groups), see `math-and-text.md` |
| Shapes / text with no TeX structure | `TransformMatchingShapes(a, b)` |
| Keep the original, show where a copy goes | `TransformFromCopy(term, target)` — a term "moves" into the next line |
| Morph one object into another | `ReplacementTransform(a, b)` (keep `b`), `Transform(a, b)` (keep `a`) |
| Two unrelated objects swap | `FadeTransform(a, b)` (cross-fade) |
| Rotate-like morph | `ClockwiseTransform` / `CounterclockwiseTransform` |
| Move along a curve | `MoveAlongPath(dot, path)` |
| Deform space | `ApplyMatrix(matrix, plane)`, `ApplyPointwiseFunction(f, mob)`, `Homotopy(...)` (`plane.prepare_for_nonlinear_transform()` first) |
| Linear-algebra scenes | `LinearTransformationScene` with `self.apply_matrix([[1,1],[0,1]])` |
| Leave a trail | `TracedPath(dot.get_center, stroke_color=ACCENT, dissipating_time=0.5)` |

## 4. Choreography

```python
self.play(LaggedStart(*[FadeIn(d, shift=UP*0.2) for d in dots], lag_ratio=0.1), run_time=2)
self.play(LaggedStartMap(Create, lines, lag_ratio=0.15), run_time=2)
self.play(Succession(Create(ax), Create(curve), FadeIn(label)), run_time=3)   # one after another
self.play(AnimationGroup(Write(eq), Create(box), lag_ratio=0.5))              # overlapping
self.play(ShowIncreasingSubsets(group), run_time=2)                           # pieces appear one by one
self.play(ChangeSpeed(anim, speedinfo={0.3: 1, 0.6: 0.3, 1: 1}))              # slow-motion middle
```

- `lag_ratio` 0.05–0.2 for many small items, 0.3–0.6 for a few large ones.
- Overlap steps a little (`AnimationGroup(..., lag_ratio=0.6)`) so the video never stops dead between actions.
- Rhythm: action → hold (let it read) → next action. A hold is `self.wait(0.5–2)`.

## 5. Easing (`rate_func=`)

| Curve | Feels | Use |
|---|---|---|
| `smooth` (default) | natural ease in-out | almost everything |
| `linear` | mechanical | tracers, scanning, loops, constant flow |
| `rush_from` / `ease_out_cubic` | fast start, soft landing | entrances, objects arriving |
| `rush_into` / `ease_in_cubic` | soft start, fast end | exits |
| `there_and_back` | goes and returns | pulse, "try this value then go back" |
| `there_and_back_with_pause` | goes, holds, returns | showing an extreme case |
| `ease_out_back` | slight overshoot | playful pops |
| `ease_out_bounce` / `wiggle` | cartoon | rarely |
| `double_smooth`, `lingering` | long settle | camera moves |

## 6. Scene-to-scene transitions

Manim renders each `Scene` as its own clip, so transitions live **inside** the scenes:

- **Clean cut**: end the scene on a held frame (`self.wait(0.5)`), start the next on a matching layout.
- **Fade through background**: last play `FadeOut(*self.mobjects)`, next scene starts with `FadeIn`.
- **Carry-over**: rebuild the last object of scene N at the same place at the start of scene N+1 and transform it — the viewer sees continuity.
- **Wipe**: `FullScreenRectangle().set_fill(BG, 1)` sliding in with `.animate.shift(...)`.
- **Camera hand-off**: in `MovingCameraScene`, zoom into an object, cut, start the next scene zoomed-in on the same object and pull out.
- Within one scene, clear the stage with `self.play(*[FadeOut(m) for m in self.mobjects])`.

## 7. Counters & live readouts

```python
v = ValueTracker(0)
num = always_redraw(lambda: DecimalNumber(v.get_value(), num_decimal_places=2, color=ACCENT).next_to(dot, UP))
var = Variable(0, MathTex("x"), num_decimal_places=2)   # "x = 0.00", track with var.tracker
self.play(v.animate.set_value(3.14), run_time=2)
```

Use `Integer` for counts. Keep readouts in a fixed spot (top-right) when they should not chase an object.

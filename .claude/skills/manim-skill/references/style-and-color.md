# Style, colour & background

Decide the look **before** writing scenes and put it in one place at the top of `script.py` (a palette block + `set_default` calls). Every scene then reads from those names, never from ad-hoc hex values.

## 1. Background

```python
config.background_color = "#14161b"        # whole render
# or per scene: self.camera.background_color = "#14161b"
```

- Pure black `#000000` looks cheap on most screens and crushes dark strokes; use an off-black with a slight hue (`#0e1117`, `#14161b`, `#1b1d23`).
- A light background (paper, whiteboard) needs every default colour flipped — Manim's defaults are white text and white strokes (see §3).
- **Gradient / vignette background**: a full-screen rectangle behind everything.

```python
bg = FullScreenRectangle(stroke_width=0).set_fill(
    color=["#1b2233", "#0b0d12"], opacity=1        # list = gradient
).set_sheen_direction(DOWN)
bg.set_z_index(-10)
self.add(bg)
```

- **Grid / blueprint background**: a faint `NumberPlane` that is *decoration*, not data.

```python
grid = NumberPlane(
    background_line_style={"stroke_color": "#2a4a6b", "stroke_width": 1, "stroke_opacity": 0.5},
    faded_line_ratio=4, axis_config={"stroke_opacity": 0},
).set_z_index(-5)
```

- Texture (paper grain, chalk dust): an `ImageMobject("paper.png").scale_to_fit_height(config.frame_height)` at `z_index=-10`, kept subtle (opacity 0.3–0.6).

## 2. Palette — one job per colour

A palette is **roles**, not a rainbow:

| Role | Use | Rule |
|---|---|---|
| `BG` | background | the only full-frame colour |
| `INK` | default text, axes, neutral strokes | ~85–95 % contrast with BG, not pure white on dark |
| `MUTED` | secondary labels, grid, de-emphasised parts | INK at lower contrast |
| `ACCENT` | **the thing that matters right now** | one at a time; it moves as the explanation moves |
| `A2`, `A3` | second / third quantity that must stay distinct (x vs y, before vs after) | keep the mapping fixed for the whole video |
| `WARN` | error, contradiction, "this is wrong" | rare |

Colour coding is meaning: once `x` is yellow, `x` is yellow in every equation, label and graph of the film. Use `set_color_by_tex` / `t2c` to keep it.

### Ready-made looks

| Look | BG | INK | MUTED | ACCENT | A2 / A3 | Notes |
|---|---|---|---|---|---|---|
| Classic explainer (3b1b-like) | `#0f1115` | `#ece9e1` | `#6b7280` | `#f4c542` yellow | `#58c4dd` teal, `#fc6255` red | CMU / default LaTeX, thin strokes, calm |
| Chalkboard | `#1f2f28` | `#e9efe6` | `#7d9488` | `#ffd166` | `#8fd3ff`, `#ff8fa3` | `TexFontTemplates.chalkduster` or a hand font, texture overlay, `Write` everything |
| Paper / print | `#f4efe6` | `#1d1d1f` | `#8a8378` | `#c8442f` vermilion | `#2f5d8a` navy, `#3d7a4f` green | flip defaults (§3), thicker strokes (3–4), serif text |
| Blueprint | `#0d2440` | `#e6f0ff` | `#5d7fa6` | `#ffcc4d` | `#7fd1ff` | faint grid background, `DashedLine` construction lines, monospace labels |
| Neon / dark tech | `#08090f` | `#d7dcf0` | `#3c4258` | `#00e5ff` cyan | `#ff3d81` magenta, `#b4ff39` lime | glow (§5), minimal text |
| Minimal mono | `#fafafa` | `#111111` | `#9a9a9a` | `#ff5a1f` | — | one accent only, lots of empty space |

```python
BG, INK, MUTED = "#0f1115", "#ece9e1", "#6b7280"
ACCENT, A2, A3, WARN = "#f4c542", "#58c4dd", "#83c167", "#fc6255"
config.background_color = BG
```

Manim's own constants are fine as a base (`BLUE_A … BLUE_E`, `TEAL`, `YELLOW`, `GOLD`, `MAROON`, `PURPLE`, `GREY_B`); `_A` is lightest, `_E` darkest.

## 3. Defaults — set them once

```python
for cls in (Text, Tex, MathTex, MarkupText, Line, Arrow, DashedLine, Circle, Square, Rectangle, Polygon):
    cls.set_default(color=INK)
Dot.set_default(color=ACCENT)
axis_style = {"color": MUTED}            # pass as Axes(axis_config=axis_style)
```

`set_default` works per class: call it on each class you actually use (setting it on `VMobject` does **not** reach `Line`, `Circle`, … because they pass their own colour). Axes and planes take colours through `axis_config` / `background_line_style`. For a light background this is mandatory, otherwise everything renders white-on-cream; check one still with `manim -s`. `cls.set_default()` with no arguments restores Manim's original defaults.

## 4. Strokes, fills, sizes

- Stroke width: default 4. Thin & elegant 2–3 on dark; 3–5 on light or small render sizes (480p eats thin lines).
- Fills: shapes as `set_fill(color, opacity=0.15–0.35)` + a solid stroke of the same hue reads cleaner than an opaque fill.
- Areas under curves, regions: `opacity` 0.3–0.5; never hide what is under them.
- Type scale (default `font_size=48`): title 56–72, headline / main equation 44–56, body 32–40, labels 24–30. More than three sizes on screen is noise.
- `DashedLine` / `DashedVMobject(mob, num_dashes=…)` for construction lines, projections, "not real yet".

## 5. Colour tools

```python
interpolate_color(BLUE, RED, 0.3)                    # a colour between two
color_gradient([BLUE, GREEN, YELLOW], 10)            # list of 10 steps
VGroup(*dots).set_color_by_gradient(BLUE, YELLOW)    # spread over submobjects
mob.set_sheen(0.4, UR)                               # soft highlight across a fill
ManimColor("#f4c542").darker(0.3) / .lighter(0.3)    # shades of a palette colour
```

**Glow** (no built-in): stack copies with growing width and falling opacity behind the line.

```python
def glow(mob, color, layers=6, width=18, opacity=0.08):
    g = VGroup(*[
        mob.copy().set_stroke(color, width=width * i / layers, opacity=opacity).set_fill(opacity=0)
        for i in range(layers, 0, -1)
    ])
    return VGroup(g, mob)
```

Use glow on one or two hero objects, not everything.

**Backing plate for text over busy art**: `BackgroundRectangle(label, fill_opacity=0.8, buff=0.15)` or `SurroundingRectangle(label, corner_radius=0.1, buff=0.2).set_fill(BG, 0.85)`.

## 6. Avoiding the generic look

- Not default blue-circle-on-black. Choose a look from §2 and commit.
- One accent at a time; dim (`set_opacity(0.3)` or `MUTED`) what is no longer the topic instead of removing it.
- Fewer, larger objects; generous margins; empty space is part of the design.
- Motion that explains (build → transform → highlight), not motion that decorates.
- Consistent object vocabulary: the same kind of thing always looks the same (all vectors arrows of one width, all points dots of one radius).

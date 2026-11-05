# Layout & composition

## 1. The frame

- Default frame is 14.22 × 8 units (16:9), centre `ORIGIN`. Read the real edges from `config.frame_width / frame_height`, `config.left_side`, `config.top`.
- **Safe margin**: keep content at least 0.5 units (≈ `MED_LARGE_BUFF`) from every edge — `to_edge(UP, buff=0.5)`, `to_corner(UL, buff=0.5)`.
- Spacing constants: `SMALL_BUFF` 0.1, `MED_SMALL_BUFF` 0.25, `MED_LARGE_BUFF` 0.5, `LARGE_BUFF` 1.
- Fit long things: `m.scale_to_fit_width(config.frame_width - 1)`, `m.set(width=…)`, `m.scale(0.8)`.

## 2. Standard layouts

| Layout | How | When |
|---|---|---|
| Centre stage | one hero object at `ORIGIN`, title `to_edge(UP)` | a single equation or shape |
| Title + body | `Title("…")` (has an underline) or `Tex(...).to_edge(UP)`; body `next_to(title, DOWN, buff=0.6)` | chapter openers |
| Split screen | `left.move_to(LEFT * config.frame_width / 4)`, `right.move_to(RIGHT * config.frame_width / 4)` | picture + algebra, before vs after |
| Graph + side panel | axes shifted left (`ax.to_edge(LEFT)`), equations stacked on the right | function analysis |
| Derivation column | `VGroup(*lines).arrange(DOWN, aligned_edge=LEFT, buff=0.35)` | step-by-step algebra |
| Grid | `VGroup(*items).arrange_in_grid(rows=2, cols=3, buff=0.6)` | comparing cases |
| Table | `MathTable([[…]], include_outer_lines=True)` / `Table` | values, truth tables |

## 3. Hierarchy

- One focal point per moment; everything else smaller, dimmer, or gone.
- At most ~3 lines of prose on screen; say the rest with pictures (or let the caller's voice-over say it).
- Align equations on `=`: build each line as `MathTex("a", "=", "b")` and `line.shift((prev[1].get_x() - line[1].get_x()) * RIGHT)`, or use one `MathTex` with `&=` and `\\` for a static block.
- Labels sit next to what they label (`next_to(obj, UR, buff=0.1)`), never in a legend far away.

## 4. Layering

- Later `add`/`play` draws on top; force order with `m.set_z_index(n)` (background −10, grid −5, content 0, labels 5, overlays 10).
- Text over lines or fills: give it a `BackgroundRectangle` so strokes don't run through glyphs.
- In 3D, labels that must stay readable go through `self.add_fixed_in_frame_mobjects(label)`.

## 5. Vertical (9:16) and square

- 9:16 frame is 9 × 16 units (set `config.frame_width = 9`, `frame_height = 16`). Stack vertically: title top third, visual middle, equation bottom third.
- Font sizes must go **up** relative to frame width — a 48 pt equation that fits 16:9 often needs `scale_to_fit_width(config.frame_width - 1)`.
- Avoid side-by-side layouts in 9:16; use top/bottom instead.
- Keep the bottom ~15 % free if the caller may add captions there.

## 6. Layout hygiene

- Build with relative placement (`next_to`, `arrange`, `align_to`, `ax.c2p`) — no hand-tuned coordinates that break when a label changes.
- Group what moves together (`VGroup`) so a whole block can be shifted, scaled or faded at once.
- Before animating a change, compute the target layout (`target = eq.copy().next_to(...)`) and transform into it — objects land where the layout says.
- Debug overlaps fast: `manim -s` the scene, or `self.add(index_labels(eq[0]))` to see glyph indices.

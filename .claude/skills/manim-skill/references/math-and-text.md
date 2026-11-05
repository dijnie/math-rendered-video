# Math & Text in Manim

LaTeX is required for `Tex`/`MathTex` (install a TeX distribution: TeX Live / MiKTeX). `Text`/`MarkupText` use Pango and need no LaTeX. **Always use raw strings `r"..."`** for TeX so backslashes survive Python.

## Which class

| Class | Engine | Use for |
|---|---|---|
| `Text` | Pango | Plain labels, titles, captions (fonts, weight, slant) |
| `MarkupText` | Pango + markup | Inline styled spans without LaTeX |
| `Tex` | LaTeX (text mode) | Typeset prose with occasional math |
| `MathTex` | LaTeX (math mode, `align*`) | Equations and formulas |

```python
title = Text("Euler's identity", font="Noto Sans", weight=BOLD, font_size=48)
eq    = MathTex(r"e^{i\pi} + 1 = 0", font_size=96)
prose = Tex(r"The area is $\pi r^2$.")
self.play(Write(title))
self.play(Write(eq))
```

## Styling text

```python
Text("RED", color=RED)
Text("Hello", t2c={"[1:-1]": BLUE})            # color by slice
Text("World", t2c={"rl": RED})                  # color by matched chars
Text("Hi", gradient=(RED, BLUE, GREEN))
MarkupText(f'plain <span fgcolor="{YELLOW}">highlight</span>')
```

## Coloring parts of an equation

```python
# A. multiple args, color one
t = MathTex("a^2", "+", "b^2", "=", "c^2")
t.set_color_by_tex("c^2", YELLOW)

# B. isolate substrings inside one string
e = MathTex(r"e^{x} = x^0 + x^1 + \tfrac{1}{2}x^2", substrings_to_isolate="x")
e.set_color_by_tex("x", YELLOW)

# C. {{ }} groups (Manim syntax) — best for matching transforms
eq = MathTex(r"{{a^2}} + {{b^2}} = {{c^2}}")
```

## Morphing one equation into another

`TransformMatchingTex` matches identical sub-TeX between two `MathTex` and morphs only what changed — ideal for algebra steps. Use `{{ }}` groups so terms align.

```python
src = MathTex(r"{{a}}^2 + {{b}}^2 = {{c}}^2")
dst = MathTex(r"{{c}}^2 = {{a}}^2 + {{b}}^2")
self.play(Write(src))
self.play(TransformMatchingTex(src, dst))      # terms fly to new positions
```

For non-TeX shape matching use `TransformMatchingShapes`. For a hard cut between unrelated equations use `ReplacementTransform(eq1, eq2)`.

## Custom LaTeX packages

```python
tmpl = TexTemplate()
tmpl.add_to_preamble(r"\usepackage{mathrsfs}")
MathTex(r"\mathscr{H} \to \mathbb{H}", tex_template=tmpl)
```

## Indexing into rendered glyphs

`MathTex`/`Tex` are `VGroup`s of submobjects; index to animate a single piece: `eq[0][2]` is the 3rd glyph of the 1st arg. `Indicate(eq[0])`, `eq[2].animate.set_color(RED)`. Prefer `{{ }}` groups or `index_labels(eq)` (debug) over guessing indices.

## Typography — fonts and looks

- `Text(..., font="Inter")` uses any font installed on the machine (`fc-list | grep -i name` to check). Good pairs: a clean sans (Inter, IBM Plex Sans, Source Sans 3) for labels + LaTeX math; a serif (EB Garamond, Libertinus) for a print/paper look; a mono (JetBrains Mono, IBM Plex Mono) for code and blueprint labels. Vietnamese text: use a font with full diacritics (Be Vietnam Pro, Inter, Noto Sans) via `Text`, since default LaTeX templates do not handle Vietnamese.
- `weight=BOLD|SEMIBOLD|LIGHT`, `slant=ITALIC`, `line_spacing=`, `disable_ligatures=True` (fixes odd spacing in some fonts).
- Change the LaTeX look as a whole with a font template:

```python
MathTex(r"\int_0^1 x^2\,dx", tex_template=TexFontTemplates.libertine)
Tex(r"Chalk look", tex_template=TexFontTemplates.chalkduster)   # needs the font installed
config.tex_template = TexFontTemplates.palatino                # global
```

  Useful members: `libertine`, `palatino`, `vollkorn`, `gfs_didot`, `latin_modern_tw` (typewriter), `comfortaa`, `chalkduster`, `french_cursive`, `droid_sans`. The default (Computer Modern) is the classic "math paper / 3b1b" look.
- `Paragraph("line one", "line two", alignment="left")` for multi-line `Text`; `Title("Chapter 1")` gives a top title with an underline.
- Code on screen: `Code(code_string=src, language="python", background="window", formatter_style="monokai", add_line_numbers=False)`; highlight a line by boxing or colouring `code.code_lines[i]`.
- Sizes: keep to three levels (title / main / label). Math is visually larger than text at the same `font_size`; drop `MathTex` labels ~10–15 % below the prose next to them.

## Making math readable

- Write the equation, **then** colour the terms in the palette roles (`set_color_by_tex`), then animate — colour is part of the meaning (see `style-and-color.md` §2).
- Reveal long expressions in pieces (`Write(eq[0])`, `Write(eq[1:])`) or `TransformFromCopy` terms from where they come from.
- Box or `Circumscribe` the final result; leave it on screen for at least 1.5 s.
- Show the substitution, don't jump: `TransformMatchingTex` from the general form to the specific one.

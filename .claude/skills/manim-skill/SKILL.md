---
name: manim-skill
description: Style and craft guide for Manim Community Edition (manimce) — look and palette, background, typography, math and text, graphs, effects and transitions, layout, camera angles and 3D, plus the core API and still-frame checks. Produces distinctive, production-grade math animation scenes that avoid generic "AI slop" aesthetics. Use whenever Manim code is written or debugged — animating an equation, a 3Blue1Brown-style scene, plotting or animating a graph/function, visualizing a math/physics/CS concept, morphing formulas, animating a geometric proof or an algorithm. Covers only the Manim work; cutting, joining, audio, voice-over and delivery belong to the video pipeline (code-rendered-video).
compatibility: Requires Python 3.9+, Manim Community Edition, ffmpeg, and a LaTeX distribution for Tex/MathTex.
---

# Manim scenes

You are a Manim animation expert. This skill covers writing and rendering Manim scenes: the look, the code, and checking the result. Output is a `script.py` plus one rendered MP4 per scene. Cutting, joining, music, voice-over, captions and delivery are the calling pipeline's job.

## Steps

1. **Decide the look first.** Pick one look and its colour roles, background, fonts and type sizes from [style-and-color](references/style-and-color.md) and [math-and-text](references/math-and-text.md). Colour is meaning: a quantity keeps its colour for the whole video.
2. **Start from the template.** Copy [assets/scene-template.py](assets/scene-template.py) as `script.py`, set the render size for the target format, replace its LOOK block with the chosen look.
3. **Plan each scene's composition and motion.** Choose the layout ([layout-and-composition](references/layout-and-composition.md)), the effects by intent ([effects-and-transitions](references/effects-and-transitions.md)) and the camera per shot ([3d-and-camera](references/3d-and-camera.md)). Graph scenes: [graphs-and-updaters](references/graphs-and-updaters.md).
4. **Write the scenes** following the rules below; API details in [core-api](references/core-api.md).
5. **Check stills, render, check again** as in [rendering-and-checks](references/rendering-and-checks.md). Fix and re-render only the affected scenes.

## Rules

- One `Scene` class per scene, named descriptively (`Scene1_Introduction`, `Scene2_DerivePDE`), so scenes re-render one at a time.
- Render config and the look live at the top of `script.py`; scenes use the palette names, never ad-hoc colours.
- Explicit `run_time=` on every `play()`; `wait()` holds on key states (≈1–2 s per short line, longer for dense equations). If the caller gives a time budget, scheduled time must match it exactly.
- `MathTex` for formulas, `Tex` for prose (`Text` for a specific font or Vietnamese); raw strings for all TeX.
- Relative layout only (`next_to`, `arrange`, `align_to`, `ax.c2p`); everything inside the frame with margins.
- One accent and one focal point at a time; dim what is no longer the topic instead of deleting it.
- Every effect has an intent, and the same intent uses the same effect throughout.
- Hold the camera still while something is being read.

## References

| File | Read when |
|---|---|
| [references/style-and-color.md](references/style-and-color.md) | choosing background, palette, look, stroke and type sizes, glow |
| [references/math-and-text.md](references/math-and-text.md) | equations, colouring terms, equation morphs, fonts, Vietnamese text, code on screen |
| [references/graphs-and-updaters.md](references/graphs-and-updaters.md) | axes, plots, areas, fields, charts, trackers and updaters |
| [references/effects-and-transitions.md](references/effects-and-transitions.md) | entrances, emphasis, transforms, choreography, easing, scene transitions |
| [references/layout-and-composition.md](references/layout-and-composition.md) | frame, margins, standard layouts, z-order, 9:16 |
| [references/3d-and-camera.md](references/3d-and-camera.md) | 3D scenes, moving / zoomed camera, camera angles per shot |
| [references/core-api.md](references/core-api.md) | Mobjects, animations, timing budgets, quick reference, gotchas |
| [references/rendering-and-checks.md](references/rendering-and-checks.md) | render flags, config, output paths, still-frame checks |
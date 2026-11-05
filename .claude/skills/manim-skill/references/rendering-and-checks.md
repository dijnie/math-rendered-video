# Rendering & checks

## Setup

```bash
pip install manim          # Python 3.9+, ffmpeg, and a LaTeX distribution (for Tex/MathTex)
manim --version
```

## Render

```bash
manim script.py Scene1_Intro Scene2_Main      # render the listed Scene classes
```

| Flag | Effect |
|---|---|
| `-s` | save the last frame as a PNG, no video encode |
| `-n a,b` | render only animations `a..b` (stop early to inspect a mid moment) |
| `-q l\|m\|h\|k` | quality preset; **overrides** the resolution/fps in `config` and changes the output folder — leave it off when `script.py` sets its own config |
| `-t` | transparent background (for overlays; output is `.mov`) |
| `--format=gif` | GIF instead of MP4 |
| `-o name` | output file name |

Output paths:
- videos: `media/videos/<file>/<pixel_height>p<frame_rate:g>/<Scene>.mp4`
- stills: `media/images/<file>/<Scene>*.png`

## Render config

Set in `script.py` (see `assets/scene-template.py`): `config.pixel_width`, `config.pixel_height`, `config.frame_width`, `config.frame_height`, `config.frame_rate`, `config.background_color`. Keep pixel and frame aspect ratios matched.

| Format | Iteration size | Frame (units) |
|---|---|---|
| 16:9 | 854×480 @ 15 | 16 × 9 |
| 9:16 | 480×854 @ 15 | 9 × 16 |
| 1:1 | 480×480 @ 15 | 8 × 8 |

Raise to the final size (e.g. 1920×1080 @ 60) only for the last render.

## Check by frames

Manim is deterministic — the same scene renders the same frames — so check stills before and after the video render:

```bash
manim -s script.py Scene2_Main                 # last frame
manim -s script.py Scene2_Main -n 0,3          # frame after the first 3 animations
ffmpeg -y -ss 7 -i media/videos/script/480p15/Scene2_Main.mp4 -vframes 1 f7.png   # any moment of a clip
ffprobe -v error -show_entries stream=width,height,r_frame_rate:format=duration -of compact media/videos/script/480p15/Scene2_Main.mp4
```

Read each PNG and check:

1. Equations and labels are mathematically correct; LaTeX compiled (no blank or box glyphs).
2. Nothing overlaps; everything sits inside the frame with margins.
3. The look holds: palette roles respected, one focal point, text readable at the render size.
4. Timing reads well — holds on key states, groups staggered, `run_time`s match any budget given.
5. Each clip has the expected size, fps and duration, and every listed scene rendered without errors.

When feedback names a moment (e.g. `[0:07] the c² label overlaps the triangle`), extract that exact frame and read it before touching code, then re-render only the affected scene.

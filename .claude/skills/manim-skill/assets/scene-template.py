"""Starting point for a Manim script.

Copy this file as script.py, then:
1. set the render size for the target format (iteration sizes below),
2. replace the LOOK block with one look from references/style-and-color.md,
3. replace the example scene with the real scenes (one class per scene).
"""

from manim import *

# --- RENDER --------------------------------------------------------------
# 16:9 -> 854x480, frame 16x9 | 9:16 -> 480x854, frame 9x16 | 1:1 -> 480x480, frame 8x8
# Raise to the final size (e.g. 1920x1080 @ 60) only for the last render.
config.pixel_width = 854
config.pixel_height = 480
config.frame_width = 16
config.frame_height = 9
config.frame_rate = 15

# --- LOOK: classic dark explainer ----------------------------------------
BG, INK, MUTED = "#0f1115", "#ece9e1", "#6b7280"
ACCENT, A2, A3, WARN = "#f4c542", "#58c4dd", "#83c167", "#fc6255"

config.background_color = BG
# set_default is per class: list every class the scenes use.
for cls in (Text, Tex, MathTex, MarkupText, Line, Arrow, DashedLine, Circle, Square, Rectangle, Polygon):
    cls.set_default(color=INK)
Dot.set_default(color=ACCENT)
AXIS_STYLE = {"color": MUTED, "stroke_width": 2}  # Axes(axis_config=AXIS_STYLE)

# Colour coding: a quantity keeps its colour for the whole video.
T2C = {"a": A2, "b": A3, "c": ACCENT}


# --- SCENES --------------------------------------------------------------
class Scene1_Introduction(Scene):
    def construct(self):
        title = Tex("Pythagoras", font_size=56).to_edge(UP, buff=0.6)
        eq = MathTex("a^2", "+", "b^2", "=", "c^2", font_size=72)
        for term, color in T2C.items():
            eq.set_color_by_tex(term, color)

        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.8)
        self.play(Write(eq), run_time=1.5)
        self.play(Circumscribe(eq[-1], color=ACCENT), run_time=1)
        self.wait(1.5)

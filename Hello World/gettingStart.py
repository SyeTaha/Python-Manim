from manim import *

config.pixel_width = 1080
config.pixel_height = 1920

config.frame_width = 9
config.frame_height = 16

config.background_color = "#0d1117"


class CodeFromString(Scene):
    def construct(self):

        rendered_code = Code(
            file_name="code.cpp",
            tab_width=4,
            background="rectangle",
            language="cpp",
            font="Monospace",
            insert_line_no=False,
            font_size=20,  # Adjust font size
            style="github-dark",
            corner_radius=0,
            background_stroke_color=config.background_color,
            line_spacing=1,
        )

        rendered_code.set_width(config.frame_width)

        self.play(Write(rendered_code), run_time=5)
        self.wait(3)

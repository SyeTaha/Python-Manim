from manim import *

line_stroke_width = 2

config.default_stroke_width = 1


class Expressions:
    def get_weighted_sum_expression(self):
        return MathTex(
            r"\text{Estimate} = \sum_{i=1}^{n} (w_i \cdot x_i) + \text{Bias}"
        ).shift(DOWN)

    def get_PLR_expression(self):
        return MathTex(r"w_i = w_i + \alpha \cdot (\Delta \, L) \cdot x_1").shift(DOWN)

    def get_PLR_expression_updated(self):
        return MathTex(
            r"w_i = w_i + \alpha \cdot (\text{Actual} - \text{Estimate}) \cdot x_1"
        ).shift(DOWN * 0.4)


class Diagram:
    def get_diagram(self):

        # Create the Circles representing Inputs
        input1 = self.get_circle().shift(LEFT * 3 + UP * 2)
        input2 = self.get_circle().shift(LEFT * 3 + UP * 0.75)
        input3 = self.get_circle().shift(LEFT * 3 + DOWN * 0.5)
        input_n = self.get_circle().shift(LEFT * 3 + DOWN * 2.5)

        bias = Circle(radius=0.25, color=WHITE, stroke_width=1).shift(DOWN * 2)

        # Create the circle representing Perceptron
        perceptron = self.get_circle()

        output = MathTex("Output").shift(RIGHT * 3)

        # variable_labels = VGroup(label1, label2, label3, labeln)
        variable_labels = self.get_labels(input1, input2, input3, input_n)

        label_bias = MathTex("Bias").move_to(bias).shift(DOWN * 0.5)
        label_bias.font_size = 20

        perceptron_label = MathTex("Perceptron").move_to(perceptron).shift(UP)
        perceptron_label.font_size = 30

        # Create arrows
        input3_inputn = DashedLine(
            start=input3.get_bottom(),
            end=input_n.get_top(),
            color=WHITE,
            stroke_width=line_stroke_width,
            dashed_ratio=0.3,
        )

        lines = self.get_lines(input1, input2, input3, input_n, perceptron)

        bias_perceptron = Line(
            start=bias.get_top(),
            end=perceptron.get_bottom(),
            color=WHITE,
            stroke_width=line_stroke_width,
        )

        perceptron_output = Arrow(
            perceptron.get_right(),
            output.get_left(),
            color=WHITE,
            stroke_width=1,
            tip_length=0.2,
        )

        return VGroup(
            # Input 1
            input1,
            # Input 2
            input2,
            # Input 3
            input3,
            # Input 3...n
            input3_inputn,
            # Input n
            input_n,
            variable_labels,
            # Perceptron
            perceptron,
            perceptron_label,
            # Point to Perceptron
            lines,
            # Bias
            bias,
            label_bias,
            bias_perceptron,
            # Output
            output,
            perceptron_output,
        )

    def get_circle(self):
        return Circle(radius=0.5, color=WHITE, stroke_width=1)

    def get_labels(self, input1, input2, input3, inputn):
        label1 = MathTex("x_1", stroke_width=0.7).move_to(input1).shift(LEFT)
        label2 = MathTex("x_2", stroke_width=0.7).move_to(input2).shift(LEFT)
        label3 = MathTex("x_3", stroke_width=0.7).move_to(input3).shift(LEFT)
        labeln = MathTex("x_n", stroke_width=0.7).move_to(inputn).shift(LEFT)

        return VGroup(label1, label2, label3, labeln)

    def get_lines(self, input1, input2, input3, inputn, perceptron):
        input1_perceptron = LabeledLine(
            start=input1.get_right(),
            end=perceptron.get_left() + UP * 0.1,  # Shift the endpoint upwards
            color=WHITE,
            stroke_width=line_stroke_width,
            label=MathTex("w_1"),
            label_frame=False,
        )
        input2_perceptron = LabeledLine(
            start=input2.get_right(),
            end=perceptron.get_left(),
            color=WHITE,
            stroke_width=line_stroke_width,
            label=MathTex("w_2"),
            label_frame=False,
        )
        input3_perceptron = LabeledLine(
            start=input3.get_right(),
            end=perceptron.get_left() + DOWN * 0.1,  # Shift the endpoint downwards
            color=WHITE,
            stroke_width=line_stroke_width,
            label=MathTex("w_3"),
            label_frame=False,
        )

        inputn_perceptron = LabeledLine(
            start=inputn.get_right(),
            end=perceptron.get_left()
            + DOWN * 0.2
            + RIGHT * 0.03,  # Shift the endpoint downwards
            color=WHITE,
            stroke_width=line_stroke_width,
            label=MathTex("w_n"),
            label_frame=False,
        )

        return VGroup(
            input1_perceptron, input2_perceptron, input3_perceptron, inputn_perceptron
        )


class Perceptron(Scene):
    def construct(self):
        heading = MathTex(r"\text{Perceptron Learning Rule}", color=WHITE)
        expression_handler = Expressions()
        diagram_handler = Diagram()

        expression = expression_handler.get_weighted_sum_expression()
        update_weights = expression_handler.get_PLR_expression()
        update_weights_transformed = expression_handler.get_PLR_expression_updated()

        diagram = diagram_handler.get_diagram().scale(0.9)

        self.play(Write(heading))
        self.wait()

        self.play(heading.animate.scale(0.9))
        self.play(heading.animate.to_edge(UP))
        self.wait()

        # Add everything to the scene
        self.play(
            Create(diagram),
            run_time=10,
        )
        self.wait()

        self.play(diagram.animate.scale(0.6), run_time=1)
        self.play(diagram.animate.to_edge(UL), run_time=1)
        self.wait()

        self.play(Write(expression))
        self.wait()

        self.play(expression.animate.scale(0.8))
        self.play(expression.animate.shift(DOWN * 2))
        self.wait()

        self.play(Write(update_weights))
        self.wait()

        self.play(Transform(update_weights, update_weights_transformed))
        self.wait()

        # Remove the transformed expression from the scene
        self.remove(update_weights_transformed)

        self.play(update_weights.animate.shift(DOWN * 0.5))
        surrounding_rect = SurroundingRectangle(update_weights, buff=0.1, color=WHITE)

        self.play(Create(surrounding_rect))
        self.wait()

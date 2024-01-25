from manim import *


class QuadraticToCubic(Scene):
    def construct(self):
        # Quadratic equation
        equation_quad = MathTex("ax^2", "+", "bx", "+", "c", "=", "0").set_color_by_gradient(BLUE, GREEN)
        equation_quad.scale(1.5)
        equation_quad.to_edge(UP)

        # Cubic equation (initially hidden)
        equation_cubic = MathTex("ax^3", "+", "bx^2", "+", "cx", "+", "d", "=", "0").set_color_by_gradient(BLUE, GREEN)
        equation_cubic.scale(1.5)
        equation_cubic.next_to(equation_quad, DOWN)

        # Display the quadratic equation
        self.play(Write(equation_quad))

        # Transform quadratic to cubic
        self.play(
            TransformMatchingShapes(
                VGroup(
                    equation_quad[0].copy(),
                    equation_quad[1].copy(),
                    equation_quad[2].copy(),
                    equation_quad[3].copy(),
                    equation_quad[4].copy(),
                    equation_quad[5].copy(),
                    equation_quad[6].copy(),
                ),
                VGroup(
                    equation_cubic[0],
                    equation_cubic[1],
                    equation_cubic[2],
                    equation_cubic[3],
                    equation_cubic[4],
                    equation_cubic[5],
                    equation_cubic[7],
                    equation_cubic[8],
                ),
            ),
            Create(equation_cubic[6]),
            run_time=2
        )

        self.wait(2)


class CubicToDepressedCubic(Scene):
    def construct(self):
        # Cubic equation
        equation_cubic = MathTex("ax^3", "+", "bx^2", "+", "cx", "+", "d", "=", "0").set_color_by_gradient(BLUE, GREEN)
        equation_cubic.scale(1.5)
        equation_cubic.to_edge(UP)

        # Description of substitution
        substitution_desc = MathTex("x = y - \\frac{b}{3a}").scale(1.5)
        substitution_desc.next_to(equation_cubic, DOWN, buff=0.5)

        # Substituted equation (initially hidden)
        equation_substituted = MathTex(
            "a\\left(y-\\frac{b}{3a}\\right)^3", "+", "b\\left(y-\\frac{b}{3a}\\right)^2", "+",
            "c\\left(y-\\frac{b}{3a}\\right)", "+", "d", "=", "0"
        ).set_color_by_gradient(BLUE, GREEN)
        equation_substituted.scale(1.5)
        equation_substituted.next_to(substitution_desc, DOWN)

        # Display the cubic equation and substitution description
        self.play(Write(equation_cubic))
        self.wait()
        self.play(Write(substitution_desc))
        self.wait()

        # Transform cubic to substituted equation
        self.play(
            TransformMatchingShapes(
                VGroup(
                    equation_cubic[0].copy(),
                    equation_cubic[1].copy(),
                    equation_cubic[2].copy(),
                    equation_cubic[3].copy(),
                    equation_cubic[4].copy(),
                    equation_cubic[5].copy(),
                    equation_cubic[6].copy(),
                ),
                VGroup(
                    equation_substituted[0],
                    equation_substituted[1],
                    equation_substituted[2],
                    equation_substituted[3],
                    equation_substituted[4],
                    equation_substituted[5],
                    equation_substituted[6],
                ),
            ),
            TransformMatchingShapes(
                VGroup(
                    equation_cubic[7].copy(),
                    equation_cubic[8].copy(),
                ),
                VGroup(
                    equation_substituted[7],
                    equation_substituted[8],
                ),
            ),
            run_time=2
        )

        self.wait(2)



class IVF(Scene):
    def construct(self):
        # Create graph
        axes = Axes(
            x_range=[-5, 5],
            y_range=[-5, 5],
            axis_config={"color": BLUE},
        )

        graph = axes.plot(lambda x: x**3 - 4*x + 1, color=WHITE)

        # Create point and line
        point = ValueTracker(-3)
        line = always_redraw(lambda: self.get_line(point, graph, axes))
        projection_area = always_redraw(lambda: self.get_projection_area(point, graph, axes))

        # Animation
        self.play(DrawBorderThenFill(axes), Create(graph))
        self.play(Create(line))
        self.play(Create(projection_area))
        self.play(point.animate.set_value(3), run_time=10, rate_func=linear)
        self.wait()

    def get_line(self, point, graph, axes):
        x = point.get_value()
        result = VGroup()
        line = DashedLine(
            start=axes.c2p(0, graph.underlying_function(x)),
            end=axes.c2p(x, graph.underlying_function(x)),
            stroke_width=4,
            stroke_color=BLUE,
        )
        dot = Dot().set_color(BLUE).move_to(axes.c2p(x, graph.underlying_function(x)))
        result.add(line, dot)
        return result

    def get_projection_area(self, point, graph, axes):
        x = point.get_value()
        y_value = graph.underlying_function(x)
        
        area_start = axes.c2p(0.02, 0)
        area_end = axes.c2p(0.02, y_value)
        area = Polygon(axes.c2p(-0.02, 0), area_start, area_end, axes.c2p(0.02, y_value), fill_color=YELLOW, fill_opacity=0.3, stroke_width=0)
        
        return area

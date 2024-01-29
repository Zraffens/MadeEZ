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
        equation_cubic = MathTex("a", "x^3", "+", "b", "x^2", "+", "c", "x", "+", "d", "=", "0").set_color_by_gradient(BLUE, GREEN)
        equation_cubic.to_edge(UP)

        # Description of substitution
        substitution_desc = MathTex("Let ", " x\\: = ", " y - \\frac{b}{3a}").set_color_by_gradient(BLUE, GREEN)
        substitution_desc.next_to(equation_cubic, DOWN, buff=0.5)

        # Substituted equation (initially hidden)
        equation_substituted = MathTex(
            "a", "\\left(y-\\frac{b}{3a}\\right)^3", "+", "b", "\\left(y-\\frac{b}{3a}\\right)^2", "+",
            "c", "\\left(y-\\frac{b}{3a}\\right)", "+", "d", "=", "0"
        ).set_color_by_gradient(BLUE, GREEN)
        equation_substituted.next_to(substitution_desc, DOWN)
        third_line = MathTex(
            "ay^3", "-", "by^2", "+", "\\frac{b^2}{3a}y", "-", "\\frac{b^3}{27a^2}", "+", "by^2",
            "-", "\\frac{2b^2}{3a}y", "+", "\\frac{b^3}{9a^2}", "+", "cy", "-", "\\frac{bc}{3a}", "+", "d", "=", "0"
        ).set_color_by_gradient(BLUE, GREEN)
        third_line.next_to(equation_substituted, DOWN)
        fourth_line = MathTex(
            "ay^3", "+", "\\left( c-\\frac{b^2}{3a} \\right) y", "+", "\\left( d + \\frac{2b^3}{27a^2}-\\frac{bc}{3a} \\right)", "=", "0"
        ).set_color_by_gradient(BLUE, GREEN)
        fourth_line.next_to(third_line, DOWN)


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
                    equation_cubic[2].copy(),
                    equation_cubic[3].copy(),
                    equation_cubic[5].copy(),
                    equation_cubic[6].copy(),
                    equation_cubic[8].copy(),
                    equation_cubic[9].copy(),
                    equation_cubic[10].copy(),
                    equation_cubic[11].copy(),
                ),
                VGroup(
                    equation_substituted[0],
                    equation_substituted[2],
                    equation_substituted[3],
                    equation_substituted[5],
                    equation_substituted[6],
                    equation_substituted[8],
                    equation_substituted[9],
                    equation_substituted[10],
                    equation_substituted[11],
                ),
            ),
            TransformMatchingShapes(
                VGroup(
                    substitution_desc[2].copy(),
                    substitution_desc[2].copy(),
                    substitution_desc[2].copy(),
                ),
                VGroup(
                    equation_substituted[1],
                    equation_substituted[4],
                    equation_substituted[7],
                ),
            ),
            run_time=1.8
        )
        self.wait(2)
        # equation_substituted = MathTex(
        #     "a", "\\left(y-\\frac{b}{3a}\\right)^3", "+", "b", "\\left(y-\\frac{b}{3a}\\right)^2", "+",
        #     "c", "\\left(y-\\frac{b}{3a}\\right)", "+", "d", "=", "0"
        # ).set_color_by_gradient(BLUE, GREEN)
        # equation_substituted.next_to(substitution_desc, DOWN)
        # third_line = MathTex(
        #     "ay^3", "-", "by^2", "+", "\\frac{b^2}{3a}y", "-", "\\frac{b^3}{27a^2}", "+", "by^2",
        #     "-", "\\frac{2b^2}{3a}y", "+", "\\frac{b^3}{9a^2}", "+", "cy", "-", "\\frac{bc}{3a}", "+", "d", "=", "0"
        # ).set_color_by_gradient(BLUE, GREEN)
        self.play(
            TransformMatchingShapes(
                VGroup(
                    equation_substituted[0].copy(),
                    equation_substituted[1].copy(),
                    equation_substituted[2].copy(),
                    equation_substituted[3].copy(),
                    equation_substituted[4].copy(),
                    equation_substituted[5].copy(),
                    equation_substituted[6].copy(),
                    equation_substituted[7].copy(),
                    equation_substituted[8].copy(),
                    equation_substituted[9].copy(),
                    equation_substituted[10].copy(),
                    equation_substituted[11].copy(),
                ),
                VGroup(
                    third_line[0],
                    third_line[1],
                    third_line[2],
                    third_line[3],
                    third_line[4],
                    third_line[5],
                    third_line[6],
                    third_line[7],
                    third_line[8],
                    third_line[9],
                    third_line[10],
                    third_line[11],
                ),
            ),
            TransformMatchingShapes(
                VGroup(
                    equation_substituted[8].copy(),
                    equation_substituted[9].copy(),
                    equation_substituted[10].copy(),
                    equation_substituted[11].copy(),
                ),
                VGroup(
                    third_line[-1],
                    third_line[-2],
                    third_line[-3],
                    third_line[-4]
                ),
            ),
            Create(third_line[12]),Create(third_line[13]),Create(third_line[14]),
            Create(third_line[15]), Create(third_line[16]),
            run_time=1.8
        )
        self.wait(2)
        self.play(
            TransformMatchingShapes(
                VGroup(
                    third_line[0].copy(),
                    third_line[1].copy(),
                    third_line[2].copy(),
                    third_line[3].copy(),
                    third_line[4].copy(),
                    third_line[5].copy(),
                    third_line[6].copy(),
                    third_line[7].copy(),
                    third_line[8].copy(),
                    third_line[9].copy(),
                    third_line[10].copy(),
                    third_line[11].copy(),
                    third_line[12].copy(),
                    third_line[13].copy(),
                    third_line[14].copy(),
                    third_line[15].copy(),
                    third_line[16].copy(),
                    third_line[17].copy(),
                ),
                VGroup(
                    fourth_line[0],
                    fourth_line[1],
                    fourth_line[2],
                    fourth_line[3],
                    fourth_line[4],
                    fourth_line[5],
                ),
            ),
            TransformMatchingShapes(
                VGroup(
                    third_line[18].copy(),
                ),
                VGroup(
                    fourth_line[6],
                ),
            ),
            run_time=1.8
        )

        self.wait(2)



class IVF(Scene):
    def construct(self):
        # Create graph
        axes = Axes(
            x_range=[-10, 10],
            y_range=[-10, 10],
            axis_config={"color": BLUE},
        )
        label = MathTex(
            "f(x)= x^3 - 4x + 1"
        ).set(width=2.5).next_to(axes, UP, buff=0.2).set_color(RED_C)
        graph = axes.plot(lambda x: x**3 - 4*x + 1, color=WHITE)

        # Create point and line
        point = ValueTracker(-3)
        line = always_redraw(lambda: self.get_line(point, graph, axes))
        projection_area = always_redraw(lambda: self.get_projection_area(point, graph, axes))

        # Animation
        self.play(DrawBorderThenFill(axes), Write(graph), Write(label))
        self.play(Create(line))
        self.play(Create(projection_area))
        self.play(point.animate.set_value(3), run_time=10, rate_func=linear)
        self.wait()

    def get_line(self, point, graph, axes):
        x = point.get_value()
        y = graph.underlying_function(x)
        result = VGroup()
        line = DashedLine(
            start=axes.c2p(0, graph.underlying_function(x)),
            end=axes.c2p(x, graph.underlying_function(x)),
            stroke_width=4,
            stroke_color=BLUE,
        )
        dot = Dot().set_color(BLUE).move_to(axes.c2p(x, graph.underlying_function(x)))
        moving_label = always_redraw(lambda: self.dot_text(point, dot, graph.underlying_function)
        )
        result.add(line, dot, moving_label)
        return result
    
    def dot_text(self, point, dot, func):
        x = point.get_value()
        y = func(x)
        condition = ''
        if y > 0:
            condition = "Slightly Positive" if y <= 4.079 else "Extremely Positive"
        else:
            condition = "Slightly Negative" if y >= -2.079 else "Extremely Negative"
        return MathTex(condition).set(width=2.5).next_to(dot, LEFT, buff=0.2).set_color(RED_C).scale(0.9)


    def get_projection_area(self, point, graph, axes):
        x = point.get_value()
        y_value = graph.underlying_function(x)
        
        area_start = axes.c2p(0.02, 0)
        area_end = axes.c2p(0.02, y_value)
        area = Polygon(axes.c2p(-0.02, 0), area_start, area_end, axes.c2p(0.02, y_value), fill_color=YELLOW, fill_opacity=0.3, stroke_width=0)
        
        return area

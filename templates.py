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


class SimplifyCubic(Scene):
     def construct(self):
        # Given cubic equation
        cubic_equation = MathTex(
            "x", "^3" "+", "px", "+", "q", "=", "0"
        ).set_color_by_gradient(BLUE, GREEN).scale(1.5)
        cubic_equation.to_edge(UP)

        # Expression involving cube roots (initially hidden)
        cube_root_expression = MathTex("x = "
            "\\sqrt[^3]{", "-\\frac{q}{2}", "+", "\\sqrt{", "\\frac{q^2}{4}", "+", "\\frac{p^3}{27}", "}",
            "}", "-", "\\sqrt[^3]{", "-\\frac{q}{2}", "-", "\\sqrt{", "\\frac{q^2}{4}", "+", "\\frac{p^3}{27}", "\}","\}"
        ).set_color_by_gradient(BLUE, GREEN).scale(1.2)
        cube_root_expression.next_to(cubic_equation, DOWN)

        # Display the cubic equation
        self.play(Write(cubic_equation))
        self.wait()

        # Transform cubic equation to cube root expression
        self.play(TransformMatchingShapes(
            VGroup(cubic_equation.copy()[0], cubic_equation.copy()[-2]),
            VGroup(cube_root_expression[0], cube_root_expression[6]),
        ), Write(cube_root_expression[1:]), run_time=2)

        self.wait(2)

        self.play(FadeOut(cubic_equation), FadeOut(cube_root_expression))

class EquationConnection(Scene):
    def construct(self):
        # First equation
        equation_first = MathTex("x^3", "+", "6x", "-", "20", "=", "0").set_color_by_gradient(BLUE, GREEN)
        equation_first.scale(1.5)
        equation_first.to_edge(UP)

        # Second equation
        equation_second = MathTex("p =", "6", ",", "q =", "-20").set_color_by_gradient(BLUE, GREEN)
        equation_second.scale(1.5)
        equation_second.next_to(equation_first, DOWN)

        # Cube root expression
        cube_root_expression = MathTex("x =", "\\sqrt[^3]{", "-\\frac{q}{2}", "+", "\\sqrt{", "\\frac{q^2}{4}", "+", "\\frac{p^3}{27}", "}", "}", "-", "\\sqrt[^3]{", "-\\frac{q}{2}", "-", "\\sqrt{", "\\frac{q^2}{4}", "+", "\\frac{p^3}{27}", "\}", "\}").set_color_by_gradient(BLUE, GREEN).scale(0.8)

        cube_root_expression.next_to(equation_second, DOWN)
        
        substituted_eqn = MathTex("x =", "\\sqrt[^3]{", "-\\frac{(-20)}{2}", "+", "\\sqrt{", "\\frac{(-20)^2}{4}", "+", "\\frac{6^3}{27}", "}", "}", "-", "\\sqrt[^3]{", "-\\frac{(-20)}{2}", "-", "\\sqrt{", "\\frac{(-20)^2}{4}", "+", "\\frac{6^3}{27}", "\}", "\}").set_color_by_gradient(BLUE, GREEN).scale(0.8)
        substituted_eqn.next_to(cube_root_expression, DOWN)
        simplified = MathTex("x = ",
            "\\sqrt[^3]{", "10", "+", "\\sqrt{", "100", "+", "8", "}",
            "}", "-", "\\sqrt[^3]{", "10", "-", "\\sqrt{", "100", "+", "8", "\}", "\}").set_color_by_gradient(BLUE, GREEN)
        simplified.next_to(substituted_eqn, DOWN)
        simplified2 = MathTex("x = ",
            "\\sqrt[^3]{",
                "\\left(",
                    "\\sqrt[^3]{10 + \\sqrt{108}}",
                    "-",
                    "\\sqrt[^3]{10 - \\sqrt{108}}",
                "\\right)^3",
            "}").set_color_by_gradient(BLUE, GREEN)
        simplified2.next_to(simplified, DOWN)
        # Display equations and expressions
        self.play(Write(equation_first))
        self.wait(2)
        self.play(Write(equation_second))
        self.wait(2)
        self.play(Write(cube_root_expression))
        self.wait(2)
        # Transform equations
        self.play(
            TransformMatchingShapes(
                VGroup(
                    equation_second.copy()[1],
                    equation_second.copy()[1],
                    equation_second.copy()[4],
                    equation_second.copy()[4],
                    equation_second.copy()[4],
                    equation_second.copy()[4],
                ),
                VGroup(
                    substituted_eqn[7],
                    substituted_eqn[17],
                    substituted_eqn[2],
                    substituted_eqn[5],
                    substituted_eqn[12],
                    substituted_eqn[15],
                ),
            ),
            TransformMatchingShapes(
                VGroup(
                    cube_root_expression.copy()[:2],
                    cube_root_expression.copy()[3:5],
                    cube_root_expression.copy()[6],
                    cube_root_expression.copy()[8:12],
                    cube_root_expression.copy()[13:15],
                    cube_root_expression.copy()[16:],
                ),
                VGroup(
                    substituted_eqn[:2],
                    substituted_eqn[3:5],
                    substituted_eqn[6],
                    substituted_eqn[8:12],
                    substituted_eqn[13:15],
                    substituted_eqn[16:],
                )
            ),
            run_time=2.7
        )
        self.wait(2)
        self.play(TransformMatchingShapes(
            substituted_eqn.copy(),
            simplified,
            run_time=2
        ))
        self.wait(2)
        self.wait(2)
        self.play(TransformMatchingShapes(
            simplified.copy(),
            simplified2,
            run_time=2
        ))
        self.wait(2)


class IVF(Scene):
    def construct(self):
        # Create graph
        axes = Axes(
            x_range=[-10, 10],
            y_range=[-20, 10],
            axis_config={"color": BLUE},
        )
        label = MathTex(
            "f(x)= x^3 - 4x + 4"
        ).set(width=2.5).next_to(axes, UP, buff=0.2).set_color(RED_C)
        graph = axes.plot(lambda x: x**3 - 4*x + 4, color=WHITE)

        # Create point1 and line
        point1 = ValueTracker(-4)
        point2 = ValueTracker(3)

        line1 = always_redraw(lambda: self.get_line(point1, graph, axes))
        line2 = always_redraw(lambda: self.get_line(point2, graph, axes))

        self.play(DrawBorderThenFill(axes), Write(graph), Write(label))
        self.play(Create(line1), Create(line2))
        self.play(point1.animate.set_value(-2.38), 
            point2.animate.set_value(-2.38), run_time=5, rate_func=linear)
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
        result.add(line, dot)
        return result
    
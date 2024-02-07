from manim import *


def cartesian():
    axes = Axes(
        x_range=[-6, 6],
        y_range=[-6, 6],
        axis_config={"color": BLUE, "include_numbers": True},
        x_length=6,
        y_length=6,
        )
    x, y = axes.get_x_axis(), axes.get_y_axis()
    x.numbers.set_color(BLUE)
    y.numbers.set_color(BLUE)
    return axes

# keep max in the multiple of 4
def polar(divs=12, max=8, size=6):
    polar_plane = PolarPlane(azimuth_units="PI radians", radius_max=max, radius_step=1, azimuth_step=divs, size=size, azimuth_label_font_size=30, radius_config={"font_size": 30}, ).add_coordinates().set_color(BLUE)
    x = polar_plane.get_coordinate_labels()
    x.set_color(BLUE)
    return polar_plane 


def create_polarobj(r, angle, point, axes, label=[], colors=[BLUE, YELLOW], label_dir=UR, origin=ORIGIN):
    point.move_to(origin)
    line = always_redraw(
        lambda: 
    Line(
        start=origin,
        end = point.get_center(),
        stroke_width=4,
        stroke_color=colors[0]
    )
        )
    # self.play(Create(polar_plane), Create(point), Create(line), run_time=2)
    # self.play(point.animate.move_to(axes.coords_to_point(6, 0)))
    # self.wait()
    path = ParametricFunction(lambda t: np.array([r/2 * np.cos(t), r/2 * np.sin(t), 0]), t_range=[0, angle])
    angle_arc = Arc(1, 0, angle, arc_center=origin, color=colors[1], stroke_width=6)
    angle_label = MathTex(label[1], color=colors[1]).scale(0.8).set_color(colors[1])
    angle_label.next_to(angle_arc, RIGHT, buff=0.5)
    # self.play(MoveAlongPath(point, path), Create(angle_arc), Create(angle_label), run_time=3)
    # self.wait()
    pcoords = always_redraw(lambda: MathTex(f"({label[0]}, {label[1]})").set_color(RED).next_to(point, label_dir))
    # self.play(Write(pcoords))
    return {"line":line, "path": path, "angle_arc": angle_arc, "angle_label": angle_label, "pcoords": pcoords, "point": point}


class MultiplyingByNeg(Scene):
    def construct(self):
        text = Tex(
            "What happens when we multiply a polar object by -1"
        ).scale(0.9).set_color_by_gradient(BLUE, GREEN)
        self.play(Write(text), run_time=2)
        self.wait(2)
        self.play(FadeOut(text))
        hero_text = MathTex("-1", "\\cdot", "A\\angle","\\theta", "=", "A'\\angle\\theta'").move_to(ORIGIN).scale(1.5).set_color_by_gradient(BLUE, GREEN)
        self.play(Write(hero_text))
        self.wait()
        self.play(hero_text.animate.to_edge(UP))
        self.wait()
        line2 = MathTex("A'\\angle\\theta'", " + ", "A\\angle", "\\theta", "=", "0").next_to(hero_text, DOWN, buff=0.6).set_color_by_gradient(BLUE, GREEN).scale(1.5)
        line3 = MathTex("A'\\angle\\theta'", "=", "A\\angle", "(", "\\theta", "+", "\\pi", ")").next_to(line2, DOWN, buff=0.6).set_color_by_gradient(BLUE, GREEN).scale(1.5)
        line4 = MathTex("-1", "\\cdot", "A\\angle","\\theta", "=", "A\\angle", "(", "\\theta", "+", "\\pi", ")").next_to(line3, DOWN, buff=0.6).set_color_by_gradient(BLUE, GREEN).scale(1.5)
        hero_text.submobjects[0].set_color(RED_B)
        hero_text.submobjects[-1].set_color(RED_B)
        line2.submobjects[0].set_color(RED_B)
        line3.submobjects[0].set_color(RED_B)
        line3.submobjects[-2].set_color(YELLOW)
        line4.submobjects[-2].set_color(YELLOW)
        line3.submobjects[0].set_color(RED_B)
        self.play(TransformMatchingShapes(
            VGroup(
                hero_text.copy()[2],
                hero_text.copy()[3],
                hero_text.copy()[4],
                hero_text.copy()[5],
            ),
            VGroup(
                line2[2],
                line2[3],
                line2[4],
                line2[0],
            )
        ), Write(line2[1]), Write(line2[5]), run_time=2)
        self.wait(3)
        self.play(TransformMatchingShapes(
            VGroup(
                line2.copy()[4],
                line2.copy()[1],
                line2.copy()[2],
                line2.copy()[0],
                line2.copy()[3],
            ),
            VGroup(
                line3[1],
                line3[5],
                line3[2],
                line3[0],
                line3[4],
            )
        ), Write(line3[3]), Write(line3[6]), Write(line3[-1]), run_time=2)
        self.wait(3)
        self.play(
            TransformMatchingShapes(
                VGroup(
                    hero_text.copy()[:5],
                ),
                VGroup(
                    line4[:5]
                )
            ),
            TransformMatchingShapes(
                VGroup(
                    line3.copy()[5:]   
                ),
                VGroup(
                    line4[5:]
                )
            ), run_time=2)
        self.wait(3)
        self.play(*[FadeOut(hero_text), FadeOut(line2), FadeOut(line3)])
        self.play(line4.animate.scale(1.1).move_to(ORIGIN + UP))
        self.wait(2)
        bcz_text = MathTex("because\\: A\\angle\\theta", "+", "\\:(-1 \\cdot A \\angle \\theta)\\:", "=", "0").next_to(line4, DOWN, buff=0.3).set_color_by_gradient(BLUE, YELLOW)
        and_text = MathTex("and\\: A\\angle\\theta", "+", "\\:\\:A\\angle(\\theta + \\pi)\\:\\:", "=", "0").next_to(bcz_text, DOWN, buff=0.3).set_color_by_gradient(BLUE, YELLOW)
        group = VGroup(bcz_text[2], and_text[2])
        square = SurroundingRectangle(group, color=WHITE, buff=0.3)
        explain = Tex("They do the same thing, so they're the same").scale(0.6).set_color(YELLOW).next_to(square, DOWN)
        self.play(Write(bcz_text))
        self.play(Write(and_text))
        self.wait(4)
        self.play(Create(square), Write(explain), run_time=2)
        self.wait(8)
        self.play(FadeOut(VGroup(
            bcz_text,
            and_text,
            square,
            explain
        )))
        explain2 = MathTex("-1","\\cdot", "A\\angle\\theta", "=", "1\\angle\\pi", "\\cdot", "A\\angle\\theta").scale(1.2).set_color_by_gradient(GREEN, BLUE).next_to(line4, DOWN, buff=1)
        explain2.submobjects[0].set_color(RED)
        explain2.submobjects[-3].set_color(RED)
        arrow_minus_one = ArcBetweenPoints(explain2[0].get_top(), explain2[2].get_top(), angle=-TAU/4).set_color(RED)
        e3 = Tex("Negates").set_color(RED).scale(0.5).next_to(arrow_minus_one, UP)
        arrow_one_pi = ArcBetweenPoints(explain2[4].get_bottom(), explain2[6].get_bottom(), angle=TAU/4).set_color(RED)
        e4 = Tex("Also Negates").set_color(RED).scale(0.5).next_to(arrow_one_pi, DOWN)
        self.play(
            Write(explain2)
        )
        self.wait(4)
        self.play(
            Create(arrow_minus_one),
            Create(arrow_one_pi),
            Write(e3),
            Write(e4)
        )
        self.wait(7)
        last_eqn = MathTex("\\therefore -1 = 1\\angle\\pi").next_to(explain2, DOWN, buff=1.2).set_color_by_gradient(BLUE, GREEN).scale(1.2)
        self.play(Write(last_eqn))
        self.wait(3)
        self.play(*[FadeOut(mobj) for mobj in self.mobjects if mobj != last_eqn])
        self.wait(2)
        self.play(last_eqn.animate.move_to(ORIGIN).scale(3))
        self.wait(3)


class IntroScene(Scene):
    def construct(self):
        # Create text with color gradient
        text = Tex(
            "Polar Coordinates: Why They're Useful in Explaining Complex Numbers"
        ).scale(0.8).set_color_by_gradient(BLUE, GREEN)
        self.play(Write(text), run_time=2)
        self.wait(5)


class CartesianToPolar(Scene):
    def construct(self):
        # Create cartesian coordinate system
        axes = cartesian()

        # Create arbitrary point in cartesian coordinates
        dot = Dot().move_to(axes.coords_to_point(3, 4))
        label = MathTex("(x, y)").next_to(dot, UR)

        # Show cartesian coordinate system
        self.play(Create(axes), run_time=3.5)
        self.play(Create(dot), Write(label), run_time=1.5)
        self.wait()

        # Transform to polar coordinate system
        polar_plane = polar(size=8)
        polar_label = MathTex("(r, \\theta)").next_to(dot, UR)
        self.play(FadeOut(axes), run_time=1.5)
        self.play(Create(polar_plane), TransformMatchingShapes(label, polar_label), run_time=3.5)
        self.wait(1)
        self.play(FadeOut(VGroup(polar_plane, polar_label)))


class Navigation(Scene):
    def construct(self):
        axes = cartesian()

        # Draw axes
        self.play(Create(axes))

        # Create and move point
        point = Dot().move_to(axes.coords_to_point(0, 0)).set_color(RED_C)
        self.play(Create(point))
        self.wait()
        self.play(point.animate.move_to(axes.coords_to_point(3, 0)))
        self.wait()
        self.play(point.animate.move_to(axes.coords_to_point(3, 2)))

        # Show coordinates
        coords = MathTex("(3, 2)").next_to(point, UR).set_color(YELLOW)
        self.play(Write(coords))

        self.wait(3)

        self.play(FadeOut(VGroup(axes, point, coords)))
        point.move_to(axes.coords_to_point(0, 0))
        polar_plane = polar()
        self.wait(1)
        pobjects = create_polarobj(6, PI/3, point, axes, label=["8", "\\frac{\\pi}{3}"])
        self.play(Create(polar_plane), Create(point), Create(pobjects["line"]), run_time=2)
        self.play(point.animate.move_to(axes.coords_to_point(6, 0)))
        self.wait()
        self.play(MoveAlongPath(point, pobjects["path"]), Create(pobjects["angle_arc"]), Create(pobjects["angle_label"]), run_time=3)
        self.wait()
        self.play(Write(pobjects["pcoords"].next_to(point, UR)))
        self.wait(1)

        self.play(Uncreate(VGroup(polar_plane, *pobjects.values())))
        

class Operations(Scene):
    def construct(self):
        axes = cartesian()
        polar_plane = polar(divs=8, max=2)
        self.play(Create(polar_plane))
        obj1, obj2 = self.create_polar(r=4, angle=PI/8, axes=axes, label=["A", "\\angle\\theta"], colors=[GREEN, YELLOW]), self.create_polar(r=3, angle=2*PI/3, axes=axes, label=["B", "\\angle\\phi"], colors=[BLUE_D, RED_C], label_dir=UR)
        self.add_objects(obj1, obj2, axes)
        next_text = Tex("What about multiplication?").move_to(ORIGIN).scale(1.2).set_color_by_gradient(BLUE, GREEN)
        self.play(Create(next_text), run_time=2)
        self.wait(6)
        self.multiply()


    def create_polar(self, r, angle, axes, label, colors=[BLUE, YELLOW], label_dir=UR):
        point = Dot().move_to(axes.coords_to_point(0, 0)).set_color(colors[0])
        pobjects = create_polarobj(r=r, angle=angle, point=point, axes=axes, label=label, colors=colors)
        pobjects["point"] = point
        self.play(Create(point), Create(pobjects["line"]), run_time=2)
        self.play(point.animate.move_to(axes.coords_to_point(r, 0)))
        # self.wait()
        self.play(MoveAlongPath(point, pobjects["path"]), run_time=2)
        self.wait()
        self.play(Write(pobjects["pcoords"].next_to(point, label_dir)))
        self.wait(1)
        return pobjects
    
    def add_objects(self, obj1, obj2, axes):
        point1, point2 = obj1["point"], obj2["point"]
        line2 = obj2["line"]
        dest = (2*(point1.get_center()[0] + point2.get_center()[0]), 2*(point1.get_center()[1] + point2.get_center()[1]))
        self.remove_updater(line2)
        self.play(point2.animate.move_to(axes.coords_to_point(*dest)), line2.animate.put_start_and_end_on(point1.get_center(), axes.coords_to_point(*dest)), run_time=2)
        dupline = Line(
            start=point1.get_center(),
            end = axes.c2p(*dest),
            stroke_width=4,
            stroke_color=BLUE_D
        )
        self.add(dupline)
        self.remove(line2)
        self.wait(2)
        obj3 = self.create_polar(r=np.sqrt(dest[0]**2+dest[1]**2), angle=np.arctan(dest[1]/dest[0]), axes=axes, label=["A+B", "\\angle\\theta"], colors=[DARK_BROWN, GRAY], label_dir=UL)
        self.remove(obj3["pcoords"])
        self.add(MathTex(f"(A+B, \\angle \\alpha)").set_color(RED).next_to(obj3["point"], UL))
        self.wait(5)
        self.play(*[FadeOut(mob) for mob in self.mobjects])


    def multiply(self):
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        text1 = MathTex("Apply\\:", "B\\angle\\phi\\: to\\: A\\angle\\theta").set_color_by_gradient(BLUE, GREEN).to_edge(UP)
        text2 = MathTex("Scale\\:", "A\\angle\\theta\\: by\\: B").set_color_by_gradient(BLUE, GREEN).next_to(text1, DOWN*9+LEFT)
        text3 = MathTex("Multiply\\:", "magnitude\\: by\\: B" ).set_color_by_gradient(BLUE, GREEN).next_to(text2, DOWN*7)
        
        text4 = MathTex("Rotate\\:", "A\\angle\\theta\\: by\\: \\phi").set_color_by_gradient(BLUE, GREEN).next_to(text1, DOWN*9+RIGHT)
        text5 = MathTex("Add\\:", "\\phi\\: to\\: phase" ).set_color_by_gradient(BLUE, GREEN).next_to(text4, DOWN*7)
        text6 = MathTex(
            r"\therefore", r"B", r"\angle", r"\phi", r"\cdot A\angle\theta",r" = ", r"B", r"A\angle(\theta +", r"\phi",r")"
        ).to_edge(DOWN).set_color_by_gradient(BLUE, GREEN)

        text7 = MathTex(
            r"\therefore", r"1", r"\angle", r"\phi", r"\cdot A\angle\theta",r" = ", r"1", r"A\angle(\theta +", r"\phi",r")"
        ).to_edge(DOWN).set_color_by_gradient(BLUE, GREEN).move_to(ORIGIN).scale(1.5)
        text7.submobjects[1].set_color(RED_B)
        text7.submobjects[-4].set_color(RED_B)
        text8 = MathTex(r"\therefore", r"1", r"\angle\phi \cdot A\angle\theta",r" = ", r"1", r"A\angle(\theta +", r"\phi",r")").set_color_by_gradient(BLUE, GREEN).scale(1.5).next_to(text7, DOWN)
        text8.submobjects[0].set_color(BLACK)
        text8.submobjects[1].set_color(BLACK)
        text8.submobjects[2].set_color(BLACK)
        text8.submobjects[4].set_color(BLACK)
        text1.submobjects[0].set_color(RED)
        text2.submobjects[0].set_color(RED)
        text3.submobjects[0].set_color(RED)
        text4.submobjects[0].set_color(RED)
        text5.submobjects[0].set_color(RED)
        
        arrow1 = Arrow(text1.get_bottom(), text2.get_top(), buff=0.4)
        arrow2 = Arrow(text1.get_bottom(), text4.get_top(), buff=0.4)
        arrow3 = Arrow(text2.get_bottom(), text3.get_top(), buff=0.2)
        arrow4 = Arrow(text4.get_bottom(), text5.get_top(), buff=0.2)
        self.play(Write(text1))
        self.wait(3.5)
        self.play(GrowArrow(arrow1))
        self.play(Write(text2))
        self.wait(3.5)
        self.play(GrowArrow(arrow3))
        self.play(Write(text3))
        self.wait(3.5)
        self.play(GrowArrow(arrow2))
        self.play(Write(text4))
        self.wait(3.5)
        self.play(GrowArrow(arrow4))
        self.play(Write(text5))
        self.wait(3.5)
        self.play(Write(text6))
        self.wait(3.5)
        self.play(*[FadeOut(mob) for mob in self.mobjects if mob != text6])
        self.wait()
        self.play(text6.animate.move_to(ORIGIN).scale(1.5))
        text6.save_state()
        self.wait(3.5)
        self.play(Transform(
            text6, text7
        ))

        self.play(Write(text8))
        self.wait(4)
        self.play(Uncreate(text8))
        self.wait(2)
        self.play(Restore(text6))
        self.remove(text7)
        self.wait(3)
        text9 = MathTex(
            r"\therefore", r"B", r"\angle", r"0", r"\cdot A\angle\theta",r" = ", r"B", r"A\angle(\theta +",r"0", r")"
        ).set_color_by_gradient(BLUE, GREEN).scale(1.5).move_to(ORIGIN)
        text10 = MathTex(r"\therefore", r"B", r"\angle", r"0", r"\cdot A\angle\theta",r" =\;\;\;\,", r"B\cdot", r"A\angle(\theta",r"", r")").next_to(text9, DOWN).scale(1.5).set_color_by_gradient(BLUE, GREEN)
        text10[0].set_color(BLACK)
        text10[1].set_color(BLACK)
        text10[2].set_color(BLACK)
        text10[3].set_color(BLACK)
        text10[4].set_color(BLACK)
        text9.get_part_by_tex("0")[0].set_color(RED_B)
        text9.submobjects[-2].set_color(RED_B)
        self.play(Transform(text6, text9))
        # self.remove(text6)
        self.wait(3)
        self.play(Write(text10))


class Exponentiation(Scene):
    def construct(self):
        axes = cartesian()
        polar_plane = polar(divs=8, max=1)
        point = Dot().move_to(axes.coords_to_point(0, 0)).set_color(YELLOW)
        pobjects = create_polarobj(r=6, angle=PI/6, point=point, axes=axes, label=["1", "\\angle\\phi"], colors=[YELLOW, GREEN])
        pobjects["point"] = point
        self.play(Create(polar_plane))
        self.play(Create(point), Create(pobjects["line"]), run_time=2)
        self.play(point.animate.move_to(axes.coords_to_point(6, 0)))
        # self.wait()
        
        path = ParametricFunction(lambda t: np.array([3 * np.cos(t), 3 * np.sin(t), 0]), t_range=[0, PI/6])
        self.play(MoveAlongPath(point, path), run_time=2)
        self.wait()
        self.play(Write(pobjects["pcoords"].next_to(point, UR)))
        self.wait(3)
        self.play(VGroup(polar_plane, point, pobjects["line"], pobjects["pcoords"]).animate.scale(0.7).to_edge(DOWN), run_time=2)
        axes.scale(0.7).to_edge(DR)
        dupline = Line(
            start=polar_plane.polar_to_point(0, 0),
            end = point.get_center(),
            stroke_width=4,
            stroke_color=YELLOW
        )
        self.add(dupline)
        self.remove(pobjects["line"])
        duplabel = MathTex("(1, \\angle\\phi)").set_color(RED).scale(0.7).next_to(point, UR)
        self.add(duplabel)
        self.remove(pobjects["pcoords"])

        expeqn = MathTex("(", "1\\angle\\phi", ")", "^n", " = ", "1\\angle\\phi", " \\cdot", "1\\angle\\phi", "\\dots", " \\cdot","1\\angle\\phi").to_edge(UP).set_color_by_gradient(BLUE, GREEN)
        brace = Brace(expeqn[5:], direction=DOWN, buff=SMALL_BUFF)
        b_label = Tex("n repeated multiplications").scale(0.7)
        b_label.next_to(brace, DOWN)
        b_label1 = Tex(" = n transformations").scale(0.7).next_to(b_label, DOWN)
        self.play(Write(expeqn[:5]))
        self.wait()
        self.play(TransformMatchingShapes(
            VGroup(
                expeqn.copy()[1],
                expeqn.copy()[1],
                expeqn.copy()[1],
            ),
            VGroup(
                expeqn[5],
                expeqn[7],
                expeqn[10]
            )
        ), Write(VGroup(expeqn[6], expeqn[8], expeqn[9])), run_time=2)
        self.wait()
        self.play(Create(brace), run_time=1.5)
        self.play(Write(b_label))
        self.play(Write(b_label1))
        angles = [PI/6, PI/3, 3*PI/6, 4*PI/6, 5*PI/6, 6*PI/6]
        lines = [Line(start=polar_plane.polar_to_point(0, 0), end=polar_plane.polar_to_point(1.1, angle)) for angle in angles]
        self.play(
            *[Create(line) for line in lines]
        )
        self.wait(5)
        self.play(*[Uncreate(line) for line in lines])
        point2 = Dot().move_to(polar_plane.polar_to_point(0, 0.1)).set_color(YELLOW)
        pobjects1 = create_polarobj(r=6, angle=PI/6, point=point2, axes=axes, label=["1^6", "6\\cdot\\phi"], colors=[YELLOW, GREEN], label_dir=UL, origin=polar_plane.polar_to_point(0, 0))
        # pobjects1["point"] = point2
        new_line2 = MathTex("(", "1\\angle\\phi", ")", "^n", " = ", "1\\angle n\\phi").next_to(expeqn, DOWN).set_color_by_gradient(BLUE, GREEN)
        for i in range(4):
            new_line2.submobjects[i].set_color(BLACK)
        self.play(Create(point2), Create(pobjects1["line"]), run_time=1)
        self.play(point2.animate.move_to(polar_plane.polar_to_point(1, 0)))
        # self.wait()
        path = ParametricFunction(lambda t: np.array(polar_plane.polar_to_point(1, t)), t_range=[0, angles[-1]])
        self.play(MoveAlongPath(point2, path), run_time=2)
        self.wait()
        self.play(Write(pobjects1["pcoords"].next_to(point2, UR)), Uncreate(VGroup(brace, b_label1, b_label)), run_time=1.2)
        self.play(Write(new_line2))
        self.wait(3)
        



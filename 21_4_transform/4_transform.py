from manim import *

class CombinedScene(Scene):
    def construct(self):
        # Inicio
        self.camera.background_color = "#20958a"  # Establecer el fondo a blanco
        text = Text("GRAFICACICON COMPUTACIONAL \nActividad: 4_Transform \nPRESENTO: JESUS ENRIQUE LUGO RAMIREZ ")
        self.play(FadeIn(text))
        self.wait(3)
        self.play(FadeOut(text))

        # TransformationText1V1
        self.camera.background_color = PURPLE
        texto1 = Text("First text")
        texto2 = Text("Second text")
        self.play(FadeIn(texto1))
        self.wait()
        self.play(Transform(texto1, texto2))
        self.wait()
        self.play(FadeOut(texto1))

        # TransformationText1V2
        self.camera.background_color = BLUE
        texto1 = Text("First text").to_edge(UP)
        texto2 = Text("Second text")
        self.play(FadeIn(texto1))
        self.wait()
        self.play(Transform(texto1, texto2))
        self.wait()
        self.play(FadeOut(texto1))

        # TransformationText2
        self.camera.background_color = GREEN
        text1 = Text("Function")
        text2 = Text("Derivative")
        text3 = Text("Integral")
        text4 = Text("Transformation")
        self.play(FadeIn(text1))
        self.wait()
        self.play(ReplacementTransform(text1, text2))
        self.wait()
        self.play(ReplacementTransform(text2, text3))
        self.wait()
        self.play(ReplacementTransform(text3, text4))
        self.wait()
        self.play(FadeOut(text4))

        # CopyTextV1
        self.camera.background_color = BLUE
        formula = MathTex(
            "\\frac{d}{dx}", "(", "u", "+", "v", ")", "=", 
            "\\frac{d}{dx}", "u", "+", "\\frac{d}{dx}", "v"
        ).scale(2)
        self.play(FadeIn(formula[:7]))
        self.wait()
        self.play(
            ReplacementTransform(formula[2].copy(), formula[8]),
            ReplacementTransform(formula[4].copy(), formula[11]),
            ReplacementTransform(formula[3].copy(), formula[9])
        )
        self.wait()
        self.play(
            ReplacementTransform(formula[0].copy(), formula[7]),
            ReplacementTransform(formula[0].copy(), formula[10])
        )
        self.wait()
        self.play(FadeOut(formula))

        # CopyTextV2
        self.camera.background_color = BLACK
        self.play(FadeIn(formula[:7]))
        self.wait()
        self.play(
            ReplacementTransform(formula[2].copy(), formula[8]),
            ReplacementTransform(formula[4].copy(), formula[11]),
            ReplacementTransform(formula[3].copy(), formula[9]),
            run_time=3
        )
        self.wait()
        self.play(
            ReplacementTransform(formula[0].copy(), formula[7]),
            ReplacementTransform(formula[0].copy(), formula[10]),
            run_time=3
        )
        self.wait()
        self.play(FadeOut(formula))

        # CopyTextV3
        formula[8].set_color(PINK)
        formula[11].set_color(BLUE)
        self.camera.background_color = GREEN
        self.play(FadeIn(formula[:7]))
        self.wait()
        self.play(
            ReplacementTransform(formula[2].copy(), formula[8]),
            ReplacementTransform(formula[4].copy(), formula[11]),
            ReplacementTransform(formula[3].copy(), formula[9]),
            run_time=3
        )
        self.wait()
        self.play(
            ReplacementTransform(formula[0].copy(), formula[7]),
            ReplacementTransform(formula[0].copy(), formula[10]),
            run_time=3
        )
        self.wait()
        self.play(FadeOut(formula))

        # ChangeTextColorAnimation
        self.camera.background_color = RED
        text = Text("Text").scale(3)
        self.play(FadeIn(text))
        self.wait()
        self.play(text.animate.set_color(YELLOW), run_time=2)
        self.wait()
        self.play(FadeOut(text))

        # ChangeSizeAnimation
        self.camera.background_color = PINK
        text = Text("Text").scale(2)
        self.play(FadeIn(text))
        self.wait()
        self.play(text.animate.scale(1.5), run_time=2)
        self.wait()
        self.play(FadeOut(text))

        # MoveText
        self.camera.background_color = ORANGE
        text = Text("Text").scale(2).shift(LEFT * 2)
        self.play(FadeIn(text))
        self.wait()
        self.play(text.animate.shift(RIGHT * 2), run_time=2, path_arc=0)
        self.wait()
        self.play(FadeOut(text))

        # ChangeColorAndSizeAnimation
        self.camera.background_color = WHITE
        text = Text("Text").scale(2).shift(LEFT * 2)
        self.play(FadeIn(text))
        self.wait()
        self.play(
            text.animate.shift(RIGHT * 2).scale(2).set_color(RED),
            run_time=2
        )
        self.wait()
        self.play(FadeOut(text))

        # Fin
        self.camera.background_color = BLACK
        text = Text("Graficación Computacional 2024B")
        self.play(FadeIn(text))
        self.play(text.animate.set_color(GREEN), run_time=2)
        self.wait(3)
        self.play(FadeOut(text))


        # TextLike1DArrays
        text1 = Text("Te")
        text2 = Text("xt")
        text2.next_to(text1, RIGHT)
        self.play(FadeIn(text1))
        self.wait(0.5)
        self.play(FadeOut(text1))
        self.play(FadeIn(text2))
        self.wait(0.5)
        self.play(FadeOut(text2))

        # TextLike2DArraysV1
        text = [
            [Text("T"), Text("e")],
            [Text("x"), Text("t")]
        ]
        text[0][0].shift(LEFT + UP)
        text[0][1].next_to(text[0][0], RIGHT)
        text[1][0].next_to(text[0][0], DOWN)
        text[1][1].next_to(text[1][0], RIGHT)
        for row in text:
            for char in row:
                self.play(FadeIn(char))
        self.wait()
        self.play(*[FadeOut(char) for row in text for char in row])

        # TextLike2DArraysV2
        text1 = Text("Te")
        text2 = Text("xt")
        text2.next_to(text1, RIGHT, buff=0.2)
        for char in text1:
            self.play(FadeIn(char))
        for char in text2:
            self.play(FadeIn(char))
        self.wait()
        self.play(FadeOut(text1), FadeOut(text2))

        # TextLike2DArraysV3
        text = [Text("Te"), Text("xt")]
        text[1].next_to(text[0], RIGHT, buff=0.2)
        for part in text:
            for char in part:
                self.play(FadeIn(char))
        self.wait()
        self.play(*[FadeOut(part) for part in text])

        # TransformIssues
        text_1 = VGroup(Text("A"), Text("B"), Text("C"))
        text_2 = Text("B")
        text_1.arrange(RIGHT, buff=0.5)
        text_2.next_to(text_1, UP, buff=1)
        self.play(
            *[
                FadeIn(text_1[i])
                for i in [0, 2]
            ],
            FadeIn(text_2)
        )
        self.wait()
        self.play(
            ReplacementTransform(text_2, text_1[1])
        )
        self.wait()
        self.play(FadeOut(text_1))

        # TransformVGroup
        text_n = Text("A")
        text_v = VGroup(Text("A")).next_to(text_n, DOWN)
        self.play(FadeIn(text_n))
        self.wait()
        self.play(ReplacementTransform(text_n, text_v[0]))
        self.wait()
        self.play(FadeOut(text_v))

        # TransformIssuesSolution1
        text_1 = Text("ABC")
        text_2 = Text("B")
        text_2.next_to(text_1, UP, buff=1)
        self.play(
            *[
                FadeIn(text_1[i])
                for i in [0, 2]
            ],
            FadeIn(text_2)
        )
        self.wait()
        self.play(
            ReplacementTransform(text_2, text_1[1])
        )
        self.wait()
        self.play(FadeOut(text_1))

        # TransformIssuesSolutionInfallible
        text_1 = Text("ABC")
        text_2 = Text("B")
        text_2.next_to(text_1, UP, buff=1)
        text_1_1_c = Text("B") \
            .match_style(text_1[1]) \
            .match_width(text_1[1]) \
            .move_to(text_1[1])
        self.play(
            *[
                FadeIn(text_1[i])
                for i in [0, 2]
            ],
            FadeIn(text_2)
        )
        self.wait()
        self.play(
            ReplacementTransform(text_2, text_1_1_c)
        )
        self.remove(text_1_1_c)
        self.add(text_1[1])
        self.wait()
        self.play(FadeOut(text_1))


"""
CombinedScene

manim -pql 4_transform.py CombinedScene 

Buen trabajo Lugo
Atte. Profa. Hazem AR
"""

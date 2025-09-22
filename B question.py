from manim import *

class TeacherStudentsScene(Scene):
    def construct(self):
        self.camera.background_color = DARK_GRAY 
        # t1 = SVGMobject("assets/PiCreatures/PiCreatures_wave_1.svg")
        t1 = SVGMobject("assets/PiCreatures/PiCreatures_jamming.svg")
        t3 = SVGMobject("assets/PiCreatures/PiCreatures_tease.svg")
        t4 = SVGMobject("assets/PiCreatures/PiCreatures_well.svg")
        teacher = VGroup(t1,t3,t4).scale(2).to_edge(DR, buff=0.2).flip(UP)
        for t in teacher:
            t[4].set_fill(GREY_BROWN, opacity=1)

        s1A = SVGMobject("assets/PiCreatures/PiCreatures_horrified.svg").scale(1.5)
        s2A = SVGMobject("assets/PiCreatures/PiCreatures_maybe.svg").scale(1.5)
        s3A = SVGMobject("assets/PiCreatures/PiCreatures_pleading.svg").scale(1.5)

        s1B = SVGMobject("assets/PiCreatures/PiCreatures_thinking.svg").scale(1.5)
        s2B = SVGMobject("assets/PiCreatures/PiCreatures_confused.svg").scale(1.5)
        s3B = SVGMobject("assets/PiCreatures/PiCreatures_pondering.svg").scale(1.5)

        s2A[4].set_fill(DARK_BLUE, opacity=1)
        s2B[4].set_fill(DARK_BLUE, opacity=1)
        students = VGroup(s1A, s2A, s3A, s1B, s2B, s3B)

        s1A.flip(UP)
        sNA = VGroup(s1A, s2A, s3A)
        sNB = VGroup(s1B, s2B, s3B)
        sNA.arrange(LEFT, buff=0.3).to_edge(DL, buff=0.3)
        sNB.arrange(LEFT, buff=0.7).to_edge(DL, buff=0.3)

        # da watchers
        self.add(t1, sNA)
        self.wait(1)

        que = Tex(r"Can you draw an ellipse using\\only a compass and a ruler?").to_edge(UL)
        que.shift(DOWN)

        ans1 = Tex("Well, no.").to_edge(UR)
        ans1.shift(0.7*DOWN)
        
        ans2 = Tex("But almost.").to_edge(UR)
        ans2.shift(1.5*DOWN)


        # transition emotion of s3A, make others look + question
        s1A.flip(DOWN)
        self.play(
            Write(que),
            ReplacementTransform(sNA, sNB),
            )
        self.wait(1)

        self.play(
            Write(ans1),
            ReplacementTransform(t1, t3)
        )
        self.wait(1)
        self.play(
            Write(ans2),
            ReplacementTransform(t3, t4)
        )
        self.wait(1)
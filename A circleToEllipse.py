from manim import *
import numpy as np

class CircleToEllipse(Scene):
    def construct(self):
        self.add(NumberPlane(background_line_style = {"stroke_color": TEAL, "stroke_width": 0.5, "stroke_opacity": 0.3}))
        # Center point and label
        center = Dot(ORIGIN)
        label_c = Tex("C").next_to(center, DR, buff=0.02)

        # Draw center and label
        self.play(FadeIn(center), Write(label_c))
        self.wait(0.5)

        # Define radius, label
        radius = Line(ORIGIN, RIGHT*2, color=BLUE)
        label_r = Tex("r").next_to(radius, UP)

        # fakers
        fake_radius = Line(ORIGIN, RIGHT*2, color=BLUE)
        fake_tracingDot = Dot(RIGHT*2)
        fake_dyn_radial = Line(ORIGIN, RIGHT*3, color=BLUE)
        fake_radial_dot = Dot(RIGHT*3)

        # Draw radius, tracing dot
        self.play(Create(radius), Write(label_r))
        self.remove(center)
        self.add(center)
       
        # Tracing a circle w/compass
        tracingDot = Dot(point=radius.get_end())
        tracedCircle = TracedPath(tracingDot.get_center)    
        circle = Circle(color=WHITE, fill_opacity=0, radius=2, stroke_width=2)

        # Draw traced stuff
        self.add(tracedCircle, tracingDot)
        self.wait(1)

        self.play(
            Unwrite(label_r, run_time=0.1),
            Rotate(radius, angle=TAU, about_point=ORIGIN, run_time=4),
            Rotate(tracingDot, angle=TAU, about_point=ORIGIN, run_time=4),
        )
        self.remove(tracedCircle, tracingDot, radius)
        self.add(fake_tracingDot, fake_radius, circle)
        self.wait(0.4)

        # Transition into ellipse
        a, b = 3, 2  # ellipse parameters
        ellipse = ParametricFunction(
            lambda t: np.array([a * np.cos(t), b * np.sin(t), 0]),
            t_range=[0, TAU],
            color=WHITE
        )

        theta = ValueTracker(0)

        # Dynamic line along ellipse
        dyn_radial = always_redraw(
            lambda: Line(
                ORIGIN,
                np.array([a * np.cos(theta.get_value()), b * np.sin(theta.get_value()), 0]),
                color=BLUE
            )
        )

        # Dynamic dot
        radial_dot = always_redraw(
            lambda: Dot(point=dyn_radial.get_end())
        )

        def radius_length():
            x = a * np.cos(theta.get_value())
            y = b * np.sin(theta.get_value())
            return np.sqrt(x**2 + y**2)

        # Live-updating label r = f(x)
        func_label = always_redraw(
            lambda: MathTex(f"r = {radius_length():.2f}").to_corner(UR)
        )
 
        self.play(
            Transform(circle, ellipse),
            Transform(fake_tracingDot, fake_radial_dot),
            Transform(fake_radius, fake_dyn_radial),
            FadeIn(func_label),
            run_time=2
        )
        self.remove(fake_tracingDot, fake_radial_dot, fake_radius, fake_dyn_radial, center)
        self.add(dyn_radial, radial_dot, center)

        # Animate theta along ellipse
        self.play(theta.animate.set_value(2*TAU), run_time=12, rate_func=linear)
        self.wait() 
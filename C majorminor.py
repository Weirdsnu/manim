from manim import *
import numpy as np

class SquareCircleWithMidpoints(Scene):
    def construct(self):
        # Create a square
        square = Square(side_length=4)
        circle = Circle(radius=2, fill_opacity=0, color=WHITE).move_to(square.get_center())

        mask = Circle(radius=1.95, color=BLACK, fill_color=BLACK, fill_opacity=1)
        mask.move_to(circle.get_center())
        diag1 = Polygon([-3,-3,0],[3,3,0],[3,-3,0],[-3,3,0]).rotate(PI/4)  # one diagonal
        diag2 = Polygon([-3,-3,0],[3,3,0],[3,-3,0],[-3,3,0]).rotate(3*PI/4)
        blue_part = Intersection(circle, diag1, fill_opacity=0, color=BLUE, stroke_width=4)
        # Red in bottom-right & top-left
        red_part  = Intersection(circle, diag2, fill_opacity=0, color=RED, stroke_width=4)
        rbcircle = VGroup(mask, blue_part, red_part, mask)
        rbcs = VGroup(rbcircle, square)

        self.play(Create(circle))
        self.wait(0.8)
        self.play(Create(square))
        self.wait(1)
        # 1st and 3rd quadrant blue, else red
        self.remove(circle)
        self.play(Create(rbcircle))
        self.wait(1)


        # Rotate about the center by 45 degrees
        self.play(Rotate(rbcs, angle=PI/4, about_point=ORIGIN), run_time=2)
        self.wait(0.8)

        # Stretch both square and circle horizontally
        self.play(rbcs.animate.stretch(1.5, dim=0), run_time=3)
        self.wait(1)


        vertices = square.get_vertices()
        midpoints = [
        (vertices[0] + vertices[1]) / 2,  # Left side
        (vertices[1] + vertices[2]) / 2,  # Top side
        (vertices[2] + vertices[3]) / 2,  # Right side
        (vertices[3] + vertices[0]) / 2,  # Bottom side
        ]
        # draw dots
        sqMdPt = VGroup(*[Dot(point=mp, color=RED) for mp in midpoints])
        # Connect opposite midpoints, dashed lines
        bisectors = VGroup()
        for i in range(len(midpoints)):
            start = midpoints[i]
            end = midpoints[(i + 2) % len(midpoints)]
            bisector_line = Line(start, end, color=YELLOW_D)
            dashed_bisector = DashedVMobject(bisector_line, num_dashes=20, dashed_ratio=0.6)
            bisectors.add(dashed_bisector)

        self.play(Create(sqMdPt))
        self.wait(0.5)

        self.play(Create(bisectors))
        self.wait(0.5)
        
        self.remove(bisectors, sqMdPt, square)
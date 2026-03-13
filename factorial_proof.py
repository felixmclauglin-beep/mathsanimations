from manim import *

class FactorialProof(Scene):
    def construct(self):

        BRtitle = Text('1/10', font_size = 10)
        BRtitle.to_corner(DR, buff = 0.1)
        self.play(Write(BRtitle))
        
        title = Text('Proof that 0! = 1', font_size = 60)
        self.play(Write(title))
        self.wait(.2)
        self.play(Circumscribe(title), color = BLUE)
        self.wait()

        self.play(FadeOut(title))
        self.wait()

        intro_text = Text('The factorial of a positive integer\n is the product of it\n and all the integers below it.', font_size = 35)
        self.play(Write(intro_text), buff = 2)
        self.wait(3)
        self.play(FadeOut(intro_text))
        self.wait()
        
        forexample = Text('For example,', font_size = 40)
        forexample.to_edge(UP, buff = .5)
        self.play(Write(forexample))
        self.wait()

        factorialeg =  MathTex('5! = 5 \\times 4 \\times 3 \\times 2 \\times 1', font_size = 40)
        self.play(Write(factorialeg))
        self.wait()
        self.play(FadeOut(forexample))
        self.play(factorialeg.animate.to_edge(UP))
        self.wait()

        subexpl = Text('Letting n = 5,\n so 4 = (n-1),\n 3 = (n-2), and so on:', font_size = 20, color = YELLOW)
        subexpl.to_corner(UL, buff = 1.5)
        self.play(Write(subexpl))
        self.wait(4)

        nfactorial = MathTex('n! = n \\times (n-1)!', font_size = 40)
        self.play(Write(nfactorial))
        self.wait(2)

        self.play(FadeOut(subexpl), FadeOut(factorialeg))
        self.wait()

        self.play(nfactorial.animate.to_edge(UP), buff = 1)
        self.wait()

       #Introduce the substitution of n = 1
        sub1 = Text('Let: n = 1', font_size = 30)
        self.play(Write(sub1))
        self.wait(2)
        self.play(sub1.animate.to_edge(UP, buff = 1.5))
        self.wait()

        #Subbing in n = 1 then simplifying expression
        subline1 = MathTex(
            '1!', '=', '1', r'\times', '(1-1)', '!',
              font_size = 40)
        
        self.play(Write(subline1))
        self.wait()
       
        #nfactorial and sub1 fade out
        self.play(FadeOut(nfactorial), FadeOut(sub1))
        self.wait()
       
        #Highlight the bracket to be simplified
        self.play(subline1[4].animate.set_color(RED))
        self.wait()
    
    
        #Text to show the simplification of the bracket, with a bulb / star to show an idea
        expltext = Text('Since (1-1) = 0,\n we can write:', font_size = 25, color = GREEN)
        expltext.to_edge(UP, buff = 1)
        #Circle and triangle to show an idea
        idea_circle = Circle(
            radius = 0.28,
            color = YELLOW)
        idea_circle.set_fill(YELLOW, opacity = 0.4)
        idea_circle.next_to(expltext, LEFT, buff = 0.1)
        star = RegularPolygon(n=8, color = ORANGE, fill_opacity = 0.5)
        star.scale(0.37)
        star.move_to(idea_circle.get_center())
        self.wait()
        self.play(Write(expltext), Create(idea_circle), Create(star))
        #Make the star in the circle spin
        self.play(Rotate(star, angle=TAU*2, about_point = star.get_center()), run_time = 3.5, rate_func = linear)
        self.wait(3.5)
        self.play(FadeOut(expltext), FadeOut(idea_circle), FadeOut(star))
        self.wait(.5)

        #Arrow in the centre, move subline1 to the left of the arrow, create arrow
        arrow = Arrow(start = ORIGIN, end = RIGHT*2, buff = 0.1, color = BLUE)
        arrow.move_to(ORIGIN)
        self.play(subline1.animate.next_to(arrow, LEFT, buff = 0.5))
        self.wait(.3)
        self.play(Create(arrow))
        self.wait(.4)

        #Make the second line, showing the simplification from (1-1)! to 0!
        subline2 = MathTex("1!", "=", "1", r"\times", "0!", font_size=40)
        subline2.next_to(arrow, RIGHT, buff=0.5)
        self.play(Write(subline2))
        self.wait(2)
        

        #Arrow and subline1 disappear, subline 2 moves to the middle
        self.play(FadeOut(subline1), FadeOut(arrow))
        self.wait(.1)
        self.play(subline2.animate.move_to(ORIGIN))
        self.wait()
    
        #Title saying make 0! the subject, then make arrow2 in the centre, move subline2 to its left, then create rearragne text on the right
        rearrangetitle = Text('Now make 0! the subject:', font_size = 30, color = GREEN)
        rearrangetitle.to_edge(UP, buff = 1)
        self.play(Write(rearrangetitle))
        self.wait(.5)
        
        arrowtwo = Arrow(start = ORIGIN, end = RIGHT*2, buff = 0.1, color = BLUE)
        arrowtwo.move_to(ORIGIN)

        rearrange = MathTex('0!', '=', r'\frac{1!}{1}', font_size=40)
        rearrange.next_to(arrowtwo, RIGHT, buff = 0.5)

        self.play(subline2.animate.next_to(arrowtwo, LEFT, buff = 0.5))
        self.wait(.3)
        self.play(Create(arrowtwo))
        self.wait(.3)
        self.play(Write(rearrange))
        self.wait(1.5)

        #move rearrange to centre, then morph the fraction to just 1
        self.play(FadeOut(subline2), FadeOut(arrowtwo))
        self.wait(.1)
        self.play(rearrange.animate.move_to(ORIGIN))
        self.wait(.3)
        self.play(rearrange[2].animate.set_color(RED))
        
        fractionsimpl = MathTex('1', font_size = 40)
        fractionsimpl.move_to(rearrange[2])

        self.play(Transform(rearrange[2], fractionsimpl))
        self.wait()
        self.play(FadeOut(rearrangetitle))
        self.wait()

        box = SurroundingRectangle(rearrange, color = YELLOW, buff = 0.25)
        self.play(Create(box))
        self.wait(.2)
        self.play(rearrange.animate.scale(3), box.animate.scale(3))
        self.wait(4)

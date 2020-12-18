#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from turtle import Turtle, Screen

class Star(Turtle):
    def __init__(self, x=0, y=0):
        super().__init__(visible=False)
        self.speed('fastest')
        self.draw_star(x, y)

    def draw_star(self, x=0, y=0):
        """ Creates the star shape """

        self.penup()
        self.setposition(x, y)
        self.pendown()

        
        self.fillcolor("red")

        self.begin_fill()

        for _ in range(9):
            self.left(90)
            self.forward(90)
            self.right(130)
            self.forward(90)

        self.end_fill()
        


t = Star()

screen = Screen()
screen.exitonclick()


# In[ ]:





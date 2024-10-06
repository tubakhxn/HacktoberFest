import turtle
import math

def draw_fractal(t, length, depth):
    if depth == 0:
        t.forward(length)
        return
    draw_fractal(t, length/3, depth-1)
    t.left(60)
    draw_fractal(t, length/3, depth-1)
    t.right(120)
    draw_fractal(t, length/3, depth-1)
    t.left(60)
    draw_fractal(t, length/3, depth-1)

def fractal():
    window = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-200, 100)
    t.pendown()
    
    draw_fractal(t, 400, 4)  # Change the depth for more complexity
    
    window.mainloop()

fractal()

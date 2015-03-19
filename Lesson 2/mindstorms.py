import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("triangle")
    brad.color("blue","yellow")
    brad.speed(3)

    square = 0
    while square < 4:
        brad.forward(100)
        brad.right(90)
        square = square + 1

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

    kevin = turtle.Turtle()
    kevin.shape("square")
    kevin.color("green")
 
    triangle = 0
    while triangle < 3:
        kevin.forward(100)
        kevin.right(120)
        triangle = triangle + 1
    
    window.exitonclick()
    
draw_shapes()

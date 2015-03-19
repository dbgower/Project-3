import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("triangle")
    brad.color("blue","yellow")
    brad.speed(3)

    for i in range(1,37):
        draw_square(brad)
        brad.right(10)

    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("blue")
    #angie.circle(100)

    #kevin = turtle.Turtle()
    #kevin.shape("square")
    #kevin.color("green")
 
    #triangle = 0
    #while triangle < 3:
    #    kevin.forward(100)
    #    kevin.right(120)
    #    triangle = triangle + 1
    
    window.exitonclick()
    
draw_shapes()

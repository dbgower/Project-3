import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("triangle")
    brad.color("blue","yellow")
    brad.speed(3)

    for i in range(1,2):
        brad.forward(10)

draw_shapes()

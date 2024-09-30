import turtle

def draw_axes():
    turtle.penup()
    turtle.goto(-200, 0) 
    turtle.pendown()
    turtle.forward(400) 
    turtle.penup()
    turtle.goto(0, -200) 
    turtle.pendown()
    turtle.left(90)
    turtle.forward(400) 
    turtle.penup()
    
def plot_function():
    turtle.penup()
    turtle.goto(-160, -160 / 5 + 7) 
    turtle.pendown()
    for x in range(-160, 161): 
        y = x / 5 + 7
        turtle.goto(x, y)

#izmantojums
turtle.speed(0)
turtle.pencolor("blue") 
draw_axes()

turtle.pencolor("red") 
plot_function()

turtle.done()

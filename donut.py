import turtle
tr = turtle.Screen()
tr.title("Draw a Donut by Ching")
pen = turtle.Turtle()
pen.color("red")
pen.pensize(5)
pen.speed(0)
pen.up()
pen.forward(-50)
pen.left(90)
pen.down()
for i in range(30):
  for i in range(3):
    pen.forward(10)
    pen.left(30)

  for i in range(10):
    pen.right(15)
    pen.forward(10)

  pen.right(29)

  for i in range(5):
    pen.forward(10)

  for i in range(5):
    pen.right(12)
    pen.forward(10)
    
  for i in range(8):
    pen.forward(10)
turtle.done()

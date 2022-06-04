import turtle

window = turtle.Screen()
window.bgcolor('green')


brad = turtle.Turtle()
n=0
m=0
o=0
h=7500**(.5)
brad.shape('turtle')
brad.color('yellow')
brad.speed(0)

brad.backward(100)

while n<3:
 brad.forward(50)
 brad.left(120)
 brad.forward(100)
 brad.left(120)
 brad.forward(100)
 brad.left(120)
 brad.forward(50)
 brad.left(120)
 brad.forward(50)
 brad.right(120)
 brad.forward(50)
 brad.right(120)
 brad.forward(50)
 brad.left(120)
 brad.up()
 brad.forward(100)
 brad.down()
 n+=1
 
brad.up()
brad.backward(300)
brad.left(90)
brad.forward(h)
brad.right(90)
brad.forward(50)
brad.down()

while m<2:
 brad.forward(50)
 brad.left(120)
 brad.forward(100)
 brad.left(120)
 brad.forward(100)
 brad.left(120)
 brad.forward(50)
 brad.left(120)
 brad.forward(50)
 brad.right(120)
 brad.forward(50)
 brad.right(120)
 brad.forward(50)
 brad.left(120)
 brad.up()
 brad.forward(100)
 brad.down()
 m+=1

brad.up()
brad.backward(200)
brad.left(90)
brad.forward(h)
brad.right(90)
brad.forward(50)
brad.down()

while o<1:
 brad.forward(50)
 brad.left(120)
 brad.forward(100)
 brad.left(120)
 brad.forward(100)
 brad.left(120)
 brad.forward(50)
 brad.left(120)
 brad.forward(50)
 brad.right(120)
 brad.forward(50)
 brad.right(120)
 brad.forward(50)
 brad.left(120)
 brad.up()
 brad.forward(100)
 brad.down()
 o+=1

brad.up()
brad.backward(100)
brad.left(90)
brad.backward(3*h)

window.exitonclick()

import turtle
happy=turtle.Screen()
happy.bgcolor("black")
turtle=turtle.Turtle()
turtle.shape("circle")
turtle.color("yellow")
turtle.width(7)
colors=["peru","ivory","dark orange","coral","cyan","hot pink","gold","ivory","yellow","red","pink","green","blue","light blue","light green",]
def ballon(size):
   turtle.color(colors[size%9])
   turtle.begin_fill()
   turtle.circle(size)
   turtle.end_fill()
   turtle.rt(90)
   turtle.fd(90)

def draw_happy(i,x,y):
    turtle.pencolor("linen")
    turtle.color(colors[i%7])
    turtle.begin_fill()
    turtle.lt(70)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.circle(33)
    turtle.end_fill()

def f1():
   
  for i in range(7):
    turtle.pensize(5)
    turtle.pencolor('light blue')
    turtle.color(colors[i%19])
    turtle.begin_fill()
    turtle.left(330)
    turtle.forward(55)
    turtle.begin_fill()
    turtle.rt(110)
    turtle.circle(33)
    turtle.end_fill()
    turtle.rt(11)
    turtle.backward(33)
    turtle.end_fill()
def cake(x,y):
   turtle.fd(x)
   turtle.rt(90)
   turtle.fd(y)
   turtle.rt(90)
   turtle.fd(x)
   turtle.rt(90)
   turtle.fd(y)
def heart():
   for i in range(43):
         
         turtle.pencolor(colors[i%9])
         turtle.rt(5)
         turtle.fd(5)
         
   turtle.fd(150)
   turtle.penup()
   turtle.rt(140)
   turtle.fd(147)
   turtle.pendown()
   for i in range(43):
         turtle.pencolor(colors[i%9])
         turtle.lt(5)
         turtle.fd(5)
   turtle.lt(7)
   turtle.fd(151)
def move(x,y):
   turtle.up()
   turtle.setposition(0,0)
   turtle.setheading(90)
   turtle.rt(90)
   turtle.fd(x)
   turtle.lt(90)
   turtle.fd(y)
   turtle.pendown()
def mov(x,y):
   turtle.up()
   turtle.setposition(0,0)
   turtle.setheading(90)
   turtle.lt(90)
   turtle.fd(x)
   turtle.rt(90)
   turtle.fd(y)
   turtle.pendown()

def A(size):
  turtle.rt(16)
  turtle.forward(size)
  turtle.rt(150)
  turtle.fd(size)
  turtle.backward(size/2)
  turtle.rt(105)
  turtle.fd(size/3)   
def B():
   turtle.forward(60)
   turtle.rt(90)
   for i in range(18):
      turtle.rt(9)
      turtle.fd(3)
   for i in range(18):
      turtle.rt(13)
      turtle.backward(3)
def C():
   turtle.circle(2)
 
   for i in range(40):
      turtle.lt(5)
      turtle.backward(5)
      
def d(size):
   turtle.fd(size)
   turtle.backward(size)
   turtle.lt(90)
   turtle.fd(26)
   for i in range(15):
      turtle.rt(12)
      turtle.fd(4)
   turtle.fd(14)
def i():
   turtle.fd(60)
def t(size):
   turtle.fd(size)
   turtle.backward(size/2)
   turtle.lt(90)
   turtle.fd(10)
   turtle.backward(20)
def H():
   turtle.fd(60)
   turtle.backward(30)
   turtle.rt(90)
   turtle.fd(30)
   turtle.lt(90)
   turtle.fd(30)
   turtle.backward(60)
def P():
   turtle.fd(60)
   turtle.rt(90)
   turtle.fd(7)
   for i in range(8):
       turtle.rt(20)
       turtle.fd(5)
def Y():
   turtle.fd(40)
   turtle.left(60)
   turtle.fd(20)
   turtle.backward(20)
   turtle.rt(90)
   turtle.fd(35)
def R():
   turtle.fd(60)
   turtle.rt(90)
   turtle.fd(7)
   for i in range(15):
      turtle.rt(12)
      turtle.fd(3)
   turtle.lt(120)
   turtle.fd(49)
def D():
   turtle.fd(60)
   turtle.rt(90)
   turtle.fd(9)
   for i in range(13):
      turtle.rt(13)
      turtle.fd(7)  

   
turtle.speed(0)  
turtle.width(9)

turtle.pencolor("cyan")
mov(220,300)
H()
mov(180,300)
A(65)
mov(135,300)
P()
mov(100,300)
P()
mov(52,300)
Y()
mov(28,300)
B()
move(12,300)
i()
move(36,300)
R()
move(80,300)
t(100)
move(102,300)
H()
move(150,300)
D()
move(190,300)
A(65)
move(250,300)
Y()
mov(120,400)
turtle.color(colors[8%5])
turtle.begin_fill()
cake(40,180)
turtle.end_fill()
mov(110,435)
turtle.color(colors[8%3])
turtle.begin_fill()
cake(40,160)
turtle.end_fill()
mov(100,470)
turtle.color("hot pink")
turtle.begin_fill()
cake(40,140)
turtle.end_fill()
mov(30,510)
turtle.width(11)
turtle.pencolor("red")
turtle.circle(7)
move(180,497)
f1()
mov(0,0)
for i in range(5):
    draw_happy(i,-189,200)  
    
for i in range(6):
   draw_happy(i,189,200) 
for i in range(7):
   draw_happy(i,123,-100)
for i in range(5):
   draw_happy(i,-123,-100) 
mov(-30,-70)
turtle.width(9)
heart()  
for i in range(9):
   draw_happy(i,0,-295) 
turtle.width(7)

   

    

happy.exitonclick()

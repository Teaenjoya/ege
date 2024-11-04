import turtle
t=turtle.Turtle()
t.rt(-90)
s=15
t.down
for i in range (4):
  t.fd(10*s)
  t.rt(90)
t.up()
for x in range (-20,20):
  for y in range (-20,20):
    t.setpos(x*s,y*s)
    t.dot(4,'blue')
t.done()
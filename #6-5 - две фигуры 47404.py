import turtle
t=turtle.Turtle()
t.rt(-90)
s=19
t.down
for i in range (4):
  t.fd(12*s)
  t.rt(90)
t.rt(30)
for i in range(3):
  t.fd(8*s)
  t.rt(60)
  t.fd(8*s)
  t.rt(120)
t.up()
for x in range (-20,20):
  for y in range (-20,20):
    t.setpos(x*s,y*s)
    t.dot(1,'blue')
t.done()
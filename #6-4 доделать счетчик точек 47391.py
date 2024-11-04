import turtle
t=turtle.Turtle()
t.rt(-90)
s=19
t.down
for i in range (14):
  t.rt(60)
  t.fd(2*s)
  t.rt(60)
  t.fd(2*s)
  t.rt(270)
t.up()
for x in range (-20,20):
  for y in range (-20,20):
    t.setpos(x*s,y*s)
    t.dot(1,'blue')
t.done()
import turtle
t = turtle.Turtle()
size=30
t.tracer(0)
t.down()
for i in range(7):
    t.fd(10*size)
    t.rt(120)
t.up()
for x in range(-20,20):
    for y in range(-20,20):
        t.setpos(x*size,y*size)
        t.dot(4,'red')
t.done()
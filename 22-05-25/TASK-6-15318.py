from turtle import *
tracer(0)
screensize(2000,2000)
m = 20
lt(90)
pendown()

for i in range(2):
    fd(13 * m)
    rt(90)
    fd(18 * m)
    rt(90)
penup()
fd(5 * m)
rt(90)
fd(9 * m)
lt(90)
pendown()
for i in range(2):
    fd(11 * m)
    rt(90)
    fd(7 * m)
    rt(90)
penup()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*m, y*m)
        dot(3, 'red')
update()
done()
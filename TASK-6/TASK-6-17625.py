from turtle import *

screensize(10_000, 10_000)
tracer(0)
m = 20
lt(90)
pendown()

for i in range(10):
    fd(22  * m)
    rt(90)
    fd(16 * m)
    rt(90)
penup()

fd(1 * m)
rt(90)
fd(1 * m)
lt(90)
pendown()

for i in range(10):
    fd(72 * m)
    rt(90)
    fd(79 * m)
    rt(90)
penup()

for x in range(-30, 30):
    for y in range(-30,30):
        goto(x * m, y * m)
        dot(5, 'white')

update()
done()
from turtle import *

tracer(0)
screensize(2000,2000)
lt(90)
m = 20
for i in range(9):
    fd(22 * m)
    rt(90)
    fd(6 * m)
    rt(90)

penup()

fd(1 * m)
rt(90)
fd(5 * m)
lt(90)
down()

for i in range(9):
    fd(53 * m)
    rt(90)
    fd(75 * m)
    rt(90)

up()
for x in range(-20, 30):
    for y in range(-20, 30):
        goto(x * m, y * m)
        dot(3,'red')





update()
done()
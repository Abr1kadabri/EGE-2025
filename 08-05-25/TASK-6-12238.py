from turtle import *
tracer(0)
screensize(2000, 2000)
m = 20
lt(90)

for i in range(2):
    fd(5 * m)
    lt(90)
    bk(13 * m)
    lt(90)
penup()
bk(10 * m)
rt(90)
fd(9 * m)
lt(90)
pendown()

for i in range(2):
    fd(11 * m)
    rt(90)
    fd(7 * m)
    rt(90)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * m, y * m)
        dot(3,'red')

update()
done()

from turtle import Turtle, Screen

def spir(d):
    if d > 800:
        pass     # nerob nič
    else:
        t.fd(d)
        t.lt(60)
        spir(d + 3)




t = Turtle()
t.speed(0)
spir(10)

Screen().exitonclick()
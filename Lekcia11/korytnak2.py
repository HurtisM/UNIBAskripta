from turtle import Turtle, Screen


tommy = Turtle()
tommy.shape("turtle")
tommy.color("red","green")


def stvorce(n, a):
    if n == 0:
        pass
    else:
        for i in range(4):
            tommy.fd(a)
            tommy.rt(90)
            stvorce(n - 1, a *0.3)
            # skúste: stvorce(n - 1, a * 0.45)

def stvorce_sikme(n, d):
    tommy.pencolor("black")
    if n > 0:
        for i in range(4):
            tommy.fd(d)
            tommy.rt(90)
            tommy.lt(30)
            stvorce(n - 1, d / 3)
            tommy.rt(30)

my_screen = Screen()

tommy.speed(0)
stvorce(4, 300)

tommy.pu()
tommy.setpos(-310, 350)
tommy.pd()
stvorce_sikme(3,200)


my_screen.exitonclick()


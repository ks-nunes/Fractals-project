from turtle import*

def kochCurve(length, generation):
    if generation == 0:
        forward(length)
        return
    length /= 3.0
    kochCurve(length, generation - 1)
    left(60)
    kochCurve(length, generation - 1)
    left(240)
    kochCurve(length, generation - 1)
    left(60)
    kochCurve(length, generation - 1)

speed(0)
length = 600.0
generation = int(input("Which generation would you like to generate? (keep in mind the higher the number the longer it'll take to finish)"))

penup()
backward(length/2)
left(90)
forward(length/4)
right(90)
pendown()

kochCurve(length, generation)
right(120)
kochCurve(length, generation)
right(120)
kochCurve(length, generation)

mainloop()

from turtle import* 

speed(0)
length = 900
Turtle._screen.setup(1280, 720)
screensize(1280, 720)
thickness = 15

initialAxioms = 'A'
rules = { 'A' : 'ABA' , 'B' : 'BBB'} 
generation = int(input("Up to which generation would you like to draw?"))

penup()
backward(length/2)
left(90)
forward(150)
right(90)

#Defines an empty variable which is filled every time with the application of the rule onto the axioms
def lsystem(initialAxioms, rules, x):
    for everynumber in range(x):
        newAxioms = ''

        for axiom in initialAxioms:
            if axiom in rules:
                newAxioms += rules[axiom]
            else:
                newAxioms += axiom
        
        initialAxioms = newAxioms
    return initialAxioms


def loop(initialAxioms, rules, generation, x, thickness):
    for everyGen in range(generation):
        if x == (generation):
            break
        else:
            arrayafication = list(lsystem(initialAxioms, rules, x))           

            #Takes the variable thickness we defined and removes one, so that each generation is less thick making the fractal more appealing
            #sadly it also breakes the code if your input is higher than 5 because for some reason that makes it think it's a negative
            #to fix this just delete the below two lines, and and remove all other mentions of it.
            #thickness -= x
            #width(thickness)

            #Decides how far the turtle should draw each letter
            numberofletters = len(arrayafication)
            def IndividualLength(length):
                indvLength = length/numberofletters
                return indvLength

            #Checks every letter and draws it
            def drawTurtle():
                for everyLetter in range(numberofletters):
                    for letter in arrayafication:
                        if letter == 'A':
                            pendown()
                            forward(IndividualLength(length))
                        else:
                            penup()
                            forward(IndividualLength(length))
                    break


            drawTurtle()

            #Moves the turtle to new startposition beneath the first line
            penup()
            backward(length)
            right(90)
            forward(30)
            left(90)

            x += 1    

#Runs the above
loop(initialAxioms, rules, generation, 0, thickness)
hideturtle()
print("Task Completed!")

#Makes it so that the windows stays after it's finished
mainloop()

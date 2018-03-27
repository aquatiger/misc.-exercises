# create a user-defined polygon
import turtle


wn = turtle.Screen()
hadir = turtle.Turtle()
hadir.speed(8)

sides = int(input("Please enter the number of sides of a polygon you want drawn: "))
length = int(input("How long would you like each side? "))
outlineColor = input("What color would you like for the outline?")
filler = input("And what color would you like to fill it with? ")

hadir.begin_fill()
hadir.color(outlineColor)
print(filler)
for i in range(sides):
    hadir.forward(length)
    hadir.left(360 / sides)
    hadir.up()
hadir.end_fill()

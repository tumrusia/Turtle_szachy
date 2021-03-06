import turtle
from math import *

def ini():
	turtle.setup(600,600)
	turtle.mode("logo")
	
def krol(size, kolor, ann):
	
	poz = size/6
	pion = size/6	
	
	ann.up()
	ann.fd(pion)
	ann.right(90)
	ann.fd(2*poz)
	ann.down()
	
	ann.fillcolor(kolor)
	ann.begin_fill()
	ann.fd(2*poz)
	ann.left(90)
	ann.fd(pion)
	ann.pensize(0)
	ann.fd(pion)
	ann.left(90)
	ann.fd(2*poz)
	ann.left(90)
	ann.fd(pion)
	ann.pensize(1)
	ann.fd(pion)
	ann.left(90)
	ann.end_fill()
	
	ann.begin_fill()
	ann.left(90)
	ann.fd(pion)
	ann.right(90)
	ann.circle(pion)
	ann.up()
	ann.fd(2*poz)
	ann.down()
	ann.circle(pion)
	ann.end_fill()
	
	ann.up()
	ann.left(90)
	ann.fd(2*pion)
	ann.left(90)
	ann.fd(5/6*poz)
	ann.right(90)
	ann.down()
	ann.begin_fill()
	ann.fd(3/2*pion)
	ann.left(90)
	ann.fd(1/3*poz)
	ann.left(90)
	ann.fd(3/2*pion)
	ann.left(90)
	ann.fd(1/3*poz)
	ann.end_fill()
	ann.up()
	ann.right(90)
	ann.fd(pion/2)
	ann.right(90)
	ann.fd(1/6*pion)
	ann.left(180)
	ann.down()
	ann.begin_fill()
	ann.circle(pion/2)	
	ann.end_fill()
	
	ann.up()
	ann.right(90)
	ann.fd(7/2*pion)
	ann.right(90)
	ann.fd(3*poz)
	ann.right(90)
	ann.down()
	

ini()
ann = turtle.Turtle()
krol(420, "pink", ann)
turtle.mainloop()
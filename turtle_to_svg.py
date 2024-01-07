
"""
Turtle drawing to SVG

Author: mosselini1 (https://www.printables.com/@mosselini1_1346202)
Date: 22/12/23
"""

import os, turtle
import canvasvg
	
def draw_sierpinski(t, length, depth):
	"""
	author: Kevin
	https://stackoverflow.com/questions/25772750/sierpinski-triangle-recursion-using-turtle-graphics
	"""
	if depth == 0:
		for i in range(3):
			t.fd(length)
			t.left(120)
	else:
		draw_sierpinski(t, length / 2, depth - 1)
		t.fd(length / 2)
		draw_sierpinski(t, length / 2, depth - 1)
		t.bk(length / 2)
		t.left(60)
		t.fd(length / 2)
		t.right(60)
		draw_sierpinski(t, length / 2, depth - 1)
		t.left(60)
		t.bk(length / 2)
		t.right(60)

def draw(t):
	t.penup()
	t.goto(-200, -175)
	t.pendown()
	draw_sierpinski(t, 400, 6)

def main(res_dir,outname):
	
	filepath = os.path.join(res_dir, outname)
	
	t = turtle.Turtle(visible=False)
	t.speed(speed=0)
	draw(t)
	
	t_scrn = t.getscreen()
	canvasvg.warnings(canvasvg.NONE)
	canvasvg.saveall(filepath, t_scrn.getcanvas())
	t_scrn.bye()
	
	try: turtle.done()
	except Exception as e: pass
	
if __name__ == "__main__": 
	main(os.getcwd(),"res.svg")

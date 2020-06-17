import turtle
import math


def ellipse(a, b, h=None, k=None, angle=None, angle_unit=None):
    myturtle = turtle.Turtle()

    if h is None:
        h = 0
    if k is None:
        k = 0
    # Angle unit can be degree or radian

    if angle is None:
        angle = 360
        converted_angle = angle*0.875

    if angle_unit == 'd' or angle_unit is None:
        converted_angle = angle * 0.875

    # We are multiplying by 0.875 because for making a complete ellipse we are plotting 315 pts according
    # to our parametric angle value

    elif angle_unit == "r":
        converted_angle = (angle * 0.875 * (180/math.pi))
    # Converting radian to degrees.

    for i in range(int(converted_angle)+1):
        if i == 0:
            myturtle.up()
        else:
            myturtle.down()
        myturtle.setposition(h+a*math.cos(i/50), k+b*math.sin(i/50))


def parabola(a, t, orientation, h=None, k=None):
    myturtle = turtle.Turtle()
    myturtle.speed(20)
    if h is None:
        h = 0
    if k is None:
        k = 0
    if orientation == 'x':
        i = -t
        while i <= t:
            if i == -t:
                myturtle.up()
                myturtle.hideturtle()
            else:
                myturtle.showturtle()
                myturtle.down()
            myturtle.setposition(h+a*math.pow(i, 2), k+2*a*i)
            i += 1/8
    elif orientation == 'y':
        i = -t
        while i <= t:
            if i == -t:
                myturtle.up()
                myturtle.hideturtle()
            else:
                myturtle.showturtle()
                myturtle.down()
            myturtle.setposition(h + 2*a*i, k + a * math.pow(i, 2))
            i += 1/8


def hyperbola(a, b, h=None, k=None):
    myturtle = turtle.Turtle()
    if h is None:
        h = 0
    if k is None:
        k = 0

    if a > b:
        for i in range(64):
            if i == 0:
                myturtle.up()
            else:
                myturtle.down()
            myturtle.setposition(h+a*(1/math.cos(i/10)), k+b*math.tan(i/10))
    
    elif a == b:
        for i in range(64):
            if i == 0:
                myturtle.up()
            else:
                myturtle.down()
            myturtle.setposition(h+a*(1/math.cos(i/10)), k+a*math.tan(i/10))

    if b > a:
        for i in range(64):
            if i == 0:
                myturtle.up()
            else:
                myturtle.down()
            myturtle.setposition(h+b*math.tan(i/10), k+a*(1/math.cos(i/10)))
            
def cardioid(a, orientation, h=None, k=None, angle=None, angle_unit=None):
    myturtle = turtle.Turtle()
    if h is None:
        h = 0
    if k is None:
        k = 0
    # Angle unit can be degree or radian

    if angle is None:
        angle = 360
        converted_angle = angle * 0.875

    if angle_unit == 'd' or angle_unit is None:
        converted_angle = angle * 0.875

    # We are multiplying by 0.875 because for making a complete cardioid we are plotting 315 pts according
    # to our parametric angle value

    elif angle_unit == "r":
        converted_angle = (angle * 0.875 * (180/math.pi))
    # Converting radian to degrees.

    if orientation == 'x':
        for i in range(int(converted_angle)+1):
            if i == 0:
                myturtle.up()
            else:
                myturtle.down()
            myturtle.setposition(h+a*math.cos(i/50)*(1-math.cos(i/50)), k+a*math.sin(i/50)*(1-math.cos(i/50)))

    elif orientation == 'y':
        for i in range(int(converted_angle)+1):
            if i == 0:
                myturtle.up()
            else:
                myturtle.down()
            myturtle.setposition(h+a*math.sin(i/50)*(1-math.cos(i/50)), k+a*math.cos(i/50)*(1-math.cos(i/50)))
            
            
def heart(a, b, orientation, h=None, k=None, angle=None, angle_unit=None):
    myturtle = turtle.Turtle()

    if h is None:
        h = 0
    if k is None:
        k = 0
    # Angle unit can be degree or radian

    if angle is None:
        angle = 360
        converted_angle = angle * 0.875

    if angle_unit == 'd' or angle_unit is None:
        converted_angle = angle * 0.875

    # We are multiplying by 0.875 because for making a complete cardioid we are plotting 315 pts according
    # to our parametric angle value

    elif angle_unit == "r":
        converted_angle = (angle * 0.875 * (180/math.pi))
    # Converting radian to degrees.

    if orientation == 'y':
        i = 0
        while i <= converted_angle:
            if i == 0:
                myturtle.up()
            else:
                myturtle.down()
            myturtle.setposition(h+a*(16*math.pow(math.sin(i/50), 3)), k+b*(13*math.cos(i/50)-5*math.cos(2*(i/50))-2*math.cos(3*(i/50))
                                 - math.cos(4*(i/50))))
            i += 1

    elif orientation == 'x':
        i = 0
        while i <= converted_angle:
            if i == 0:
                myturtle.up()
            else:
                myturtle.down()
            myturtle.setposition(k+b*(13*math.cos(i/50)-5*math.cos(2*(i/50))-2*math.cos(3*(i/50))
                                 - math.cos(4*(i/50))), h+a*(16*math.pow(math.sin(i/50), 3)))
            i += 1

def butterfly(a, b, n=None, h=None, k=None):
    myturtle = turtle.Turtle()

    if h is None:
        h = 0
    if k is None:
        k = 0
    if n is None:
        n = 602
#  Default value for no of turns is 602 since that is the required no of turns to complete the curve.   
    for i in range(n+1):
        if i == 0:
            myturtle.up()
        else:
            myturtle.down()
        myturtle.setposition(h + a*math.sin(i/30)*(math.exp(math.cos(i/30)) - 2*math.cos((4*i)/30) - math.pow(math.sin(i/360), 5))
                             , k + b*math.cos(i/30)*(math.exp(math.cos(i/30)) - 2*math.cos((4*i)/30) - math.pow(math.sin(i/360), 5)))


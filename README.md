
Creating Conic Sections using Python Turtle
===================


We have created a Python package '**turtle_conics**'.Using this package, we can draw different curves like **Ellipse** ,**Parabola**, **Hyperbola** in Python Turtle in any orientation as you like. 
*THIS IS THE LATEST VERSION OF THE PACKAGE. * 
**Check out the Source code for the Package in my [Github Repository](https://github.com/Devansu-Yadav/My-First-Python-Package)**

----------
FEATURES
--------------
>-*Simple function to create any of the above mentioned curves by importing functions from **all_curves** module specifying the arguments.* 
>-*Can be used inside Looping structures to create different patterns.*
--------
WHAT'S NEW
------------------
>- **Added Butterfly curve in the new update**
>- **Added Heart curve in the update (0.1.1)**
>- **Added Cardioid curve in the update (0.1.0)**
--------
How To Import The Package ?
-------------------------
*NOTE:- While Importing the Package, the name of the package is  'turtle_conics' and not 'turtle-conics'. 
---------------------------------------------
>- **For importing all functions inside the package:-**

>  import turtle
>  from turtle_conics.all_curves import *
>  #Now make a function call for any of the curves
>  turtle.done()

>- **For importing a single function inside package:**

> import turtle
> from turtle_conics.all_curves import (func)
> #Now make a function call for any of the curves
> turtle.done()



HISTORY
-----------
**0.0.1** (2020-05-22)
>- *First release on PyPI*

**0.0.2**(2020-05-24)
>- *Added Rectangular Hyperbola*

**0.1.0**(2020-05-27)
>- *Added Cardioid curve*

**0.1.1**(2020-06-05)
>- *Added Heart curve*

**0.1.2**(2020-06-05)
>- *Made few changes in the package*

**0.1.3**(2020-06-15)
>- *Added Butterfly curve*

Package Description
----------------------------

The '**turtle_conics**' package consists of  module '**all_curves**' with 5 functions to draw Ellipse, Parabola, Hyperbola, Cardioid and the Heart Curve.

--**ELLIPSE**
 
 **We can draw 2 types of ellipse**:-
 **- Major axis along X axis (a>b)**
 **- Major axis along Y axis (b>a)**
> 
**def ellipse(a, b, h= None, k= None, angle= None, angle_unit= None)**
>- **a**:-It is the half-length of major axis of ellipse if (a>b) else half-length of minor axis when(b>a).
>- **b**:-It is the half-length of major axis of ellipse if (b>a) else half-length of minor axis when (a>b).
>- **h,k**:-(Optional) For drawing ellipses with **center (h,k)**.By default both are **zero**.
>- **angle**(Optional) By providing the angle we can draw elliptical arcs upto that specific angle. By default **angle** is set to **360** degrees.
>- **angle_unit**(Optional) The argument for **angle** can be in **degrees** or  **radians**. By default it is set to **'d'**.
**NOTE:-** **For  angle_units specify argument as 'd' or 'r'**.


--**Parabola**

 **We can draw 4 types of parabola:-**
 **-Parabola along +ve X axis**
 **-Parabola along -ve X axis**
 **-Parabola along +ve Y axis**
**-Parabola along -ve Y axis**
> 
**def parabola(a, t, orientation, h=None, k=None)**
>- **a**:- It is the distance from the origin to the focus of parabola.
>- **t**:- It is a parameter of a parabola.Used to define the curvature of parabola.Value of **t** should be greater than **zero**.
>- **orientation**:-Takes argument as **'x'** or **'y'** for drawing parabola along X axis or Y axis.
>- **h,k**:-(Optional) For drawing parabola with **vertex at (h,k)**.By default both are **zero**.
>- **NOTE:-** **For drawing Parabola along  Negative  Axes pass Negative value for  'a'**.  

--**Hyperbola**

**We can draw 2 types of Hyperbola:-**
**-Transverse axis ie hyperbola along X axis(a>b)**
**-Transverse axis ie hyperbola along Y axis(b>a)**

> **def hyperbola(a, b, h=None, k=None)**
>- **a** :-It represents the distance from the vertex to the center of hyperbola when (a>b) else it represents the distance perpendicular to the transverse axis from the vertex to the asymptote line when (b>a).
>- **b**:-It represents the distance from the vertex to the center of hyperbola when (b>a) else it represents the distance perpendicular to the transverse axis from the vertex to the asymptote line when (a>b).
> - **h,k**:-(Optional) For drawing hyperbola with **center (h,k)**.By default both are **zero**.
>- **We can also make a Rectangular Hyperbola by giving equal values to 'a' and 'b'.**
>- **NOTE:-For drawing Hyperbola along X axis enter values for 'a' and 'b' such that (a>b) else for drawing hyperbola along Y axis put (b>a) .**

--**CARDIOID**
 
 **We can draw 4 types of cardioid**:-
 **-Axis along X-axis**
 **#Cardioid along +ve X axis**
 **#Cardioid along -ve X axis**
 
 **-Axis along Y-axis**
 **#Cardioid along +ve Y axis**
 **#Cardioid along -ve Y axis**
 
>**def cardioid(a, orientation, h=None, k=None, angle=None, angle_unit=None)**
>- **a**:-It defines the size of the cardioid.
>- **orientation**:-Takes argument as **'x'** or **'y'** for drawing cardioid along X axis or Y axis.
>- **h,k**:-(Optional) For drawing cardioid whose starting point is    **(h,k)**. By default both are **zero**.
>- **angle**(Optional) By providing the angle we can draw arcs of the cardioid upto that specific angle. By default **angle** is set to **360** degrees.
>- **angle_unit**(Optional) The argument for **angle** can be in **degrees** or  **radians**. By default it is set to **'d'**.
**NOTE:-** **For  **angle_units** specify argument as 'd' or 'r'**. **For drawing Cardioid along  Negative  Axes pass Negative value for  'a'**.  

--**HEART CURVE**
 
 **We can draw 4 types of hearts**:-
 **-Axis along X-axis**
 **#Heart along +ve X axis**
 **#Heart along -ve X axis**
 
 **-Axis along Y-axis**
 **#Heart along +ve Y axis**
 **#Heart along -ve Y axis**
 
>**def heart(a, b, orientation, h=None, k=None, angle=None, angle_unit=None)**
>- **a**:-It defines the Horizontal size of the heart.
>- **b**:-It defines the Vertical size of the heart.
>- **orientation**:-Takes argument as **'x'** or **'y'** for drawing heart along X axis or Y axis.
>- **h,k**:-(Optional) For drawing heart whose starting point is    **(h,k)**. By default both are **zero**.
>- **angle**(Optional) By providing the angle we can draw arcs of the heart upto that specific angle. By default **angle** is set to **360** degrees.
>- **angle_unit**(Optional) The argument for **angle** can be in **degrees** or  **radians**. By default it is set to **'d'**.
**NOTE:-** **For  angle_units specify argument as 'd' or 'r'**. **For drawing Heart along  Negative Axes pass Negative value for  'b'**.  

--**THE BUTTERFLY CURVE**

**def butterfly(a, b, n=None,h= None, k= None)**

>- **a**:-It defines the Horizontal size of the butterfly.
>- **b**:-It defines the Vertical size of the butterfly.
>- **n**:-(Optional) It is the **Number of Turns** to draw a Butterfly. By Default it is set to **602** turns.
>- **h,k**:-(Optional) For drawing a butterfly whose starting point is    **(h,k)**. By default both are **zero**.
**NOTE:-** **To make a Perfect Butterfly you can set the values of 'a' and 'b' as equal**.  



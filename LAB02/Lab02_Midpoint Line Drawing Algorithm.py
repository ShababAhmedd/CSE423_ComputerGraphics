from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

############################
### Find Zone Algorithm  ###
############################
def findZone(x0, y0, x1, y1):

    dy = y1-y0
    dx = x1-x0

    if abs(dx) > abs(dy):   # Represents zone 0, 3, 4, 7.
        if dx > 0 and dy > 0:
            print("FindZone: 0")
            return 0
        elif dx < 0 and dy > 0:
            print("FindZone: 3")
            return 3
        elif dx < 0 and dy < 0:
            print("FindZone: 4")
            return 4
        else:
            print("FindZone: 7")
            return 7

    else:                   # Represents zone 1, 2, 5, 6.
        if dx > 0 and dy > 0:
            print("FindZone: 1")
            return 1
        elif dx < 0 and dy > 0:
            print("FindZone: 2")
            return 2
        elif dx < 0 and dy < 0:
            print("FindZone: 5")
            return 5
        else:
            print("FindZone: 6")
            return 6
#============================================================

#######################################
### Zone Zero Conversion Algorithm  ###
#######################################
def ZoneZeroConversion(zone, x, y):

    if zone == 0:
        print("Zone Zero Conversion Executed:", x, ",", y)
        return x, y
    elif zone == 1:
        print("Zone Zero Conversion Executed:", y, ",", x)
        return y, x
    elif zone == 2:
        print("Zone Zero Conversion Executed:", -y, ",", x)
        return -y, x
    elif zone == 3:
        print("Zone Zero Conversion Executed:", -x, ",", y)
        return -x, y
    elif zone == 4:
        print("Zone Zero Conversion Executed:", -x, ",", -y)
        return -x, -y
    elif zone == 5:
        print("Zone Zero Conversion Executed:", -y, ",", -x)
        return -y, -x
    elif zone == 6:
        print("Zone Zero Conversion Executed:", -y, ",", x)
        return -y, x
    elif zone == 7:
        print("Zone Zero Conversion Executed:", x, ",", -y)
        return x, -y
#-----------------------------------------------------------
#########################################
### Zero to Original zone Algorithm ###
########################################
def zero_to_original_zone(zone, x, y):

    if zone == 0:
        print("Converted to original zone:", x, ",", y)
        return x, y
    if zone == 1:
        print("Converted to original zone:", y, ",", x)
        return y, x
    if zone == 2:
        print("Converted to original zone:", -y, ",", -x)
        return -y, -x
    if zone == 3:
        print("Converted to original zone:", -x, ",", y)
        return -x, y
    if zone == 4:
        print("Converted to original zone:", -x, ",", -y)
        return -x, -y
    if zone == 5:
        print("Converted to original zone:", -y, ",", -x)
        return -y, -x
    if zone == 6:
        print("Converted to original zone:", y, ",", -x)
        return y, -x
    if zone == 7:
        print("Converted to original zone:", x, ",", -y)
        return x, -y
#-----------------------------------------------------------
#########################################
### Mid Point Line Drawing Algorithm ###
########################################
def MidPointLine(zone, x0, y0, x1, y1):

    dy = y1-y0
    dx = x1-x0
    d_init = 2*dy - dx
    e = 2*dy
    ne = 2*(dy-dx)

    x = x0
    y = y0

    while x <= x1:

        a, b = zero_to_original_zone(zone, x, y)        # Converting the points to the original zone and then drawing it
        draw_points(a, b)
        print("point drawn")

        if d_init <= 0:
            x += 1
            d_init += e

        else:
            x += 1
            y += 1
            d_init += ne
#-----------------------------------------------------------
# This is the control centre from where the whole eight way symmetry algorithm is executed.
def eight_way_symmetry(x0, y0, x1, y1):
    zone = findZone(x0, y0, x1, y1)
    z0_x0, z0_y0 = ZoneZeroConversion(zone, x0, y0)
    z0_x1, z0_y1 = ZoneZeroConversion(zone, x1, y1)
    MidPointLine(zone, z0_x0, z0_y0, z0_x1, z0_y1)
    print("Task finished!")
    print("=================================================================")
    print()
#-----------------------------------------------------------
def three():
    eight_way_symmetry(100, 400, 200, 400)
    eight_way_symmetry(100, 300, 200, 300)
    eight_way_symmetry(100, 200, 200, 200)
    eight_way_symmetry(200, 400, 200, 200)

def seven():
    eight_way_symmetry(300, 400, 400, 400)
    eight_way_symmetry(300, 200, 400, 400)
#-----------------------------------------------------------
# This function is used to draw pixels.
def draw_points(x, y):
    # The parameter that is passed in the function dictates the size of the pixel.
    glPointSize(5)

    glBegin(GL_POINTS)

    # Think of this as a co-ordinate. At the given x and y position the pixel will be drawn.
    glVertex2f(x, y)


    glEnd()

def iterate():
    glViewport(0, 0, 500, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 600, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    # (Red, Green, Blue)
    glColor3f(1.0, 1.0, 1.0)

    ###============================###
    ### call_the_draw_methods_here ###
    ###============================###

    three()
    seven()

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)

# Size of the window.
# Manipulating this value will let us change the size of the output widow where the pixel is shown.
glutInitWindowSize(500, 600)

glutInitWindowPosition(0, 0)

# window name
wind = glutCreateWindow(b"LAB02: Midpoint Line Drawing Algorithm")

glutDisplayFunc(showScreen)

glutMainLoop()
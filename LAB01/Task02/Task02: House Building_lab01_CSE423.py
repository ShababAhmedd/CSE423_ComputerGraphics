from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# This function is used to draw pixels.
def draw_points(x, y):
    # The parameter that is passed in the function dictates the size of the pixel.
    glPointSize(10)

    glBegin(GL_POINTS)

    # Think of this as a co-ordinate. At the given x and y position the pixel will be drawn.
    glVertex2f(x, y)

    glEnd()


# This function is used to draw lines.
def draw_lines():
    glBegin(GL_LINES)

#-----------Exterior_Rectangle-----------
    #==========X-axis==========#
    glVertex2f(100, 100)
    glVertex2f(500, 100)

    glVertex2f(100, 500)
    glVertex2f(500, 500)
    #==========Y-axis==========#
    glVertex2f(100, 100)
    glVertex2f(100, 500)

    glVertex2f(500, 100)
    glVertex2f(500, 500)

# -----------Interior_two_Rectangles-----------
    #==========X-axis==========#
    glVertex2f(150, 350)
    glVertex2f(250, 350)

    glVertex2f(150, 450)
    glVertex2f(250, 450)

    glVertex2f(350, 350)
    glVertex2f(450, 350)

    glVertex2f(350, 450)
    glVertex2f(450, 450)
    #==========Y-axis==========#
    glVertex2f(150, 350)
    glVertex2f(150, 450)

    glVertex2f(250, 350)
    glVertex2f(250, 450)

    glVertex2f(350, 350)
    glVertex2f(350, 450)

    glVertex2f(450, 350)
    glVertex2f(450, 450)

#-----------Interior_Door-----------
    # ==========X-axis==========#
    glVertex2f(250, 100)
    glVertex2f(350, 100)

    glVertex2f(250, 250)
    glVertex2f(350, 250)
    #==========Y-axis==========#
    glVertex2f(250, 100)
    glVertex2f(250, 250)

    glVertex2f(350, 100)
    glVertex2f(350, 250)
    glEnd()

def draw_points(x, y):
    # The parameter that is passed in the function dictates the size of the pixel.
    glPointSize(5)

    glBegin(GL_POINTS)

    # Think of this as a co-ordinate. At the given x and y position the pixel will be drawn.
    glVertex2f(x, y)

    glEnd()

def drawTriangle():
    glBegin(GL_TRIANGLES)
    # The points have to be in anticlockwise order.
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(100, 500)
    glVertex2f(500, 500)
    glVertex2f(300, 750)
    glEnd()

def iterate():
    glViewport(0, 0, 600, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 600, 0.0, 800, 0.0, 1.0)
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
    # draw_points function to draw pixels.
    draw_points(330, 170)
    #--------------------------------------
    # draw_lines function to draw lines.
    draw_lines()
    #--------------------------------------
    # drawTriangle function to draw triangles with colours filled within it.
    glColor3f(1.0, 0.0, 0.0)
    drawTriangle()
    #--------------------------------------

    #--------------------------------------
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)

# Size of the window.
# Manipulating this value will let us change the size of the output widow where the pixel is shown.
glutInitWindowSize(600, 800)

glutInitWindowPosition(0, 0)

# window name
wind = glutCreateWindow(b"Task02: House Building")

glutDisplayFunc(showScreen)

glutMainLoop()
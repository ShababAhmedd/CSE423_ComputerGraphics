from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

# This function is used to draw pixels.
def draw_points():
    # The parameter that is passed in the function dictates the size of the pixel.
    glPointSize(5)
    glBegin(GL_POINTS)

    coordinate_points = 50
    for i in range(coordinate_points):
        x = random.randint(1, 500)
        y = random.randint(1, 500)
        # Think of this as a co-ordinate. At the given x and y position the pixel will be drawn.
        glVertex2f(x, y)

    glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
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
    draw_points()

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)

# Size of the window.
# Manipulating this value will let us change the size of the output widow where the pixel is shown.
glutInitWindowSize(500, 500)

glutInitWindowPosition(0, 0)

# window name
wind = glutCreateWindow(b"Task01: Drawing Pixels")

glutDisplayFunc(showScreen)

glutMainLoop()
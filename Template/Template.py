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
    #===================================================
    glVertex2f(10, 10)    # Starting point of the line.
    glVertex2f(490, 490)    # Ending point of the line.
    #===================================================
    glEnd()


def drawTriangle():
    glBegin(GL_TRIANGLES)
    # The points have to be in anticlockwise order.
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(100, 250)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(200, 250)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(200, 300)

    glEnd()


def drawQuads():
    glBegin(GL_QUADS)

    # The points have to be in anticlockwise order.
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(300, 300)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(400, 300)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(400, 100)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(300, 100)

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
    #glColor3f(1.0, 1.0, 0.0)

    ###============================###
    ### call_the_draw_methods_here ###
    ###============================###
    # draw_points function to draw pixels.
    glColor3f(0.0, 1.0, 0.0)
    draw_points(250, 250)
    #--------------------------------------
    # draw_lines function to draw lines.
    glColor3f(1.0, 0.0, 0.0)
    draw_lines()
    #--------------------------------------
    # drawTriangle function to draw triangles with colours filled within it.
    drawTriangle()
    #--------------------------------------
    #drawQuads function to draw quads with colours filled  within it.
    drawQuads()
    #--------------------------------------
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)

# Size of the window.
# Manipulating this value will let us change the size of the output widow where the pixel is shown.
glutInitWindowSize(500, 500)

glutInitWindowPosition(0, 0)

# window name
wind = glutCreateWindow(b"Template")

glutDisplayFunc(showScreen)

glutMainLoop()
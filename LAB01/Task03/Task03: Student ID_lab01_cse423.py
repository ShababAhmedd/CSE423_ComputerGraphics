from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


# This function is used to draw lines.
def draw_lines():
    glBegin(GL_LINES)
#===========2===========#
    glColor3f(1.0, 0.0, 0.0)    # Colour = Red
    #--------horizontal_lines--------#
    glVertex2f(50, 100)
    glVertex2f(100, 100)

    glVertex2f(50, 200)
    glVertex2f(100, 200)

    glVertex2f(50, 300)
    glVertex2f(100, 300)
    #--------vertical_lines--------#
    glVertex2f(50, 100)
    glVertex2f(50, 200)

    glVertex2f(100, 200)
    glVertex2f(100, 300)

    print("2")

#===========0===========#
    glColor3f(0.0, 1.0, 0.0)  # Colour = Green
    # --------horizontal_lines--------#
    glVertex2f(150, 100)
    glVertex2f(200, 100)

    glVertex2f(150, 300)
    glVertex2f(200, 300)
    # --------vertical_lines--------#
    glVertex2f(150, 100)
    glVertex2f(150, 300)

    glVertex2f(200, 100)
    glVertex2f(200, 300)

    print("0")

#===========2===========#
    glColor3f(0.0, 0.0, 1.0)  # Colour = Blue
    # --------horizontal_lines--------#
    glVertex2f(250, 100)
    glVertex2f(300, 100)

    glVertex2f(250, 200)
    glVertex2f(300, 200)

    glVertex2f(250, 300)
    glVertex2f(300, 300)
    # --------vertical_lines--------#
    glVertex2f(250, 100)
    glVertex2f(250, 200)

    glVertex2f(300, 200)
    glVertex2f(300, 300)

    print("2")

#===========4===========#
    glColor3f(1.0, 1.0, 0.0)  # Colour = Yellow
    # --------horizontal_lines--------#
    glVertex2f(350, 200)
    glVertex2f(400, 200)
    #--------vertical_lines--------#
    glVertex2f(400, 100)
    glVertex2f(400, 300)
    # --------y=x--------#
    glVertex2f(350, 200)
    glVertex2f(400, 300)

    print("4")

#===========1===========#
    glColor3f(0.0, 1.0, 1.0)  # Colour = Cyan
    # --------vertical_lines--------#
    glVertex2f(500, 100)
    glVertex2f(500, 300)
    # --------y=x--------#
    glVertex2f(450, 250)
    glVertex2f(500, 300)

    print("1")

#===========0===========#
    glColor3f(1.0, 1.0, 1.0)  # Colour = White
    # --------horizontal_lines--------#
    glVertex2f(550, 100)
    glVertex2f(600, 100)

    glVertex2f(550, 300)
    glVertex2f(600, 300)
    # --------vertical_lines--------#
    glVertex2f(550, 100)
    glVertex2f(550, 300)

    glVertex2f(600, 100)
    glVertex2f(600, 300)

    print("0")

#===========3===========#
    glColor3f(1.0, 0.0, 1.0)  # Colour = Purple
    # --------horizontal_lines--------#
    glVertex2f(650, 100)
    glVertex2f(700, 100)

    glVertex2f(650, 200)
    glVertex2f(700, 200)

    glVertex2f(650, 300)
    glVertex2f(700, 300)
    # --------vertical_lines--------#
    glVertex2f(700, 100)
    glVertex2f(700, 300)

    print("3")

#===========7===========#
        # Colour = Rainbow
    # --------vertical_lines--------#
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(750, 300)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(800, 300)
    # --------y=x--------#
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(750, 100)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(800, 300)

    print("7")

    glEnd()


def iterate():
    glViewport(0, 0, 900, 400)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 900, 0.0, 400, 0.0, 1.0)
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
    # draw_lines function to draw lines.
    draw_lines()

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)

# Size of the window.
# Manipulating this value will let us change the size of the output widow.
glutInitWindowSize(900, 400)
glutInitWindowPosition(0, 0)

# window name
wind = glutCreateWindow(b"Task03: Student ID")

glutDisplayFunc(showScreen)

glutMainLoop()
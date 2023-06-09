import glfw
from OpenGL.GL import *
import numpy as np

gComposedM = np.identity(3)

# B
def render(T):
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    # draw cooridnate
    glBegin(GL_LINES)
    glColor3ub(255, 0, 0)
    glVertex2fv(np.array([0.,0.]))
    glVertex2fv(np.array([1.,0.]))
    glColor3ub(0, 255, 0)
    glVertex2fv(np.array([0.,0.]))
    glVertex2fv(np.array([0.,1.]))
    glEnd()
    # draw triangle
    glBegin(GL_TRIANGLES)
    glColor3ub(255, 255, 255)
    glVertex2fv( (T @ np.array([.0,.5,1.]))[:-1] )
    glVertex2fv( (T @ np.array([.0,.0,1.]))[:-1] )
    glVertex2fv( (T @ np.array([.5,.0,1.]))[:-1] )
    glEnd()

# C D
def key_callback(window, key, scancode, action, mods):
    global gComposedM
    if key == glfw.KEY_W:
        if action == glfw.PRESS or action == glfw.REPEAT:
            # print('press w')
            gComposedM = np.array([[1., 0., 0.],
                                    [0., 0.9, 0.],
                                    [0., 0., 1.]]) @ gComposedM
    elif key == glfw.KEY_E:
        if action == glfw.PRESS or action == glfw.REPEAT:
            # print('press e')
            gComposedM = np.array([[1., 0., 0.],
                                    [0., 1.1, 0.],
                                    [0., 0., 1.]]) @ gComposedM    
    elif key == glfw.KEY_S:
        if action == glfw.PRESS or action == glfw.REPEAT:
            # print('press s')
            th = np.pi / 18
            gComposedM =  np.array([[np.cos(th), -np.sin(th), 0.],
                                    [np.sin(th), np.cos(th), 0.],
                                    [0., 0., 1.]]) @ gComposedM
    elif key == glfw.KEY_D:
        if action == glfw.PRESS or action == glfw.REPEAT:
            # print('press d')
            th = -(np.pi / 18)
            gComposedM =  np.array([[np.cos(th), -np.sin(th), 0.],
                                    [np.sin(th), np.cos(th), 0.],
                                    [0., 0., 1.]]) @ gComposedM
    elif key == glfw.KEY_X:
        if action == glfw.PRESS or action == glfw.REPEAT:
            # print('press x')
            gComposedM = np.array([[1., 0., 0.1],
                                    [0., 1., 0.],
                                    [0., 0., 1.]]) @ gComposedM
    elif key == glfw.KEY_C:
        if action == glfw.PRESS or action == glfw.REPEAT:
            # print('press c')
            gComposedM = np.array([[1., 0., -0.1],
                                    [0., 1., 0.],
                                    [0., 0., 1.]]) @ gComposedM
    elif key == glfw.KEY_R:
        if action == glfw.PRESS or action == glfw.REPEAT:
            # print('press r')
            gComposedM = np.array([[-1., 0., 0.],
                                    [0., -1., 0.],
                                    [0., 0., 1.]]) @ gComposedM
    elif key == glfw.KEY_1:
        if action == glfw.PRESS or action == glfw.REPEAT:
            # print('press 1')
            gComposedM = np.identity(3)

def main():
    if not glfw.init():
        return
        # A
    window = glfw.create_window(480, 480, "2019011449", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.set_key_callback(window, key_callback)
    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        
        global gComposedM
        render(gComposedM)
        
        glfw.swap_buffers(window)
    
    glfw.terminate()

if __name__ == "__main__":
    main()
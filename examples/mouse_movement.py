import time

from python_input import Input, MouseButton

inp = Input()

while(not inp.get_key("q")):
    #Keyboard
    vel = inp.get_mouse_vel()
    print(inp.get_mouse_scroll())

    time.sleep(0.05)
import time

from python_input import Input, MouseButton

inp = Input()

while(not inp.get_key("q")):
    pos = inp.get_mouse_pos()
    vel = inp.get_mouse_vel()
    scroll = inp.get_mouse_scroll()

    print(f"{pos=:} {vel=:} {scroll=:}")

    time.sleep(0.05)
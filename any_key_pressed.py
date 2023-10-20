from python_input import Input, MouseButton

inp = Input()

while(not inp.get_key("q")):
    if(inp.any_key_pressed()):
        print(inp.get_all_pressed_keys())
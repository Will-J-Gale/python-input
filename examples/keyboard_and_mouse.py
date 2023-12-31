from python_input import Input, MouseButton

inp = Input()

while(not inp.get_key("q")):
    #Keyboard
    if inp.get_key("space"):
        print("Space pressed!")
    elif(inp.get_key_down("a")):
        print("A down")
    elif(inp.get_key_up("d")):
        print("D up")
    
    #Mouse
    if(inp.get_mouse(MouseButton.left)):
        print("Left pressed")
    elif(inp.get_mouse_down(MouseButton.middle)):
        print("Middle down")
    elif(inp.get_mouse_up(MouseButton.right)):
        print("Right up")
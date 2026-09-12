# Python-Input
Simple mouse and keyboard input for python.

## Usage - Buttons

```python
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
```

## Usage - Mouse movement
```python
from python_input import Input, MouseButton

inp = Input()

while(not inp.get_key("q")):   
    pos = inp.get_mouse_pos()
    vel = inp.get_mouse_vel()
    scroll = inp.get_mouse_scroll()

    print(f"{pos=:} {vel=:} {scroll=:}")
```

## Keys
Keys are the simple string representation of the keys.  
To list all available keyboard key strings use `print_available_keys`

```python
from python_input import Input, MouseButton

inp = Input()
inp.print_available_keys()

```

## Installing from source
```bash
uv init
uv build
uv pip install dist/python_input-<VERSION>.tar.gz
```



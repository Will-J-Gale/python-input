import atexit

from pynput import keyboard, mouse
from pynput.keyboard import Key, KeyCode
from pynput.keyboard._xorg import CHARS
from pynput.mouse import Button

class MouseButton:
    left = Button.left
    right = Button.right
    middle = Button.middle

class _KeyboardInput:
    def __init__(self):
        self._keyboard_listener = keyboard.Listener(
            on_press=self._on_key_press,
            on_release=self._on_key_release
        )

        self._chars = [char for char in CHARS]
        self._chars.extend([key.name for key in Key])
        char_states = {char:False for char in self._chars}
        
        self._keys_down = char_states.copy()
        self._keys_pressed = char_states.copy()
        self._keys_up = char_states.copy()

        self._keyboard_listener.start()
        self._key_pressed = False
        atexit.register(self._close)

    def print_available_keys(self):
        for key in self._chars:
            print(key)

    def _on_key_press(self, key):
        self._key_pressed = True
        keyCode = key.char if isinstance(key, KeyCode) else key._name_

        self._keys_pressed[keyCode] = True
        self._keys_down[keyCode] = True

    def _on_key_release(self, key):
        self._key_pressed = False
        keyCode = key.char if isinstance(key, KeyCode) else key._name_
        self._keys_pressed[keyCode] = False
        self._keys_up[keyCode] = True

    def get_key(self, key:str) -> bool:
        return self._keys_pressed[key]
        
    def get_key_down(self, key:str) -> bool:
        result = self._keys_down[key]
        self._keys_down[key] = False
        return result
        
    def get_key_up(self, key:str) -> bool:
        result = self._keys_up[key]
        self._keys_up[key] = False
        return result
        
    def any_key_pressed(self) -> bool:
        return self._key_pressed
    
    def get_all_pressed_keys(self):
        return [key for key, pressed in self._keys_pressed.items() if pressed]
    
    def _close(self):
        self._keyboard_listener.stop()
    
class _MouseInput:
    def __init__(self):
        self._mouse_listener = mouse.Listener(
            on_move=self._on_mouse_move,
            on_click=self._on_mouse_click,
            on_scroll=self._on_mouse_scroll
        )
        self._mouse_pressed = False
        self._mouse_position = (0,0)

        mouse_states = {
            MouseButton.left: False,
            MouseButton.right: False,
            MouseButton.middle: False,
        }

        self._mouse_buttons_down = mouse_states.copy()
        self._mouse_buttons_pressed = mouse_states.copy()
        self._mouse_buttons_up = mouse_states.copy()

        self._mouse_listener.start()
        atexit.register(self._close)

    
    def _on_mouse_move(self, x:int, y:int):
        self.mousePositon = (x, y)

    def _on_mouse_click(self, x:int, y:int, button:MouseButton, state:bool):
        self._mouse_pressed = state

        if(state):
            self._mouse_buttons_pressed[button] = True
            self._mouse_buttons_down[button] = True
        else:
            self._mouse_buttons_pressed[button] = False
            self._mouse_buttons_up[button] = True

    def _on_mouse_scroll(self, *args):
        pass

    def _close(self):
        self._mouse_listener.stop()

    def get_mouse_position(self) -> (int, int):
        return self._mouse_position
    
    def get_mouse(self, button:MouseButton) ->bool:
        return self._mouse_buttons_pressed[button]
    
    def get_mouse_down(self, button:MouseButton) -> bool:
        state = self._mouse_buttons_down[button]
        self._mouse_buttons_down[button] = False
        return state
    
    def get_mouse_up(self, button:MouseButton) -> bool:
        state = self._mouse_buttons_up[button]
        self._mouse_buttons_up[button] = False
        return state

class Input:
    def __init__(self):
        self._keyboard_input = _KeyboardInput() 
        self._mouse_input = _MouseInput()

        self.print_available_keys = self._keyboard_input.print_available_keys
        self.get_key = self._keyboard_input.get_key
        self.get_key_down = self._keyboard_input.get_key_down
        self.get_key_up = self._keyboard_input.get_key_up
        self.any_key_pressed = self._keyboard_input.any_key_pressed
        self.get_all_pressed_keys = self._keyboard_input.get_all_pressed_keys

        self.get_mouse = self._mouse_input.get_mouse
        self.get_mouse_down = self._mouse_input.get_mouse_down
        self.get_mouse_up = self._mouse_input.get_mouse_up
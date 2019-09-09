#! /usr/bin/env python3

import AH
from pynput.keyboard import Key, Listener, KeyCode

def on_press(key):
    check_key(key)

def on_release(key):
    if key == Key.esc:
        return False

def check_key(key):
    if key == KeyCode.from_char('4'):
        AH.main(60, 30)

    if key == KeyCode.from_char('5'):
        pkill -n

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
    
    



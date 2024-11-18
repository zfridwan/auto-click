import pyautogui
import time
import threading
from pynput import keyboard

# Global variables
clicking = False
interval = 0.1  # Default interval (seconds)

# Function to handle mouse clicking
def click_mouse():
    global clicking
    while clicking:
        pyautogui.click()
        time.sleep(interval)

# Start/Stop functions
def start_clicking():
    global clicking
    clicking = True
    threading.Thread(target=click_mouse).start()

def stop_clicking():
    global clicking
    clicking = False

# Keyboard hotkey handling
def on_press(key):
    try:
        if key.char == "s":  # Start clicking (press 's')
            start_clicking()
        elif key.char == "e":  # Stop clicking (press 'e')
            stop_clicking()
    except AttributeError:
        pass

def on_release(key):
    if key == keyboard.Key.esc:  # Stop the program (press 'ESC')
        stop_clicking()
        return False

# Main function
if __name__ == "__main__":
    print("Press 's' to start clicking, 'e' to stop, 'ESC' to exit.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

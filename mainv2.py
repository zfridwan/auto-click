import pyautogui
import threading
import time
import tkinter as tk
from tkinter import messagebox

# Global variables
clicking = False
interval = 0.1  # Default interval (in seconds)

# Function to handle clicking
def click_mouse():
    while clicking:
        pyautogui.click()
        time.sleep(interval)

# Start/Stop functions
def start_clicking():
    global clicking
    if clicking:
        return
    clicking = True
    threading.Thread(target=click_mouse, daemon=True).start()
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)

def stop_clicking():
    global clicking
    clicking = False
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)

# Function to set the click interval
def set_interval():
    global interval
    try:
        interval = float(interval_entry.get())
        if interval <= 0:
            raise ValueError("Interval must be positive.")
        messagebox.showinfo("Success", f"Click interval set to {interval} seconds.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid positive number.")

# Function to exit the application
def exit_application():
    global clicking
    clicking = False
    root.destroy()

# Create GUI
root = tk.Tk()
root.title("Auto-Clicker")
root.geometry("300x200")
root.resizable(False, False)

# GUI components
tk.Label(root, text="Click Interval (seconds):").pack(pady=5)
interval_entry = tk.Entry(root, width=10)
interval_entry.pack(pady=5)
interval_entry.insert(0, "0.1")  # Default value

set_button = tk.Button(root, text="Set Interval", command=set_interval)
set_button.pack(pady=5)

start_button = tk.Button(root, text="Start Clicking", command=start_clicking)
start_button.pack(pady=5)

stop_button = tk.Button(root, text="Stop Clicking", command=stop_clicking, state=tk.DISABLED)
stop_button.pack(pady=5)

exit_button = tk.Button(root, text="Exit", command=exit_application)
exit_button.pack(pady=5)

# Run the GUI event loop
root.mainloop()

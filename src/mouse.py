import pyautogui

# Mendapatkan posisi kursor mouse saat ini
pos = pyautogui.click(x=200, y=200)  # Klik kiri di posisi (200, 200)
pyautogui.rightClick()         # Klik kanan
pyautogui.middleClick()        # Klik tengah
print(f"Posisi mouse: {pos}")

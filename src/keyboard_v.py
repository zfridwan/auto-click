import tkinter as tk
import pyautogui
import pygetwindow as gw
import time

# Fungsi untuk mencari dan mengklik jendela berdasarkan nama
def klik_jendela_target(nama_jendela):
    # Mencari jendela berdasarkan nama
    for window in gw.getAllTitles():
        if nama_jendela.lower() in window.lower():
            jendela = gw.getWindowsWithTitle(window)[0]
            jendela.activate()  # Fokuskan jendela
            pyautogui.click(jendela.left + jendela.width // 2, jendela.top + jendela.height // 2)
            print(f"Fokus dan klik jendela: {window}")
            return True
    print("Jendela target tidak ditemukan!")
    return False

# Fungsi untuk menangani penekanan tombol
def tekan_tombol(tombol):
    target = target_jendela.get()  # Ambil nama aplikasi target
    if target:
        if klik_jendela_target(target):  # Fokuskan jendela target
            if tombol == 'Space':
                pyautogui.press('space')  # Simulasi tombol spasi
            else:
                # Mengirimkan input ke kolom teks atau bar pencarian di Chrome
                pyautogui.write(tombol.lower())  # Simulasi mengetik huruf
        else:
            print("Jendela target tidak ditemukan!")

# Fungsi untuk memilih jendela
def pilih_jendela():
    # Mendapatkan semua judul jendela yang terbuka
    jendela_list = gw.getAllTitles()
    
    if jendela_list:
        # Membuat jendela baru untuk memilih aplikasi
        pilih_window = tk.Toplevel()
        pilih_window.title("Pilih Aplikasi Target")
        pilih_window.geometry("300x200")

        def pilih(jendela):
            target_jendela.set(jendela)  # Menyimpan jendela yang dipilih
            pilih_window.destroy()  # Tutup jendela pemilihan
            print(f"Jendela yang dipilih: {jendela}")
            klik_jendela_target(jendela)  # Fokuskan jendela yang dipilih

        # Menampilkan tombol untuk setiap jendela terbuka
        for jendela in jendela_list:
            tk.Button(pilih_window, text=jendela, command=lambda j=jendela: pilih(j)).pack(pady=2)

# Membuat jendela utama
root = tk.Tk()
root.title("Keyboard Virtual")
root.geometry("400x300")

# Variable untuk menyimpan jendela target
target_jendela = tk.StringVar()

# Tombol untuk memilih aplikasi target
pilih_jendela_button = tk.Button(root, text="Pilih Aplikasi Target", command=pilih_jendela)
pilih_jendela_button.pack(pady=20)

# Daftar tombol keyboard
tombol_keyboard = [
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M'],
    ['Space']
]

# Membuat tombol-tombol di GUI
for baris, tombol_baris in enumerate(tombol_keyboard):
    frame = tk.Frame(root)
    frame.pack(pady=5)
    for tombol in tombol_baris:
        teks_tombol = ' ' if tombol == 'Space' else tombol
        perintah = lambda t=tombol: tekan_tombol(t)
        btn = tk.Button(
            frame,
            text=teks_tombol,
            width=5,
            height=2,
            command=perintah
        )
        btn.pack(side=tk.LEFT, padx=3)

# Menjalankan aplikasi
root.mainloop()

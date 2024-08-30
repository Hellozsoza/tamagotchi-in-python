import os
import threading
import time
import sys
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

path = os.path.dirname(os.path.abspath(__file__))

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(path)

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def openFile(file_name):
   script_dir = os.path.dirname(os.path.abspath(__file__))
   script_dir.replace('\\','/')
   file_path = os.path.join(script_dir, file_name)
   file_path.replace('\\','/')
   return file_path

window = Tk()
tamagotchiIco = openFile("tamagotchi.ico")
print(tamagotchiIco)
window.iconbitmap(tamagotchiIco)
window.title("Tamagotchi")
window.geometry("700x500")
window.configure(bg = "#753737")

running = True
closed = False
hunger = 0
text1 = f"Hunger: {hunger}/10"

def closeApp():
    global closed
    closed = True

window.protocol("WM_DELETE_WINDOW", closeApp)

def hungerHigher():
    global hunger, text1, running, closed
    while running:
        time.sleep(4.5)
        if hunger < 10 and not hunger < 0 and not closed:
            hunger += 1
            text1 = f"Hunger: {hunger}/10"
        elif not closed:
            text1 = "Your pet sadly died. 🪦"
            canvas.itemconfig(writtenText, text=text1)
            canvas.delete(image)
            canvas.itemconfig(yourPetText, text="You don't have a living pet")
            time.sleep(5)
            break
        else:
            text1 = "You killed your pet?! 🗡️"
            canvas.itemconfig(writtenText, text=text1)
            canvas.delete(image)
            canvas.itemconfig(yourPetText, text="You don't have a living pet")
            time.sleep(1.25)
            break
        canvas.itemconfig(writtenText, text=text1)
    window.quit()

def hungerLower():
    global hunger, text1
    if running and not closed:
        if hunger > 0:
            hunger -= 1
            text1 = f"Hunger: {hunger}/10"
        else:
            hunger -= 2
    canvas.itemconfig(writtenText, text=text1)

def start():
    thread = threading.Thread(target=hungerHigher)
    thread.start()

canvas = Canvas(
    window,
    bg = "#753737",
    height = 500,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
yourPetText = canvas.create_text(
    44.999999999999886,
    130.0,
    anchor="nw",
    text="Your Pet",
    fill="#FFFFFF",
    font=("Inter", 32 * -1)
)

button_image = PhotoImage(
    file=relative_to_assets("button.png"))
button = Button(
    image=button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: hungerLower(),
    relief="flat"
)
button.place(
    x=454.9999999999999,
    y=355.0,
    width=200.0,
    height=50.0
)

writtenText = canvas.create_text(
    289.9999999999999,
    50.0,
    anchor="nw",
    text=text1,
    fill="#FFFFFF",
    font=("Inter", 32 * -1)
)

image_image = PhotoImage(
    file=relative_to_assets("image.png"))
image = canvas.create_image(
    145.9999999999999,
    305.0,
    image=image_image
)

start()
window.resizable(False, False)
window.mainloop()
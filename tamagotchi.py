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
running1 = True
closed = False
thirstExited = False
hunger = 0
thirst = 0
text1 = f"Hunger: {hunger}/10"
text2 = f"Thirst: {thirst}/10"

def closeApp():
    global closed
    closed = True

window.protocol("WM_DELETE_WINDOW", closeApp)

def stopThirst():
    global running1
    running1 = False

def hungerHigher():
    global hunger, text1, running, closed, thirstExited, running1, thirst
    while running:
        if hunger < 10 and not hunger < 0 and not thirst < 0 and not closed:
            time.sleep(4.5)
            hunger += 1
            text1 = f"Hunger: {hunger}/10"
        elif not closed:
            text1 = "Your pet sadly died. 🪦"
            canvas.delete(thirstText)
            canvas.itemconfig(hungerText, text=text1)
            canvas.delete(image)
            canvas.itemconfig(yourPetText, text="You don't have a living pet")
            time.sleep(5)
            break
        else:
            text1 = "You killed your pet?! 🗡️"
            canvas.delete(thirstText)
            canvas.itemconfig(hungerText, text=text1)
            canvas.delete(image)
            canvas.itemconfig(yourPetText, text="You don't have a living pet")
            time.sleep(1.25)
            break
        canvas.itemconfig(hungerText, text=text1)
    stopThirst()
    while True:
        if not thirstExited:
            continue
        else:
            break
    window.quit()

def hungerLower():
    global hunger, text1, thirst
    if running and not closed:
        if hunger > 0 and not thirst < 0:
            hunger -= 1
            text1 = f"Hunger: {hunger}/10"
        else:
            hunger -= 2
    canvas.itemconfig(hungerText, text=text1)

def thirstHigher():
    global thirst, text1, text2, running, closed, thirstExited, running1
    while running1:
        if thirst < 10 and not thirst < 0 and not closed:
            time.sleep(4.5)
            thirst += 1
            text2 = f"Thirst: {thirst}/10"
            canvas.itemconfig(thirstText, text=text2)
        elif not closed:
            text1 = "Your pet sadly died. 🪦"
            canvas.delete(thirstText)
            canvas.itemconfig(hungerText, text=text1)
            canvas.delete(image)
            canvas.itemconfig(yourPetText, text="You don't have a living pet")
            time.sleep(5)
            break
        canvas.itemconfig(hungerText, text=text1)
    thirstExited = True

def thirstLower():
    global thirst, text2
    if running and not closed:
        if thirst > 0:
            thirst -= 1
            text2 = f"Thirst: {thirst}/10"
        else:
            thirst -= 2
    canvas.itemconfig(thirstText, text=text2)

def start():
    thread = threading.Thread(target=hungerHigher)
    thread1 = threading.Thread(target=thirstHigher)
    thread1.start()
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

button_image1 = PhotoImage(
    file=relative_to_assets("button1.png"))
button1 = Button(
    image=button_image1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: thirstLower(),
    relief="flat"
)
button1.place(
    x=454.9999999999999,
    y=280.0,
    width=200.0,
    height=50.0
)

hungerText = canvas.create_text(
    289.9999999999999,
    50.0,
    anchor="nw",
    text=text1,
    fill="#FFFFFF",
    font=("Inter", 32 * -1)
)

thirstText = canvas.create_text(
    289.9999999999999,
    125.0,
    anchor="nw",
    text=text2,
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
# Simple Number guessing game (GUI version)
# Reference: (tokyoedtech) https://www.youtube.com/c/TokyoEdTech/search?query=guessing%20game

import tkinter
import random
from PIL import ImageTk, Image


secret_num = random.randint(1, 20)


def check():

    # get the value from txt_guess
    guess = int(txt_guess.get())

    if guess < secret_num:
        msg = "Guessed too small"
    elif guess > secret_num:
        msg = "Guessed too high"
    elif guess == secret_num:
        msg = "Correct!"
    else:
        msg = "something went wrong..."

    # show the result
    lbl_result["text"] = msg

    # clear txt_guess
    txt_guess.delete(0, 5)


def reset():
    # pass
    # declare the global variable
    global secret_num
    # get a random number
    secret_num = random.randint(1, 20)
    # change the lbl_result text
    lbl_result["text"] = "Game reset, guess again!"


# create a root window
root = tkinter.Tk()

# change root window background color
root.configure(bg="white")

# change the title
root.title("Guess the number!")

# change the window size
root.geometry("450x290")
# create widgets
canvas = tkinter.Canvas(root, width=225, height=180)
canvas.pack(side="top")
img = ImageTk.PhotoImage(Image.open("brain_teaser.jpg"))
canvas.create_image(110, 90, image=img)

lbl_title = tkinter.Label(root, text="Welcome to the guessing game!", bg="white")
lbl_title.pack()
lbl_title.config(font=('Helvatical bold', 20))

lbl_result = tkinter.Label(root, text=" Good luck!", bg="white")
lbl_result.pack()
lbl_result.config(font=('Helvatical bold', 20))

btn_check = tkinter.Button(root, text="Check", fg="green", bg="white", command=check)
btn_check.pack(side="left", ipadx=30)
btn_check.config(font=('Helvatical bold', 20))

btn_reset = tkinter.Button(root, text="Reset", fg="red", bg="white", command=reset)
btn_reset.pack(side="right", ipadx=30)
btn_reset.config(font=('Helvatical bold', 20))

# change font of Entry to adjust its height
txt_guess = tkinter.Entry(root, width=5, font=('Helvatical bold', 20))
txt_guess.pack()

# start the main events loop
root.mainloop()
# root.destroy()

import random
import tkinter.messagebox
from tkinter import *
from tkinter.ttk import *


def fancy_string(s: str):
    """Return a formated str from a str."""
    r = ""
    for i in range(len(s)):
        r += s[i]
        if i != len(s) - 1:
            r += " "
    return r


def fancy_list(l: list):
    """Return a formated str from a string."""
    r = ""
    for i in range(len(l)):
        r += l[i]
        if i != len(l) - 1:
            r += " "
    return r


def callback_key(event):
    global letters_tried
    print(event)
    # We check the state so we're sure there is a word to guess
    if state.get() == "wait_for_input":
        print(event.char)
        l = event.char
        if l not in letters_tried:
            letters_tried.append(l)
            if l in word.get():
                temp_placeholder = ""
                for i in range(len(word.get())):
                    if word.get()[i] == l:
                        temp_placeholder += l
                    else:
                        temp_placeholder += word_placeholder.get()[i]
                word_placeholder.set(temp_placeholder)
                word_placeholder_displayed.set(fancy_string(temp_placeholder))
                print(word_placeholder.get())
            else:
                errors_left_intvar.set(errors_left_intvar.get() - 1)
                errors_left_strvar_displayed.set(str(errors_left_intvar.get()) + " errors left.")
                global photo
                global photo_label
                photo = PhotoImage(file=f"HangmanFig/Hangman_{6 - errors_left_intvar.get()+1}.gif")
                photo_label.configure(image=photo)
                print(word_placeholder.get())

            letters_tried_strvar.set("Letters tried: " + fancy_list(letters_tried))
        else:
            tkinter.messagebox.showwarning("Letter already guessed",
                                           "You've already guessed that letter. Please try again.")

        # FAILURE
        if errors_left_intvar.get() == 0:
            state.set("failed")
            print("failed")
            tkinter.messagebox.showinfo("Boooh!", f"You lost ! Your word was {word.get()}.")

        # WIN
        if "_" not in word_placeholder.get():
            state.set("won")
            tkinter.messagebox.showinfo("Congratulations!", "You won!")


def play():
    # Random selection of the word w1
    with open("list.txt", "r", encoding="utf-8") as rawfile:
        text = rawfile.read()
        words = text.split()
        word.set(words[random.randint(0, len(words) - 1)])

    # Creating placeholder word
    tmp = ""
    for i in range(len(word.get())):
        tmp += "_"
        # if i != len(word.get()) - 1:
        #     tmp += " "

    # We reset everything
    global photo
    global photo_label
    global letters_tried
    photo = PhotoImage(file=f"HangmanFig/Hangman_1.gif")
    photo_label.configure(image=photo)

    word_placeholder.set(tmp)
    word_placeholder_displayed.set(fancy_string(tmp))

    errors_left_intvar.set(6)
    errors_left_strvar_displayed.set("6 errors left.")

    letters_tried = []
    letters_tried_strvar.set("Letters tried: " + fancy_list(letters_tried))

    state.set("wait_for_input")


root = Tk()
root.title("Hangman")
root.config(bg='white')

# Now unused canvas
# can = Canvas(root)
# can.pack()

root.bind("<Key>", callback_key)

style = Style()
style.configure("TLabel", background="white", font=('Segoe UI', 10))

start_button = Button(root, text="Start", command=play)
quit_button = Button(root, text="Quit", command=quit)
start_button.pack()
quit_button.pack()

letters_tried = []

letters_tried_strvar = StringVar()
word_placeholder = StringVar()
word_placeholder_displayed = StringVar()
word = StringVar()
state = StringVar()

errors_left_intvar = IntVar()
errors_left_strvar_displayed = StringVar()

photo = PhotoImage(file="HangmanFig/Hangman_0.gif")
photo_label = Label(root, image=photo)

errors_left_label = Label(root, textvariable=errors_left_strvar_displayed)
placeholder_word_label = Label(root, textvariable=word_placeholder_displayed)
letters_tried_label = Label(root, textvariable=letters_tried_strvar)

photo_label.pack()
errors_left_label.pack()
placeholder_word_label.pack()
letters_tried_label.pack()

root.mainloop()

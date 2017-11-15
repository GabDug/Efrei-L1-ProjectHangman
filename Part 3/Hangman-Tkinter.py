import random
from tkinter import *


def fancy_list(l: list):
    """Return a formated str from a list."""
    r = ""
    for i in range(len(l)):
        r += l[i]
        if i != len(l) - 1:
            r += " "
    return r


def callback_key(event):
    global letters_tried
    print(event)
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
                print(word_placeholder.get())
            else:
                errors_left_intvar.set(errors_left_intvar.get() - 1)
                global photo
                global label_photo
                photo = PhotoImage(file=f"HangmanFig/Hangman_{6 - errors_left_intvar.get()+1}.gif")
                label_photo.configure(image=photo)
                print(word_placeholder.get())
        else:
            print("You've already guessed that letter. Try again.")

        # FAILURE
        if errors_left_intvar.get() == 0:
            state.set("failed")
            print("failed")
            # TODO exit and show failure

        # WIN
        if "_" not in word_placeholder.get():
            state.set("won")
            print("won")
            # TODO exit and show win


def play():
    # Random selection of the word w1
    with open("list.txt", "r", encoding="utf-8") as rawfile:
        text = rawfile.read()
        words = text.split()
        word.set(words[random.randint(0, len(words) - 1)])
        print(word.get())

    # Creating placeholder word
    tmp = ""
    for i in range(len(word.get())):
        tmp += "_"
        # if i != len(word.get()) - 1:
        #     tmp += " "
    word_placeholder.set(tmp)
    # toguess.set(word_placeholder.get())
    errors_left_intvar.set(6)

    # While there are unguessed letters, print the hang(wo)man and the previous guesses
    # while "_" in w2:
    # The lambda thing is just to remove the s when there is only one error left.
    # print(f"Letters you have guessed:\n {fancy_list(letters_tried)}")
    # print(
    #     f"You have the right to make up to {errors_left_intvar.get()} "
    #     f"error{(lambda x: 's' if (errors_left_intvar.get() != 1) else '' )(errors_left_intvar.get())}.\n"
    #     # f"{art[gender][-(errors_left_intvar.get()+1)]}"  # Corresponds to the right ASCII picture
    #     f"{fancy_list(w2)}")

    # If they are no errors left, break ; else ask a guess
    # if errors_left_intvar.get() == 0:
    #     return

    state.set("wait_for_input")

    # if "_" in word_placeholder.get():
    #     print(f"You lose! Booo\n"
    #           f"Your word was {word.get()}")
    # else:
    #     print("Yay! You win!")


root = Tk()
root.title("Hangman")

can = Canvas(root)
can.pack()

root.bind("<Key>", callback_key)

start_button = Button(can, text="Start", command=play)
start_button.pack()

gender = "man"
letters_tried = []

text_print = StringVar()
word_placeholder = StringVar()
word = StringVar()
state = StringVar()

# toguess = StringVar()
# toguess.set("_ _ _ _")

errors_left_intvar = IntVar()

photo = PhotoImage(file="HangmanFig/Hangman_1.gif")
label_photo = Label(can, image=photo)
label_photo.pack()
errors_left = Label(can, textvariable=errors_left_intvar)
toguess_tk = Label(can, textvariable=word_placeholder)
text_print = Label(can, textvariable=text_print)
errors_left.pack()
toguess_tk.pack()
text_print.pack()

root.mainloop()

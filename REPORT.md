![Project Hangman](https://raw.githubusercontent.com/SoFolichon/ProjectHangman/master/logo-project-hangman.png)
===============
*By Gabriel DUGNY and Vincent LACROUTS, Efrei Paris Promo 2022, November 2017.*


Introduction
------------
&nbsp;&nbsp;&nbsp;&nbsp;This program written in Python 3.6 allows the users to play the "Hangman" game, 
in a console or with a Tk graphical interface.


Presentation
------------
&nbsp;&nbsp;&nbsp;&nbsp;According to the sheet, the goal of the game is to guess a word, while your character on the screen is not
hung yet. 

For part 2, the non graphical game, we respected all the specifications:
* The user has to guess a random word, one letter at a time.
* The guess is not counted as one if the letter has already been guessed.
* If the letter is in the word, we show them in the placeholder word, instead of a "_".
* If the letter is not in the word, the user is warned that he was wrong, he loses a try, 
and his character gets closer to death...
* The user is able to choose between a male and female character.
* The user is asked if he wants to play again at the end of a round.

To do so, we used decided to use some functions that helps us, especially for displaying the lists as we want to.

For part 3, we created a GUI using Tkinter. We used a more event driven way of programming, as the program reacts to user input.



The different algorithms
------------------------
### Part 1 : Playing with strings
#### 3 - List of Words
##### 3. a)    
```python
l = ["Salut", "les", "amis", "Anticonstitutionnellement"]

for w in l:
    print(w[1:-1])
```
For this program we just print the different words from the second letter to the penultimate one, one after the other 
with a `for` loop.

##### 3. b)
```python
l = ["Salut", "les", "amis", "Anticonstitutionnellement"]
max_length = 0
pos = 0

for i in range(len(l)):
    if len(l[i]) > max_length:
        max_length = len(l[i])
        pos = i

print(f"Longest word is \"{l[pos]}\" at index {pos}.")
```
Here, we are searching for the longest word. We are comparing the length of each words with the previous length. 
To do so we're using an `if` condition in a `for` loop.

##### 3. c)
```python
l = ["amelie", "gérad", "parc zoologique", "zoo"]

l.sort()

print(l[-1])
```    
For this program we're sorting the array alphabetically by using the function `sort()`, then we show the last
string in the array (index -1).

##### 3. d) 
```python
l = ["Salut", "les", "amis", "Anticonstitutionnellement"]
l2 = []

for w in l:
    l2.append(len(w))

print(l)
print(l2)
```
In this program we're adding the length of each word in a second array by using a `for` loop.

##### 3. e)
```python
l = ["Salut", "les", "amis", "Anticonstitutionnellement"]
print(f"They are {len(l)} elements in the list :")
for w in l:
    print(w)
```
In this one we display the numbers of the elements of the array follow by the elements. 
We get get the length of the array with `len()` then we're printing all the array
by using a `for` loop.

##### 3. f)
```python
l = ["Salut", "les", "amis", "Anticonstitutionnellement", "salut", "salutations", "sAlUT"]

word_to_delete = "SALUT"
offset = 0

for i in range(len(l)):
    w = l[i + offset]
    if word_to_delete.lower() == w.lower():
        l.pop(i + offset)
        offset -= 1

print(l)
```
In this program, we delete all the occurences of a given word. We're defining the word to delete with `input()`
then we launch a `for` loop going through all the elements. With use an offset, to change the index when deleting
elements in the for loop. 


##### 3. g)

```python
l = ["Salut", "les", "$w_1$", "Anticonstitutionnellement"]
a = str(input("word to replace"))
b = str(input("word that replace"))

for i in range(len(l)):
    l[i] = l[i].replace(a, b)

print(l)
```
For this one we're asking the user what word does he want to replace and with which word by using `input()`.
Then we replace it in all the elements of the array by using a for loop of the length of the array.

##### 3. h)
```python
l = ["Salut", "les", "$w_1$", "Anticonstitutionnellement", "SALUT"]
l2 = []

word = input("Enter your word? ")

for i in range(len(l)):
    w = l[i]
    if word.lower() == w.lower():
        l2.append(i)

print(f"They are {len(l2)} occurences of {word} at index : {l2}")
```
For this program we're defining the word that we need to check the number of occurrence so we've created a `for` loop of 
the length of the array and we're doing an `if` to check in a lower version of the words and if it's same word we're adding
one to the number of occurrences.


#### 4 - Text files
##### 4. a)
```python
with open("list.txt", "r", encoding="utf-8") as rawfile:
    text = rawfile.read()
    words = text.split()
    text = text.replace('\n', '').replace('\r', '')
    char = len(text.replace('\n', '').replace('\r', ''))
    print(f"Number of words : {len(words)}\n"
          f"Number of characters : {len(text)}")
```           
In this program we're using the with statement close the file properly, then we read the text. We're using the function
`split()` to get the number of words and we replace the enters and spaces to get the number of characters with 
the `len()` function.


##### 4. b)
```python
with open("list.txt", "r", encoding="utf-8") as rawfile:
    text = rawfile.read()
    words = text.split()
    words_set = sorted(set(words))
    for w in words_set:
        print(f"{words.count(w)} {w}")
```    
In this program we're using the `with` statement to read the text file, as it will close the file properly on his own at 
the end of the `with`.
We're using the function `split()` to get all words and we sort them. 
Finally in the for loop that is doing all the different words of the list we print the number of occurrences.

##### 4. c)
```python
with open("list.txt", "r", encoding="utf-8") as rawfile:
    text = rawfile.read()
    text = text.upper()
    print(text)

    with open("list_upper.txt","w",encoding="utf-8") as rawfile_upper:
        rawfile_upper.write(text)
```
Here, we have to change the list to put all words uppercase.
For this program we're using the `with` statement again to read the text. Then we're using the 
function `upper()` to put the whole file in uppercase. Finally we write the text in an other file.


##### 4. d)
```python
with open("list.txt", "r", encoding="utf-8") as rawfile:
    text = rawfile.read()
    words = text.split()
    w1 = input("w1? ")

    for w2 in words:
        if w1.lower() in w2.lower():
            print(f"{w2}")
```       
For this program we're using the with statementtoo to read the file. Then we're using the 
function `lower()` . Finally we use the `in` keyword to find if the word w1 is in w2.

##### 4. e)
```python
import random

with open("list.txt", "r", encoding="utf-8") as rawfile:
    text = rawfile.read()
    words = text.split()

print(words[random.randint(0, len(words)-1)])
```
For this one we import the random class, then we're using the with statement to read the text.
Finally we print a random word by choosing a random int in the length of the number of words, 
and choosing the word associated with it in the list.

##### 4. f)
```python
import random

with open("list.txt", "r", encoding="utf-8") as rawfile:
    text = rawfile.read()
    words = text.split()

    w1 = words[random.randint(0, len(words) - 1)]

    l = input("Choose a letter: ")

    w2 = ""

    if l in w1:
        for i in range(len(w1)):
            if w1[i] == l:
                w2 += l
            else:
                w2 += "_"

        print(w2)
```   
Here we also use random and the `with` statement.
Then we choose a random word by choosing a random int in the length of the number of words. We input a str. Finally we create a w2 then 
we use a if to see if a letter is in the word and if it is, we print the word with "_" at the place of other letters.

### Part 2 : Hangman without GUI
```python
import os
import random

# NOTE :
# The formating we used, using f-strings requires Python 3.6+


art = {'man': ["  ______\n"
               "  |    |\n"
               "       |\n"
               "       |\n"
               "       |\n"
               "       |\n"
               "       |\n"
               "    ___|___\n",
               "  ______\n"
               "  |    |\n"
               " ( )   |\n"
               "       |\n"
               "       |\n"
               "       |\n"
               "       |\n"
               "    ___|___\n",
               "  ______\n"
               "  |    |\n"
               " ( )   |\n"
               "  |    |\n"
               "  |    |\n"
               "       |\n"
               "       |\n"
               "    ___|___\n",
               "  ______\n"
               "  |    |\n"
               " ( )   |\n"
               " /|    |\n"
               "/ |    |\n"
               "       |\n"
               "       |\n"
               "    ___|___\n",
               "  ______\n"
               "  |    |\n"
               " ( )   |\n"
               " /|\   |\n"
               "/ | \  |\n"
               "       |\n"
               "       |\n"
               "    ___|___\n",
               "  ______\n"
               "  |    |\n"
               " ( )   |\n"
               " /|\   |\n"
               "/ | \  |\n"
               " /     |\n"
               "/      |\n"
               "    ___|___\n",
               "  ______\n"
               "  |    |\n"
               " ( )   |\n"
               " /|\   |\n"
               "/ | \  |\n"
               " / \   |\n"
               "/   \  |\n"
               "    ___|___\n"
               ],
       'woman': ["  ______\n"
                 "  |    |\n"
                 "       |\n"
                 "       |\n"
                 "       |\n"
                 "       |\n"
                 "       |\n"
                 "       |\n"
                 "    ___|___\n",
                 "  ______\n"
                 "  |    |\n"
                 " { }   |\n"
                 "       |\n"
                 "       |\n"
                 "       |\n"
                 "       |\n"
                 "       |\n"
                 "    ___|___\n",
                 "  ______\n"
                 "  |    |\n"
                 " { }   |\n"
                 "  |    |\n"
                 "  |    |\n"
                 "       |\n"
                 "       |\n"
                 "       |\n"
                 "    ___|___\n",
                 "  ______\n"
                 "  |    |\n"
                 " { }   |\n"
                 " /|    |\n"
                 "/ |    |\n"
                 "       |\n"
                 "       |\n"
                 "       |\n"
                 "    ___|___\n",
                 "  ______\n"
                 "  |    |\n"
                 " { }   |\n"
                 " /|\   |\n"
                 "/ | \  |\n"
                 "       |\n"
                 "       |\n"
                 "       |\n"
                 "    ___|___\n",
                 "  ______\n"
                 "  |    |\n"
                 " { }   |\n"
                 " /|\   |\n"
                 "/ | \  |\n"
                 " / \   |\n"
                 "/---\  |\n"
                 " |     |\n"
                 "    ___|___\n",
                 "  ______\n"
                 "  |    |\n"
                 " { }   |\n"
                 " /|\   |\n"
                 "/ | \  |\n"
                 " / \   |\n"
                 "/---\  |\n"
                 " | |   |\n"
                 "    ___|___\n"
                 ]}


def clear():
    """Clear the screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def fancy_list(l: list):
    """Return a formated str from a string."""
    r = ""
    for i in range(len(l)):
        r += l[i]
        if i != len(l) - 1:
            r += " "
    return r


def choose_gender():
    gen = ""
    while gen != "man" and gen != "woman":
        choice = input("Do you want to be portrayed as a man ? [Y/n] ")
        no = ['no', 'n', 'non', 'woman', 'women']
        if choice in no:
            gen = 'woman'
        else:
            gen = 'man'
        return gen


gender = choose_gender()

# While the user wants to play
# (if the user wants to quit, break)
while True:
    # Random selection of the word w1
    with open("list.txt", "r", encoding="utf-8") as rawfile:
        text = rawfile.read()
        words = text.split()
        w1 = words[random.randint(0, len(words) - 1)]

    # Creating placeholder word w2
    w2 = ["_"] * len(w1)

    errors_left = 6
    letters_tried = []

    # While there are unguessed letters, print the hang(wo)man and the previous guesses
    while "_" in w2:
        clear()
        # The lambda thing is just to remove the s when there is only one error left.
        print(f"Letters you have guessed:\n {fancy_list(letters_tried)}")
        print(
            f"You have the right to make up to {errors_left} "
            f"error{(lambda x: 's' if (errors_left != 1) else '' )(errors_left)}.\n"
            f"{art[gender][-(errors_left+1)]}"  # Corresponds to the right ASCII picture
            f"{fancy_list(w2)}")

        # If they are no errors left, break ; else ask a guess
        if errors_left == 0:
            break

        # We want the input to be a single lowercase letter
        while True:
            l = input("Guess a letter: ")
            if len(l) != 1 or not l.isalpha():
                print("Please guess only ONE letter at a time!")
            else:
                break

        # If the letter has not already been guessed by the user...
        if l not in letters_tried:
            # Add it to the list of letters tried
            letters_tried.append(l)
            # Check if it's in the hidden word
            if l in w1:
                for i in range(len(w1)):
                    if w1[i] == l:
                        w2[i] = l
            else:
                errors_left -= 1
        else:
            print("You've already guessed that letter. Try again.")

    if "_" in w2:
        print(f"You lose! Booo\n"
              f"Your word was {w1}")
    else:
        print("Yay! You win!")

    playagain = None
    
    # We use a loop to be sure the user inputs something correct
    while playagain is None:
        choice = input("Do you want to play again ? [Y/n] ")
        no = ['no', 'n', 'non', 'quit', "quitter", "q"]
        if choice in no:
            playagain = False
        else:
            playagain = True

    if not playagain:
        break
```
The hangman without GUI is more or less like an addition of some of the previous programs (4.a/4.f). 
The main loop has no condition (```while True:```) but is not an infinite loop, as the user is able to choose a the end of a round if he
wants to play again or not. If he wants to quit, the ```break``` statement will stop the loop.

### Part 3 : Hangman with GUI
```python
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
```
The Hangman with the GUI has the sames bases as the other hangman but we had to it a few changes to allow it to work
with Tkinter.
    
Main difficulties encountered
-----------------------------
&nbsp;&nbsp;&nbsp;&nbsp;The difficulties were mostly during the passage from the simple Hangman to the hangman with the GUI, 
in fact the hardest parts were to change a part of our variables to transform it into ```IntVar()```/```StringVar()``` 
to get variable that change constantly according to the program and the displaying of the images.


Analysis
--------
&nbsp;&nbsp;&nbsp;&nbsp;In our opinion the project was really divided in 3 part the first one was pretty easy it remembered us the TP we add, 
then the Hangman forced us to think about a way of realising it and finally the GUI part that had aloud us to think even deeper.
But even if it had add some difficulties, the goal was easy to understand so it helped us a lot. 


Conclusion
----------
&nbsp;&nbsp;&nbsp;&nbsp;This project was very interesting even if we encountered some difficulties, it helped us to develop our level in Python 
and the last part made us rediscovered the Tkinter module. It helped us to improve our knowledge in Python, as well as our
ability to work in pairs and collaborate.
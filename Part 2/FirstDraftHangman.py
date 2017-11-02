import os
import random

# NOTE :
# The formating we used, using f-strings requires Python 3.6+
man = ["  ______\n"
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
       ]


def clear():
    """Clear the screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def fancy_list(l: list):
    """Return a fromated str from a string."""
    r = ""
    for i in range(len(l)):
        r += l[i]
        if i != len(l) - 1:
            r += " "
    return r


# Random selection of the word w1
with open("list.txt", "r", encoding="utf-8") as rawfile:
    text = rawfile.read()
    words = text.split()
    w1 = words[random.randint(0, len(words) - 1)]
    # print(w1)

# Creating placeholder word w2
w2 = ["_"] * len(w1)

errors_left = 6
letters_tried = []

# While there are unguessed letters and some tries
while "_" in w2 and errors_left > 0:
    clear()

    # Are they more than 1 error (do we need an s ?
    if errors_left !=1:
        plural_errors = "s"
    else:
        plural_errors = ""
    print(f"Letters you have guessed:\n {fancy_list(letters_tried)}")
    print(f"You have the right to make up to {errors_left} error{plural_errors}.\n"
          f"{man[-(errors_left+1)]}"
          f"{fancy_list(w2)}")

    # We want the input to be a single lowercase letter
    while True:
        l = input("Guess a letter: ")
        if len(l) != 1 or not l.isalpha():
            print("Please guess only ONE letter at a time!")
        else:
            break

    if l not in letters_tried:
        letters_tried.append(l)
        if l in w1:
            for i in range(len(w1)):
                if w1[i] == l:
                    w2[i] = l
                    # print(fancy_list(w2))
        else:
            errors_left -= 1

            # print(fancy_list(w2))
    else:
        print("You've already guessed that letter. Try again.")

if "_" in w2:
    print(f"You lose! Booo\n"
          f"Your word was {w1}")
else:
    print("Yay! You win!")

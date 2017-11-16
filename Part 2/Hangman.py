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
        # Add space after a character except if it's the last character
        if i != len(l) - 1:
            r += " "
    return r


def choose_gender():
    gen = ""
    while gen != "man" and gen != "woman":
        choice_gender = input("Do you want to be portrayed as a man ? [Y/n] ")
        choice_no = ['no', 'n', 'non', 'woman', 'women']
        if choice_gender in choice_no:
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

        if l not in letters_tried:
            letters_tried.append(l)
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

    while playagain is None:
        choice = input("Do you want to play again ? [Y/n] ")
        no = ['no', 'n', 'non', 'quit', "quitter", "q"]
        if choice in no:
            playagain = False
        else:
            playagain = True

    if not playagain:
        break

![Project Hangman](logo-project-hangman.png)
===============
*By Gabriel DUGNY and Vincent LACROUTS, Efrei Paris Promo 2022, November 2017.*


Introduction
------------
This program written in Python 3.6 allows the users to play the "Hangman" game, 
in a console or with a Tk graphical interface.


Presentation
------------
According to the sheet, the goal of the game is to guess a word, while your character on the screen is not
hung yet. 

For part 2, the non graphical game, we respected all the specifications:
- The user has to guess a random word, one letter at a time.
- The guess is not counted as one if the letter has already been guessed.
- If the letter is in the word, we show them in the placeholder word, instead of a "_".
- If the letter is not in the word, the user is warned that he was wrong, he loses a try, 
and his character gets closer to death...
- The user is able to choose between a male and female character.
- The user is asked if he wants to play again at the end of a round.

To do so, we used decided to use some functions.

For part 3, we created a GUI using Tkinter. We used a more event driven way of programming.


The different algorithms
------------------------

####Part 1
3. a)    


     l = ["Salut", "les", "amis", "Anticonstitutionnellement"]
     
     for w in l:
     print(w[1:-1])
     
For this program we just print the differents words from the second letter to the penultimate on after  the other whith a for loop

3. b)

    
    l = ["Salut", "les", "amis", "Anticonstitutionnellement"]
    max_length = 0
    pos = 0
    
    for i in range(len(l)):
        if len(l[i]) > max_length:
            max_length = len(l[i])
            pos = i
    
    print(f"Longest word is \"{l[pos]}\" at index {pos}.")

For this one we are classing the lenth of the differents words by comparing thoses
to do so wwe're using an if in a for loop

3. c)


    l = ["amelie", "gérad", "parc zoologique", "zoo"]
    
    l.sort()
    
    print(l[-1])
    
For this program we're sorting the array by usinge the function sort, the we're showing the last
string  in the array

3. d) 


    l = ["Salut", "les", "amis", "Anticonstitutionnellement"]
    l2 = []
    
    for w in l:
        l2.append(len(w))
    
    print(l)
    print(l2)
    
    
In this program we're adding the length of all the word in a second array by using a for loop

3. e)

     
    l = ["Salut", "les", "amis", "Anticonstitutionnellement"]
    print(f"They are {len(l)} elements in the list :")
    for w in l:
        print(w)
        
In this one we're using the print (f ) to get the length of the array in the print, then we're printing all the array
by using a for loop

3. f)


    l = ["Salut", "les", "amis", "Anticonstitutionnellement", "salut", "salutations", "sAlUT"]
    
    word_to_delete = "SALUT"
    offset = 0
    
    for i in range(len(l)):
        w = l[i + offset]
        if word_to_delete.lower() == w.lower():
            l.pop(i + offset)
            offset -= 1
    
    print(l)
    
    
For this program we're defining the word to delete then we've created a for loop of the length of the array and we're 
doing an if to check in a lower version of the words and if it's same word we're deleting it


    
1. g)


3. h)


    l = ["Salut", "les", "$w_1$", "Anticonstitutionnellement", "SALUT"]
    l2 = []
    
    word = input("Enter your word? ")
    
    for i in range(len(l)):
        w = l[i]
        if word.lower() == w.lower():
            l2.append(i)
    
    print(f"They are {len(l2)} occurences of {word} at index : {l2}")
    
    
For this program we're defining the word that we need to check the number of occurrence so we've created a for loop of 
the length of the array and we're doing an if to check in a lower version of the words and if it's same word we're adding
one to the number of occurrences


####Part 2

4. a)
    
Main difficulties encountered
-----------------------------


Analysis
--------


Conclusion
----------


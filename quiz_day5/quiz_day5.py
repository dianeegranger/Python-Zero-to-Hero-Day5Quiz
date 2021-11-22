#!/usr/bin/env python
# coding: utf-8

# November 22, 2021<br/>
# <br/>
# Diane Granger<br/>
# dianeegranger@gmail.com<br/>
# <br/>
# Quiz Day 5<br/>
# Python Essentials Zero to Hero<br/>
# LetsUpgrade<br/>
# <br/>
# Instructor:  Kamal Seth<br/>

# In[5]:


def wordguess():
    
    import os
    import random

    words = ['toys', 'red', 'green', 'Christmas', 'Santa', 'gingerbread', 'gifts', 'shopping', 'wreath', 'holly']
    words = [each_string.lower() for each_string in words]

    word = random.choice(words)
    select = random.choice(word)

    guess = ''



    while True:
        name = input("Please enter your name: ")
        guess = input("Please guess a word: ")
   
        if guess.lower() == word:
            print("Great guess!!!", guess.lower(), "is the randomly chosen word from the word list.")
            print("Thank you for playing.")
            break

        elif guess.lower() != word:
            print(guess.lower(), "is not the randomly chosen word.  Please guess again.\n")

wordguess()


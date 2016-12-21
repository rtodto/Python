#!/usr/bin/env python

import sys
import time
import os
import platform
from random import randint

#List of games
games = ['Dice Rolling', 'Guess the Number', 'Hangman']
#Only used for hangman
hangman_list = ['Amsterdam', 'Berlin','Ankara', 'Prague', 'Paris']
hangman_category = "Cities"

def roll_dice():
  """Rolls two dices"""
  return randint(1,6), randint(1,6)

def guess_number(user_number):
  """Guess the number computer generates between 1 and 10"""

  computer_number = randint(1,10)
  attempt = 0
  #print 'Computer number is %d' % computer_number
  while user_number != computer_number:
      print "Sorry, your guess is incorrect!"
      user_number = int(raw_input("Try again> "))
      attempt += 1

  print "Congratulations you have guessed the number after %d attempt" % attempt

def list_games():
  """This function lists the games"""

  print '*' * 20
  #List the games
  for index,game in enumerate(games):
    print index,game
  print '*' * 20
  choice = int(raw_input("Enter the game number#> "))
  run_game(choice)

def hangman():
    number_of_attempts = 5
    """Find the words in the list"""
    clear_screen()
    print '\nCategory of our game is : %s\n\
You have %d attempts to find the word\n\
Number of words in the game : %d \n'\
           % (hangman_category, number_of_attempts, len(hangman_list))
    #lower all items in the list
    hangman_list_lower = [ hang_item.lower() for hang_item in hangman_list ]
    #pick the items in the list and play the game
    for index,hang_word in enumerate(hangman_list_lower):
        print 'Word #%d has %d letters' % (index + 1, len(hang_word))
        guessed_word = ['_'] * len(hang_word)
        incorrect_guess = 0
        while incorrect_guess < number_of_attempts:
          guess_letter = raw_input('\nWhat is your letter of guess? #'\
          + str(number_of_attempts - incorrect_guess)+ ' attempts left > ')
          #if a letter is re-typed, increase incorrect counter again
          #as we are cruel
          if guess_letter in guessed_word:
              print 'You already guessed this letter'
              incorrect_guess += 1
              continue #we stop executing the rest of the while loop

          if guess_letter in hang_word:
              #find indexes of the guessed letter in the word.
              letter_indexes = [ ind for ind,letter in enumerate(hang_word) if letter == guess_letter]
              print "we have found %d letters and here is now how it looks:  " \
                     % len(letter_indexes)
              for k in letter_indexes: #assign the letters to their positions
                guessed_word[k] = guess_letter
              g_to_str = ' '.join(guessed_word)
              print g_to_str
              if '_' not in g_to_str:
                print "You have found all letters, congratulations!\n"
                do_delay()
                clear_screen()
                break
          else:
              print "Letter %s doesn't exist in this word!!!" % guess_letter
              incorrect_guess += 1
              if incorrect_guess == number_of_attempts:
                  print 'Sorry, you have failed on this world, 5 seconds to the next word\n'
                  do_delay()
                  clear_screen()

def do_delay():
    '''Delay the execution'''
    for i in range(5,1,-1):
        print '%d\r' %i,
        sys.stdout.flush()
        time.sleep(1)

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    elif platform.system() == "Linux":
        os.system('clear')
    else:
        print 'Unknown OS'
        pass

def replay(choice):
    """Replays the game if requested"""
    if choice in 'yY':
      run_game(choice)
    else:
      list_games()

def run_game(choice):
   """Execute the game requested"""

   if choice == 0: #roll dice
     dice1, dice2 = roll_dice()
     print dice1,dice2
     choice = raw_input("You want to play again? (y/n) ")
     replay(choice)
   elif choice == 1: #guess number
     user_number = int(raw_input("What is your guess from 1 to 10> "))
     guess_number(user_number)
   elif choice == 2: #hangman game
     hangman()
   else:
       print 'Invalid option, have no idea how you typed that.'


#List the games first here.
list_games()


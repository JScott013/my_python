"""This is a rock paper scissors game. I am writing now to justify the term mulitline comment and make all of those quotation marks work for a living!"""

from random import randint
from time import sleep

options = ["R", "P", "S"]
lose_msg = "You lost!"
win_msg = "You win!"

def decide_winner(user_choice, computer_choice):
  print "Your selection: %s" % user_choice
  print "Computer selecting..."
  sleep(1)
  print "The computer's choice: %s" % computer_choice
  user_choice_index = options.index(user_choice)
  computer_choice_index = options.index(computer_choice)
  if user_choice_index == computer_choice_index:
    print "It's a tie!"
  elif user_choice_index == 0 and computer_choice_index == 2:
    print win_msg
  elif user_choice_index == 1 and computer_choice_index == 0:
    print win_msg
  elif user_choice_index == 2 and computer_choice_index == 1:
    print win_msg
  elif user_choice_index >2:
    print "Invalid Choice!"
    return
  else:
    print lose_msg
    
def play_RPS():
  print "Rock, Paper, Scissors"
  user_choice = raw_input("Select R for rock, P for Paper, or S for scissors\n").upper()
  sleep(1)
  #computer_choice = options [randint(0,2)]
  computer_choice =  options [randint(0, len(options)-1)]
  decide_winner(user_choice, computer_choice)

play_RPS()

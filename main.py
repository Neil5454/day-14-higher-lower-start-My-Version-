##Unable to continuosly swap compare a with compare b
# from art import logo
from art import vs
from game_data import data
import random
import os

items_game_data = len(data)

def play_game():
  current_score = 0
  while True:
    choice_a = random.randint(0, items_game_data)
    choice_b = random.randint(0, items_game_data)
    print(data[choice_a]["follower_count"])
    print(data[choice_b]["follower_count"])
    print("Compare A: " + data[choice_a]["name"]+", a " + data[choice_a]["description"]+", from " + data[choice_a]["country"]+".")
    # print(vs)
    print("Compare B: " + data[choice_b]["name"]+", a " + data[choice_b]["description"]+", from " + data[choice_b]["country"]+".")
    choice_a_follower_count = data[choice_a]["follower_count"]
    choice_b_follower_count = data[choice_b]["follower_count"]
    if choice_a_follower_count > choice_b_follower_count:
      answer = "A"
    else:
      answer = "B"
    guess = input("Who has more followers? Type 'A' or 'B'. ").upper()
    if guess == answer:
      current_score += 1
      os.system('clear')
      print(f"You're right.  Current score: {current_score}.")
    else:
      print("Sorry, that's wrong. Final score: 0")
      break

play_game()
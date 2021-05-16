import random
from art import logo
import os
# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.


def deal_card():
    """"Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(card_list):
    """"Take a list of cards and pass the score"""
    cards_value = sum(card_list)
    if cards_value > 21:
        for i in range(0, len(card_list)):
            if card_list[i] == 11:
                card_list[i] = 1
        cards_value = sum(card_list)
    if cards_value == 21 and len(card_list) == 2:
        return 0
    return cards_value

def compare(user_score,computer_score):
  if user_score == computer_score:
    return "Draw"
  elif computer_score == 0:
    return "Lose, opponent has a Blackajack 😱"
  elif user_score == 0:
    return "Win with a blackjack. 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win. 😊  " 
  elif user_score > computer_score:
    return "You win 😀 "
  else:
    return "You lose 😢 "


def play_game():
  print(logo)
  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
      user_cards.append(deal_card())
      computer_cards.append(deal_card())

  while not is_game_over:
      user_score = calculate_score(user_cards)
      computer_score = calculate_score(computer_cards)
      print(f"  Your cards: {user_cards}, current_score: {user_score}")
      print(f"  Computer's first card : {computer_cards[0]}")
      if user_score == 0 or computer_score == 0 or user_score > 21:
          is_game_over = True
      else:
          user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
          if user_should_deal == "y":
              user_cards.append(deal_card())
          else:
              is_game_over = True


  # Hint 6: Create a function called calculate_score() that takes a List of cards as input
  # and returns the score.
  # Look up the sum() function to help you do this.

  while computer_cards != 0 and computer_score < 17:
      computer_cards.append(deal_card())
      computer_score = calculate_score(computer_cards)

  print(f"  Your final hand: {user_cards}, final score: {user_score}")
  print(f"  Computer's final hand is :{computer_cards}, final score: {computer_score} " )
  print(compare(user_score,computer_score))

while input("Do you want to paly a game of blackjack? Type 'y' or 'n': ") == "y":
  os.system('clear')
  play_game()
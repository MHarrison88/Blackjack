############### Blackjack Project #####################

#SELF NOTES: Overcomplicated things when i didnt have to at first. tried to pass multiple things at once and do several calculations
# need to learn to do one step at a time instead of combining multiple things.

############### Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import art
import random
restart = True
 
def deal_cards():
  #Select a random card and add it to the card list
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calc_score(card_list):
  #Calculate the score of a card list.
  if sum(card_list) == 21 and len(card_list) == 2:
    return 0

  #Alter the ace (11) if score is above 21
  if 11 in card_list and sum(card_list) > 21:
    card_list.remove(11)
    card_list.append(1)

  return sum(card_list)

def compare(p_score, a_score):
  #Win logic
  if p_score == a_score:
    return "It is a tie."
  elif a_score == 0:
    return "The computer has a Blackjack, you lose..."
  elif p_score == 0:
    return "You have a Blackjack, you win!"
  elif p_score > 21:
    return "Your score is over 21, you lose..."
  elif a_score > 21:
    return "The computer went over 21, you win!"
  elif p_score > a_score:
    return "You win!"
  else:
    return "You lose..."

def play():
  print(art.logo)
  player_hand = []
  player_score = 0
  ai_hand = []
  ai_score = 0
  game = True

#Starting two cards
  player_hand.append(deal_cards())
  player_hand.append(deal_cards())
  ai_hand.append(deal_cards())
  ai_hand.append(deal_cards())

  while game:
    player_score = calc_score(player_hand)
    ai_score = calc_score(ai_hand)
    print(f"You're cards are {player_hand} and current score is {player_score}")
    print(f"Dealer's first card is {ai_hand[0]}")

    if player_score > 21 or player_score == 0 or ai_score == 0:
      game = False
    else:
      cont = input("Would you like to draw another card? 'Y' or 'n': \n").lower()

      if cont == "y":
        player_hand.append(deal_cards())
      else:
        game = False

  while ai_score > 0 and ai_score < 17:
    ai_hand.append(deal_cards())
    ai_score = calc_score(ai_hand)

  print(f"Your final hand is {player_hand} and final score is {player_score}")
  print(f"Computer's final hand is {ai_hand} and final score is {ai_score}")
  print(compare(player_score, ai_score))

while restart:
  res = input("Would you like to play? Y or n: ").lower()
  if res == "y":
    play()
  else:
    restart == False
    break
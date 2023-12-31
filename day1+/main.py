import random

def deal():
    cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]
    card = random.choice(cards)
    return card

def calculate(player_cards):
    if sum(player_cards) == 21 and len(player_cards) == 2:
        return 0
    elif sum(player_cards) > 21 and 11 in player_cards:
        player_cards.remove(11)
        player_cards.append(1)
    return sum(player_cards)

def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    print("You went over. You lose 😤")
  if user_score == computer_score:
    print("Draw 🙃")
  elif user_score > 21:
    print("You went over. You lose 😭")
  elif computer_score > 21:
    print("Opponent went over. You win 😁")
  elif user_score > computer_score:
    print("You win 😃")
  else:
    print("You lose 😤")

def computer_turn(computer,computer1,computer2):
    print(f"computer's cards are {computer1,computer2}")
    is_done = False
    while is_done == False:
        score = calculate(computer)
        if score < 17:
            card = deal()
            computer.append(card)
            print(f"computer has drawn {card}")
        else:
            return score
            is_done = True


player = []
computer = []
is_donee = False
while is_donee == False:
    player1 = deal()
    player2 = deal()
    computer1 = deal()
    computer2 = deal()
    player.append(player1)
    player.append(player2)
    player_score = calculate(player)
    computer.append(computer1)
    computer.append(computer2)
    computer_score = calculate(computer)
    if computer_score == 0:
        print("Lose, opponent has Blackjack 😱")
    elif player_score == 0:
        print("Win with a Blackjack 😎")
    else:
        player_turn = True
        while player_turn == True:
            print(f"You have drawn {player1,player2}\ncomputer's first card is {computer1}")
            draw = input("type 'y' if you would like to draw another card and 'n' if you do not want to do so: ")
            if draw == "y":
                cardd = deal()
                player.append(cardd)
                score = calculate(player)
                if score > 21:
                    print(f"you have drawn {cardd} score has exceeded 21\ncomputer's cards were {computer1,computer2}\nYou Lose!")
                    player_turn = False
                    is_donee = True
                else:
                    print(f"you have drawn {cardd}")
            if draw == "n":
                score = calculate(player)
                computer_score = computer_turn(computer,computer1,computer2)
                compare(score,computer_score)
                player_turn = False
                is_donee = True








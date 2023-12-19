player_turn = input("What do you choose? 0 for rock, 1 for scissors, 2 for paper")
import random
random = str(random.randint(0,2))
listing = ['rock', 'scissors', 'paper']
print('computer choose '+listing[int(random)])
if int(player_turn)>=3 or int(player_turn)<0:
    print('You typed an invalid number, you lose!')
elif player_turn == random:
    print('Tie')
elif player_turn == '0' and random == '1':
    print('You win')
elif player_turn == '1' and random == '2':
    print('You win')
elif player_turn == '2' and random == '0':
    print('You win')
else:
    print('You lose')
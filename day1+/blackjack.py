import random
number = random.randint(1,101)

def guess(number,lives):
  guesses = int(input(f"You have {lives[0]} attempts remaining to guess the number.\nMake a guess: "))
  if guesses != number:
    lives[0] -= 1
    if guesses > number:
      print("Too high.\nGuess again.")
    elif guesses < number:
      print("Too low.\nGuess again.")
  elif guesses == number:
    print("Your guess is correct")
    global is_done
    is_done = True
  return lives


print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' of 'hard': ")
is_done = False
if difficulty == 'easy':
  lives = [10]
else:
  lives = [5]
while not is_done and lives[0] >0:
  guess(number, lives)
  if lives[0] == 0:
    print("You have no lives left, you lose")







import random

topNum = int(input("What is the top limit? "))

def random_num(int):
  return random.randint(1, int)

answer = random_num(topNum)

print(answer)

guess_count = 0

while guess_count < 3:
  guess_count += 1
  guess = int(input("What's your guess? "))

  if guess != answer and guess_count < 3:
    print("Nope!")
  elif guess != answer and guess_count == 3:
    print("You lose! The answer was {}.".format(answer))
  else:
    print("You win!")
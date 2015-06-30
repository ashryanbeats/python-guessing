import random

topNum = int(input("What is the top limit? "))

def random_num(int):
  return random.randint(1, int)

answer = random_num(topNum)

print(answer)

guess = int(input("What's your guess? "))

if guess != answer:
  print("You lose!")
else:
  print("You win!")
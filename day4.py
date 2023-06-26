rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

player = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer = random.randint(0, 2)
image = [rock, paper, scissors]
# 0 = draw
# 1 = player win
# 2 = computer win
win_matrix = [[0, 2, 1], [1, 0, 2], [2, 1, 0]]
result = win_matrix[player][computer]
print(image[player])
print("Computer chose: ")
print(image[computer])

if result == 1:
  print("You win!")
elif result == 2:
  print("You loose")
else:
  print("Draw")

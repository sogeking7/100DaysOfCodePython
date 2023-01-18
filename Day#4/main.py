import random

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

rps = [rock, paper, scissors]

you = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
computer = random.randint(0, 2)

print(you)
print(rps[you])
print("Computer chose:")
print(rps[computer])

if (you == computer):
    print("Draw")
elif ((you == 0 and computer == 2)):
    print ("You win!")
elif ((you == 1 and computer == 0)):
    print("You win!")
elif ((you == 2 and computer == 1)):
    print("You win!")
else:
    print("You lose")
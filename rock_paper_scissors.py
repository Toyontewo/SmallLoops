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
game_img = [rock, paper, scissors]
user_choice = int(input("What do you choose?\n0. Rock\n1. Paper\n2. Scissors\n"))

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you loose!")
else:
    print(game_img[user_choice])

    comp_choice = random.randint(0, 2)
    print("Computer choose: ")
    print(game_img[comp_choice])

    if user_choice == 0 and comp_choice == 2:
        print("You win")
    elif comp_choice == 0 and user_choice == 2:
        print("You loose")
    elif comp_choice > user_choice:
        print("You lose")
    elif user_choice > comp_choice:
        print("You win")
    elif comp_choice == user_choice:
        print("It's a draw")

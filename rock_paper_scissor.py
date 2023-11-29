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
print("******Welcome to play rock paper scissor game******")
game_images = [rock,paper, scissors]
choice = int(input("what do you want to choose, 0 for rock, 1 for paper, 2 for scissor : \n"))

computer_choice = random.randint(0,2)

if choice >= 3 or choice < 0:
    print("Please enter valid number 0 ,1 ,2")
else:
    if choice == 0 and computer_choice == 2:
        print(game_images[choice])
        print(f"Computer had choose {computer_choice}")
        print(game_images[computer_choice])
        print("****You win****")
    elif choice == 1 and computer_choice == 0:
        print(game_images[choice])
        print(f"Computer had choose {computer_choice}")
        print(game_images[computer_choice])
        print("****You win****")
    elif choice == 2 and computer_choice == 1:
        print(game_images[choice])
        print(f"Computer had choose {computer_choice}")
        print(game_images[computer_choice])
        print("****You win****")
    elif choice == computer_choice:
        print(game_images[choice])
        print(f"Computer had choose {computer_choice}")
        print(game_images[computer_choice])
        print("***Its a tie.***")
    else:
        print(game_images[choice])
        print(f"Computer had choose {computer_choice}")
        print(game_images[computer_choice])
        print("You loss the game.")

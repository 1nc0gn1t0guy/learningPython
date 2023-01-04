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

value = random.randint(0,2)

computer_choice = [rock, paper, scissors]

user_choice = input("Choose your weapon (rock, paper, scissors): ")

if value == 0 and user_choice == "rock":
    print(f"You chose {computer_choice[0]} and computer chose {computer_choice[value]} so it's a draw!")

elif value == 1 and user_choice == "rock":
    print(f"You chose {computer_choice[0]} and computer chose {computer_choice[value]} so you lose!")

elif value == 2 and user_choice == "rock":
    print(f"You chose {computer_choice[0]} and computer chose {computer_choice[value]} so you win!")

elif value == 0 and user_choice == "paper":
    print(f"You chose {computer_choice[1]} and computer chose {computer_choice[value]} so you win!")

elif value == 1 and user_choice == "paper":
    print(f"You chose {computer_choice[1]} and computer chose {computer_choice[value]} so it's a draw!")

elif value == 2 and user_choice == "paper":
    print(f"You chose {computer_choice[1]} and computer chose {computer_choice[value]} so you lose!")

elif value == 0 and user_choice == "scissors":
    print(f"You chose {computer_choice[2]} and computer chose {computer_choice[value]} so you lose!")

elif value == 1 and user_choice == "scissors":
    print(f"You chose {computer_choice[2]} and computer chose {computer_choice[value]} so you win!")

elif value == 2 and user_choice == "scissors":
    print(f"You chose {computer_choice[2]} and computer chose {computer_choice[value]} so it's a draw!")

else:
    print("Please write a valid value.")
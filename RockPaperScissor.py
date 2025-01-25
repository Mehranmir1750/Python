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

image = [rock,paper,scissors]

choice =int(input("choose your choice? 0->rock 1->paper 2->scissor "))
computer_choice = random.randint(0,2)

print(image[computer_choice])

if choice == computer_choice:
    print("draw")
elif choice == 0 and computer_choice ==1:
    print("you lost!")
elif choice == 0 and computer_choice ==2:
    print("you won!")
elif choice == 1 and computer_choice ==0:
    print("you won!")
elif choice == 2 and computer_choice ==0:
    print("you lost!")
elif choice == 1 and computer_choice ==2:
    print("you lost!")
elif choice == 2 and computer_choice ==1:
    print("you won!")
else:
    print("invalid choice")






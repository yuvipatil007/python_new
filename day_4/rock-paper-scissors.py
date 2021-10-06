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

you_choice=int(input("what do you choose? Type 0 for ROck, 1 for Paper or 2 for scissors"))
computer_option=[0,1,2]
computer_choice=random.choice(computer_option)

if you_choice==0 and computer_choice==2:
  print("computer choice \n")
  print(scissors)
  print("you choice \n")
  print(rock)
  print("you win") 
elif you_choice==0 and computer_choice==1:
  print("computer choice \n")
  print(paper)
  print("you choice \n")
  print(rock)
  print("you loose")
elif you_choice==0 and computer_choice==0:
  print("computer choice \n")
  print(rock)
  print("you choice \n")
  print(rock)
  print("you are equal")  
elif you_choice==1 and computer_choice==0:
  print("computer choice \n")
  print(rock)
  print("you choice \n")
  print(paper)
  print("you are win")
elif you_choice==2 and computer_choice==1:
  print("computer choice \n")
  print(paper)
  print("you choice \n")
  print(scissors)
  print("you are win")
elif you_choice==1 and computer_choice==1:
  print("computer choice \n")
  print(paper)
  print("you choice \n")
  print(paper)
  print("you are equal")
elif you_choice==2 and computer_choice==1:
  print("computer choice \n")
  print(paper)
  print("you choice \n")
  print(scissors)
  print("you win")
elif you_choice==2 and computer_choice==0:
  print("computer choice \n")
  print(rock)
  print("you choice \n")
  print(scissors)
  print("you loose")
elif you_choice==2 and computer_choice==2:
  print("computer choice \n")
  print(scissors)
  print("you choice \n")
  print(scissors)
  print("you are equal")
else:
  print("put right value")



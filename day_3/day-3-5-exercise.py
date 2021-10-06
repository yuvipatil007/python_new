# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


name = name1+name2
name=name.lower()
true_count = 0
true_count+=name.count('t')
true_count+=name.count('r')
true_count+=name.count('u')
true_count+=name.count('e')
#print(true_count)
love_count = 0
love_count+=name.count('l')
love_count+=name.count('o')
love_count+=name.count('v')
love_count+=name.count('e')
#print(love_count)
scores = int(str(true_count)+str(love_count))
if scores<10 or scores>90:
  print(f"your score is {scores}, you go together like coke and mentos")
elif scores>=40 and scores<50:
  print(f"Your score is {scores}, you are alright together")
else:
  print(f"Your score is {scores}")
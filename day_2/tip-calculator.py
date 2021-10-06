#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("Welcome to the tip calculator")
total=float(input("what was the total bill?"))
per =int(input("what percentage tip would you like to give? 10,12,15?"))
person=int(input("How many people to split the bill?"))

percent=1+float(per/100)

each_person_amount = (total/person)*percent

print("Each person should pay :${:0.2f}".format(each_person_amount))
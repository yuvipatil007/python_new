# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

number_student=0
sum_heights=0

for i in student_heights:
  number_student+=1
  sum_heights+=i
print(round(sum_heights/number_student))



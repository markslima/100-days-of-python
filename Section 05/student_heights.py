# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
student_sum = 0
student_num = 0

for student in student_heights:
    student_num += 1
    student_sum += student

print(f"\nOkay, so there were a total of {student_num} students in your list.\nThe total student height was {student_sum} cm.\nSo the average student height is {round(student_sum / student_num)}\n")
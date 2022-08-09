student_heights = input("Input a list of student heights cms \n").split()
total_height = 0
student_count = len(student_heights)


for n in range(0, student_count):
  student_heights[n] = int(student_heights[n])
  total_height += student_heights[n]

avg_height = round(total_height / student_count)

print(f"{avg_height} is the avg height in cms")
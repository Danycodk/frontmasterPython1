
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
#   print(student_scores)


tallest = 0

for higher in student_scores:
  if higher > tallest :
   tallest = higher

print(tallest)
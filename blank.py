def is_blank(line):
    return '\n' in line

f = open("questions.dat", "r")
for x in f:
#  print(len(x))
  print(x)
#   if x[0] == '*':
  if len(x) == 1:
    print("hit a blank line")
    answer = input("Enter the answer:")
#   if is_blank(x):
#      print("hit a blank line")
  
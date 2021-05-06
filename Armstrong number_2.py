num = int(input("number:  "))

n = len(str(num))
result = 0
x = num
while x != 0:
  digit = x % 10 
  result = result + digit ** n
  x = x // 10 
if num == result :
  print(num, "is an Armstrong number")
else:
  print(num, "is not an Armstrong number") 

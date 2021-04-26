num = int(input("number:  "))
while True:
  if num.isnumeric():
    break
  else:
    num = int(input()) 
n = len(str(num))
result = 0
x = num
while x != 0:
  digit = x % 10 #basamak sayısı
  result = result + digit ** n
  x = x // 10 
if num == result :
  print(num, "is an armstron number")
else:
  print(num, "not armstrong number")   
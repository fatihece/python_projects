# Task : Write a program that takes a number from the user ( asal sayı bulma kodu)
# and prints the result to check if it is a prime number

# The examples of the desired output are as follows :

# input →  19 ⇉ output : 19 is a prime number
# input →  10 ⇉ output : 10 is not a prime number


asal = int(input("number:"))

if asal > 1:
  for i in range(2, asal):
    if asal % i == 0:
      print(asal, "is not a prime number")
      break
  else:
    print(asal, "is a prime number") 

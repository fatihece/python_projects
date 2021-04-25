# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.
#Girilen sayının çif mi tek mi olduğunu kontrol eden program
#Girilen sayı 2'ye bölündüğünde kalan 0 ise, sayı çift(even) sayıdır.
#Kalan sayı 1 ise, sayı tek(odd) sayıdır.
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print(f"{num} is Even")
else:
   print(f"{num} is Odd")

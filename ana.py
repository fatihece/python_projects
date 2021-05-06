# Write a program that prompts the user to input a number and reverse its digits. 
# For example, the reverse of 12345 is 54321; reverse of 5600 is 65.

num = int(input("Enter a positive integer: "))
x = num
rev = 0
while x > 0:
    digit = x % 10
    rev = digit + rev*10
    x= int(x/10)
print("Reverse of",num,"is", rev)

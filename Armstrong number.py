number = input("Enter a number : ").strip()

while True:   
    if number.isdecimal():
        break
    else:
        number = input(" It is an invalid entry. Don't use non-numeric, float, or negative values! : ")

result = 0

for i in number:
    result += int(i) ** len(number)


if result == int(number):
    print(f"{number} is an Armstrong number.")
else :
    print(f"{number} is not an Armstrong number.")

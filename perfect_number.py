#Write a Python function to check whether a number is perfect or not.


def isPerfect(num):
    toplam=0
    for i in range(1, num):
        if num%i==0:
            toplam+=i
    if toplam==num:
        return True
    else:
        return False    

isPerfect(6)
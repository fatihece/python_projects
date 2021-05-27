"""
Girilen üç sayıdan en çok tekrar eden sayıyı bulan
fonksiyon yazınız.

Finding the most repeating number out of three entered in function

equal(4,4,4) --> 3
equal(3,4,4) --> 2
equal(1,2,3) --> 0

"""

def equal(a,b,c):
    numbers = [a,b,c]
    result = numbers.count(max(numbers, key=numbers.count))
    if result > 1:
        return result
    else:
        return 0 

print(equal(4,4,4))
print(equal(3,4,4))
print(equal(1,2,3))
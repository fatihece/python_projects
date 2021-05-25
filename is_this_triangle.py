"""
Implement a method that accepts 3 integer values a, b, c. 
The method should return true if a triangle can be built with the sides of given length and false in any other case.
(In this case, all triangles must have surface greater than 0 to be accepted).
"""
def is_triangle(a, b, c):
    
    return  (a+b > c) and abs(a-b) < c and (a+c > b) and abs(a-c) < b and (b+c > a) and abs(b-c) < a   
    
print(is_triangle(1,3,2))
print(is_triangle(3,4,5))
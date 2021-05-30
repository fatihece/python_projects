"""
given a list [1,2,3] get an all possible output permutation of these numbers in a list.
Example:
Input : [1,2,3]
Output :
        [
          [1, 2, 3], 
          [1, 3, 2], 
          [2, 1, 3], 
          [2, 3, 1], 
          [3, 1, 2], 
          [3, 2, 1]  
        ]
"""


solution = [[]]
num =[1,2,3]
num_set = set(num)
for index in range(len(num)) :
    solution =[i+[j] for i in solution for j in num_set.difference(set(i))]
    print(solution) # gives us every iteration to see all steps
print(solution)
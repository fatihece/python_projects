""" find the max and min element in alist without using 
max() and min() function"""

nums = [9,3,5,11,8,27,2,15]
max_num = nums[0]

for n in nums:
    if n > max_num:
        max_num = n
print(max_num)   


#------------************----------------
      
nums = [9,3,5,11,8,27,2,15]

min_num = nums[0]
for n in nums:
    if n < min_num:
        min_num = n
print(min_num)        

#! Given an array nums[], create a new array result[] such that:
#! result[i] = product of all elements of nums except nums[i]
#! example: 
#! Input: nums = [11,5,10,2]
#! Output: result = [100, 220, 110, 550] 
                    
#TODO INTERVIEW QUESTION














nums = eval(input("Enter list numbers: "))
#5,11,10,2
result = []

for i in nums:
    product = 1
    for j in nums:
        if i == j:
            continue
        else:
            product = product * j
    result.append(product)
    product = 1

print(f"Input List: {nums}")
print(f"Desired Output List: {result}")
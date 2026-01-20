
#! Given an array nums[], create a new array result[] such that:
#! result[i] = product of all elements of nums except nums[i]
#! example: 
#! Input: nums = [1, 2, 3, 4]
#! Output: result = [24, 12, 8, 6] 

nums = eval(input("Enter list numbers: "))
result = []
product = 1

for i in nums:
    for j in nums:
        if i == j:
            continue
        else:
            product = product * j
    result.append(product)
    product = 1

print(f"Input List: {nums}")
print(f"Desired Output List: {result}")
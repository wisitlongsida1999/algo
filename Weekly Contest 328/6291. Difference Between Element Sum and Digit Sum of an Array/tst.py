nums = [1,15,6,3]

sumDigit = int()
for num in nums:
    
    sumDigit += sum([int(x) for x in str(num)])

    
print(sumDigit)
    
def test(n):
    #base case
    if n<= 0:
        return 0
    elif n<=2:
        return 1
    #recursive case
    else:
        return test(n-3)+test(n-2)+test(n-1)

        
        
        
print(test(25))
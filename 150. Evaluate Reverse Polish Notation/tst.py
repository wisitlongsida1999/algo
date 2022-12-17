op = '/'

def revert_operator(num1,num2,opr):
    
    if opr == '+':
        
        return num1+num2
    elif opr == '-':
        
        return num1-num2

    elif opr == '*':
        return num1*num2

    elif opr == '/':
        return num1/num2


print(int(1/142))

l = [1,2]


l[0] = 4

print(l.pop(1))
print(l) 

print('+'.isnumeric()== False)
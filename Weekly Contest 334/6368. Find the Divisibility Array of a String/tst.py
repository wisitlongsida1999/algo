# time limit exceeded

# w = '998244353'
# m = 3

# t = list()

# for i,j in enumerate(w):
    
#     if int(w[:i+1]) %m == 0:
#         t.append(1)
#     else:
#         t.append(0)
    


# print(t)



# time limit exceeded
w = '998244353'
m = 3

t = list()

for i in range(0,len(w),2):
    
    if int(w[:i+1]) %m == 0:
        t.append(1)
    else:
        t.append(0)

    if int(w[:i+2]) %m == 0:
        t.append(1)
    else:
        t.append(0)

if len(w) %2 != 0:
    t.pop()

print(t)
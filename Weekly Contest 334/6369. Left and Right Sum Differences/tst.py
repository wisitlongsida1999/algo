


n = [10,4,8,3]
t = list()
for i ,j in enumerate(n):
    # if i == 0:
    #     t.append(sum(n[i+1:]))
    #     continue
    
    # if i == len(n)-1:
    #     t.append(sum(n[:-1]))
    #     break

    t.append(abs(sum(n[:i])-sum(n[i+1:])))

print(t)


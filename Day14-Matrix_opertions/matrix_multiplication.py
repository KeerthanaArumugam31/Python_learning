a=[]
b=[]
c=[]
for i in range(2):
    a.append([])
    for j in range(2):
        a[i].append(int(input("Enter the number:")))
for i in range(2):
    b.append([])
    for j in range(2):
        b[i].append(int(input("Enter the number:")))
for i in range(2):
    c.append([])
    for j in range(2):
        sum=0
        for k in range(2):
            mul=a[i][k]*b[k][j]
            sum+=mul
        c[i].append(sum)
for i in c:
    print(*i)
        
    

a=[]
b=[]
for i in range(2):
    a.append([])
    for j in range(2):
        a[i].append(int(input("Enter the number:")))
for i in range(2):
    b.append([])
    for j in range(2):
        b[i].append(a[j][i])
for i in b:
    print(*i)
        


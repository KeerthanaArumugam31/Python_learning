a=[]
b=[]
c=[]
row=int(input("Enter the row value:"))
column=int(input("Enter the column value:"))
for i in range(row):
    a.append([])
    for j in range(column):
        a[i].append(int(input("Enter the number:")))
for i in range(row):
    b.append([])
    for j in range(column):
        b[i].append(int(input("Enter the number:")))
for i in range(row):
    c.append([])
    for j in range(column):
        c[i].append(a[i][j]-b[i][j])
for i in c:
    print(*i)

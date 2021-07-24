x=[]
r=int(input("Enter the number:"))
c=int(input("Enter the number:"))
for i in range(r):
    x.append([])
    for j in range(c):
        x[i].append(int(input()))
for i in range(r):
    for j in range(c):
        if j==0 or j==c-1 or i==j:
            print(str(x[i][j]),end=" ")
        else:
            print(" ",end=" ")
    print()

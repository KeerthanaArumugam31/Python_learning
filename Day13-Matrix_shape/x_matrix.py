x=[]
r=int(input("Enter the number:"))
c=int(input("Enter the number:"))
for i in range(r):
    x.append([])
    for j in range(c):
        x[i].append(int(input()))
for i in range(r):
    for j in range(c):
        if i==j or i+j==r-1:
            print(" ",str(x[i][j]),end=" ")
        else:
            print(" ",end=" ")
    print()

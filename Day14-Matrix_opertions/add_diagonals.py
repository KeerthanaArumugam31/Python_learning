a=[]
sum=0
for i in range(3):
    a.append([])
    for j in range(3):
        a[i].append(int(input("Enter the number:")))
        if (i==j):
            sum=sum+a[i][j]
        elif i+j==2:
            sum=sum+a[i][j]
print(sum)
        

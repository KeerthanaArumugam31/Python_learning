k=1
for i in range(5):
    for j in range(5):
        print(k,end=" ")
        k=(i+j)%2
    print()

k=1
for i in range(1,6):
    for j in range(1,6):
        k=2*(i+j)-3
        if k<10:
            print(" "+str(k),end=" ")
        else:
            print(k,end=" ")
    print()



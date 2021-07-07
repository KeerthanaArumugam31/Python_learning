for i in range(1,6):
    k=i
    for j in range(1,6):
        if k<10:
            print(" "+str(k),end=" ")
        else:
            print(k,end=" ")
        k=k+5
    print()

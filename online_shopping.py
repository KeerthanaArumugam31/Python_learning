f=open("stock.txt")
id=input("Enter the Id:")
for i in f:
    if str(id) in i:
        j=i.split(" ")
        print(f"Product name:{j[1]}")
        print(f"Product price:{j[2]}")
        Quantity=int(input("Enter the quantity:"))
        if Quantity<=int(j[3]):
            print(f"Total Amount is {Quantity*int(j[2])}")
            break
        else:
            print("Out of stock")
            break
else:
     print("Id is unavailable")

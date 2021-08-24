product={101:["Chocolate",80,100],102:["Ice-Cream",100,20],103:["Milkshake",35,30],104:["Biscuits",30,10],105:["Cakes",35,50]}
while True:
    id=int(input("Enter the Product_Id:"))
    r=open("stock.txt","r")
    w=open("stock.txt","a")
    if id in product:
        print("Product Name:",product[id][0])
        print("Product Price:",product[id][1])
        print("Available Stock:",product[id][2])
        w.write(str(f"{id} {product[id][0]} {product[id][1]} {product[id][2]}\n"))
    else:
        print("Id Unavailable")
        break
        w.close()
        r.close()





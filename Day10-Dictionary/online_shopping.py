product={1001:['Bag',20,30],1002:['Pen',10,100],1003:['Soap',45,5],1004:['Diarymilk',10,50],1005:['Paste',30,3],1006:['Notebook',30,5]}
sum=0
while True:
   id=int(input("Enter the product id:"))
   if id in product:
     print("Product Name:",product[id][0])
     print("Price:",product[id][1])
     Quantity=int(input("Enter the quantity:"))
     if Quantity<product[id][2]:
        Amount=Quantity*product[id][1]
        print("Amount is",Amount)
        sum+=Amount
        print("successfully purchased")    
     else:
        print("Stock unavailabe")
   else:
      print("id unavailable")
      break

print("Bill amount",sum)
      


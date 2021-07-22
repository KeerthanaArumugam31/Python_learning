cart={}
while True:
    ch=int(input("1.Add to cart 2.Remove from cart 3.Update cart 4.View cart 5.exit"))
    if ch==1:
        product_id=input("Product id:")
        product_name=input("Product name:")
        quantity=input("Quantity:")
        price=input("Price:")
        cart.setdefault(product_id,[product_name,quantity,price])
        print("Added to cart successfully !!!")
    elif ch==2:
        product_id=input("Product id:")
        del(cart[product_id])
    elif ch==3:
        product_id=input("Product id:")
        product_name=input("Product name:")
        quantity=input("Quantity:")
        price=input("Price:")
        cart[product_id]=([product_name,quantity,price])
    elif ch==4:
        for product_id in cart.keys():
            print(product_id," ",cart[product_id][0]," ",cart[product_id][1]," ",cart[product_id][2])
    else:
        break

product_name1=input("Enter the first product name:")
price1=int(input("Enter the price amount:"))
quantity1=int(input("Enter the quantity:"))
discount1=int(input("Enter the discount:"))

product_name2=input("Enter the second product name:")
price2=int(input("Enter the price amount:"))
quantity2=int(input("Enter the quantity:"))
discount2=int(input("Enter the discount:"))

product_name3=input("Enter the third product name:")
price3=int(input("Enter the price amount:"))
quantity3=int(input("Enter the quantity:"))
discount3=int(input("Enter the discount:"))

product_name4=input("Enter the fourth product name:")
price4=int(input("Enter the price amount:"))
quantity4=int(input("Enter the quantity:"))
discount4=int(input("Enter the discount:"))

product_name5=input("Enter the fifth product name:")
price5=int(input("Enter the price amount:"))
quantity5=int(input("Enter the quantity:"))
discount5=int(input("Enter the discount:"))

total1=quantity1*price1
total2=quantity2*price2

total3=quantity3*price3
total4=quantity4*price4
total5=quantity5*price5

discount_amnt1=discount1/100*total1
discount_amnt2=discount2/100*total2
discount_amnt3=discount3/100*total3
discount_amnt4=discount4/100*total4
discount_amnt5=discount5/100*total5

total_amount=total1+total2+total3+total4+total5
discount_amount=discount_amnt1+discount_amnt2+discount_amnt3+discount_amnt4+discount_amnt5
pay_amount=total_amount-discount_amount

print(f"Total amount is {total_amount}")
print(f"Discount amount is {discount_amount}")
print(f"You have to pay {pay_amount}")
print(f"   THANK YOU !!! , WELCOME AGAIN   ")





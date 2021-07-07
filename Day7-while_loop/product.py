num=int(input("Enter the number:"))
mul=1
while num>0:
    mul*=num%10
    num=num//10
print(mul)

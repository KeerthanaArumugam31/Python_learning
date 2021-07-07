n=int(input("Enter the number:"))
sum=0
x=n
while(n>0):
    digit=n%10
    fact=1
    for i in range(1,digit+1):
      fact*=i
    sum+=fact
    n=n//10
if x==sum:
    print("It is a strong number")
else:
    print("It is not a strong number")
    

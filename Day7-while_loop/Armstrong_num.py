n=int(input("enter the number:"))
sum=0
x=n
while(n>0):
    digit=n%10
    value=digit**3
    sum=sum+value
    n//=10
if x==sum:
    print(x,"it is an armstrong number")
else:
    print(x,"it is not an armstrong number")

        
        

    

    

#Factorial
n=int(input("Enter the number:"))
fact=1
for i in range(1,n+1):
  fact*=i
  if i<n:
      print(f"{i}*",end="")
  elif i==n:
      print(f"{i}",end="")
print(f"={fact }")     

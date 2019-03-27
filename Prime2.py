flag=1
n=input("Enter the number")
for i in range(2,n):
    if(n%i==0):
        print(n," is not prime")
        flag=0
        break


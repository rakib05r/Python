a=int (input())
b=int (input())
flag=0
for i in range(2,b-1,1):
    if(b%i==0):
        flag=1
    if(flag==1):
        print("Not Prime")
    else:
        
            print("Prime")
            

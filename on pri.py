lower =int(input("Enter Starting value "))
upper =int(input("Enter Ending value "))
print("Prime numbers between",lower,"and",upper,"are:")

for num in range(lower,upper + 1):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
input("Exit")

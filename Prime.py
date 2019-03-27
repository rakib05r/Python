a=2
num=int(input("Enter a number"))
while num > a :
  if num%a==0 & a!=num:
    print('not prime')
    a=a+1
  else:
    print('prime')
    a=(num)+1
input("Exit")

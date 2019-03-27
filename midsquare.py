z = 7182

for i in range (10):

    str1 = z*z

    str1 = str(str1)

    str2 = list(str1)
   
    str3 = str2[2]+str2[3]+str2[4]+str2[5]
    
    a = int (str3)

    print str1,"   ", a ,"   ", float(a)/10000
    
    z=a

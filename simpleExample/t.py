def f(str1,str2,str3):
    x=str1.find(str2)
    if (x!=-1):
        str1=str1.replace(str2,str3)
        return (str1)
    else:
        return(str1)



Bu bir deneme
print(f("covid is a bad illness", "covid", "cancer"))



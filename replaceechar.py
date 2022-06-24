def rep(str, ch1, ch2):
    #Write your code here
    for i in str:
        if i==ch1:
            str=str.replace(i,ch2)
        elif i==ch2:
            str=str.replace(i,ch1)
        else:
            continue
    return str


str = input("Enter string:")
ch1 = input("Enter ch1:")
ch2 = input("Enter ch2:")
print (rep(str, ch1, ch2))

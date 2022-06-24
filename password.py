def password(str):
    if len(str)<4:
        return 0
    elif str[0].isdigit():
        return 0
    dig=0
    cap=0
    for i in range (len(str)):
        if not str[i].isdigit():
            dig = 1
        if str[i]==" " or str[i]=="/":
            return 0
        # elif not str[i].isupper():
        #     return 0
        if not str[i]>="A" and str[i]<="Z":
            cap = 1
    if dig !=0 and cap !=0:
        return 1
    else:
        return 0


str = input("Enter str:")
print (password(str))




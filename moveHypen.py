def hypen(str):
    if len(str) == 0:
        return -1
    nstr =""
    hyp= 0
    for i in str:
        if i == "-":
            hyp += 1
        else:
            nstr += i
    return hyp*"-" + nstr
str = input("Enter string:")
print (hypen(str))


str = input("Enter str:")
print (hypen(str))




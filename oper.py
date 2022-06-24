def fun(str):
    if len(str)==0:
        return -1
    a=int(str[0])
    i=1
    while i<len(str):

        if str[i]=="A":
            a&=int(str[i+1])
        elif str[i]=="B":
            a|=int(str[i+1])
        if str[i]=="C":
            a^=int(str[i+1])
        i+=2
    return a
str = input("Enter your string:")
print (fun(str))

#     # IP -0C1A1B1C1C1B0A0
#       OP - 0
#
# # IP - 1C0C1C1A0B1
# OP-1
#


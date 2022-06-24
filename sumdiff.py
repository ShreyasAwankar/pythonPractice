def sumDiff(m,n):
    divisible = 0
    nondivisible =0
    for i in range (m+1):
        if i%n==0:
            divisible+=i
        else:
            nondivisible+=i
    return abs(nondivisible-divisible)
# m = int(input("Enter m:"))
# n = int(input("Enter n:"))
# print (sumDiff(m,n))
str= input()
for i in range(len(str)):
     if not str[i].isdigit():
         print("0")
     else :
         print ("1")
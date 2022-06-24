# num = 534978231
# strnum = str(num)
# print (strnum[3])

# def carry(num1, num2): This program is to be corrected its not providing the correct output for given inputs
    str1=str(num1)
    str2=str(num2)
    carr = 0
    if len(str1)>=len(str2):
        l = len(str1)
        for i in range(l):
            x = int(str1[len(str1)-1]) + int(str2[len(str2)-1])
            if x >= 10:
                carr += 1

    if len(str1) < len(str2):
        l = len(str2)
        for i in range(l):
            x = int(str2[len(str2) - 1]) + int(str1[len(str1) - 1])
            if x >= 10:
                carr += 1
    return carr
num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))
print (carry(num1, num2))
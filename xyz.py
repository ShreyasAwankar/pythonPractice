#
# num = int(input("Enter a number "))
# for i in range (0, num+1):
#     if i%2 == 0:
#         print (i, end =",")
#     if i%3==0:
#         continue

def bc(n):
    for i in range(3, n + 1):
        print (i)


inp = int(input("n: "))
bc(inp)

n = int(input("How many rows:\n"))
type = int(input("Enter 1 or 0:\n"))

if type == 1:
    for i in range (1,n+1):
        print ("*"*i)
elif type == 0:
    for i in range (1, n+1):
        print ("*"*(n+1-i))
else:
    print ("Please enter either 1 or 0 in second input...")

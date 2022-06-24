def evSum (m,n):
    num = 0
    for i in range (m, n+1):
        if i%2 == 0:
            num = num + i
    return f"The sum of all even numbers within your entered range is - {num}"
m = int(input("Enter first number of range:\n"))
n = int(input("Enter last number of range:\n"))
print (evSum(m,n))
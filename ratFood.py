def ratFood(r,unit,n,arr):
    foodreq = r * unit
    foodpr=0
    count=0
    if n == 0:
        return -1
    for i in range (n):
        if foodpr < foodreq:
            foodpr += arr[i]
            count += 1

    if foodreq>foodpr:
        return 0
    return count
r = int(input("Enter r:"))
unit = int(input("Enter unit:"))
n = int(input("Enter n:"))
arr=list(map(int, input("Enter array:").split()))
print (ratFood(r,unit,n,arr))







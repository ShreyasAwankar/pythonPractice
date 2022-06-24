def productsmallestPair(sum, arr):
    if len(arr)<2:
        return -1
    arr.sort()
    for i in range (len(arr)):
        if arr[i]+arr[i+1] < sum:
            return arr[0] * arr[1]
            break
        else:
            return 0
sum = int(input("Enter Sum:"))
arr = list(map(int, input("Enter arr:").split()))
print (productsmallestPair(sum, arr))



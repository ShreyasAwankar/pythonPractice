def largeSmallSum(arr):
    if len(arr)<4:
        return 0
    evenArr = []
    oddArr = []
    for i in range (len(arr)):
        if i%2==0:
            evenArr.append(arr[i])
        else:
            oddArr.append(arr[i])
    evenArr.sort()
    oddArr.sort()
    return evenArr[len(evenArr)-2] + oddArr[len(oddArr)-2]
arr = list(map(int, input("Enter arr elements:").split(",")))
print (largeSmallSum(arr))
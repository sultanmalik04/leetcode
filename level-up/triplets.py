def triplets(arr, s):
    ans = []
    arr.sort()
    for i in range(len(arr)-2):
        pairSum = s - arr[i]
        j = i+1
        k = len(arr) - 1
        while j < k:
            s1 = arr[j] + arr[k] 
            if s1 == pairSum:
                ans.append([arr[i], arr[j], arr[k]])
                j += 1
                k -= 1
            elif s1 < pairSum:
                j += 1
            else:
                k -= 1
    return ans


print(triplets([1,2,3,4,5,6,9,10], 15))
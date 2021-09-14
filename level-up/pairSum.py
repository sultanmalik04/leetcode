def pairSum(arr, s):
    ans = []
    unordered_set = set()

    for i in range(len(arr)):
        x = s - arr[i]
        if x in unordered_set:
            ans.append(x)
            ans.append(arr[i])
            return ans
        unordered_set.add(arr[i])
    return ans

print(pairSum([4, 3, 2, 3, 2], 7))
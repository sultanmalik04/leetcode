def longet_band(a):
    n = len(a)
    largestLen = 0

    unordered_set = set(a)

    for element in a:
        prev = element - 1

        if not prev in unordered_set:
            cnt = 1
            next_element = element + 1

            while next_element in unordered_set:
                next_element += 1
                cnt += 1
            largestLen = max(largestLen, cnt)
    return largestLen 


print(longet_band([1, 2, 3, 4, 0, 5, 6, 7, 9, 12, 10])) # 8
print(longet_band([4, 5, 6, 8, 9, 10, 11, 7, 3])) # 9
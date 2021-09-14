def highest_mountain(a):
    l = len(a)

    highest = 0
    i = 1

    while i < l-1:
        
        # check if a[] is peak or not
        if a[i] > a[i-1] and a[i] > a[i+1]:
            cnt = 1
            j = i

            # count backwards
            while j >= 1 and a[j] > a[j-1]:
                cnt += 1
                j -= 1

            # count forwards
            while i < l-1 and a[i] > a[i+1]:
                cnt += 1
                i += 1
            highest = max(highest, cnt)
        else:
            i += 1 
    return highest

print(highest_mountain([5, 6, 1, 2, 3, 4, 5, 4, 3, 2, 0, 1, 2, 3, -2, -4])) # 9
print(highest_mountain([2, 1, 2, 3, 4, 5, 3, 6])) # 6
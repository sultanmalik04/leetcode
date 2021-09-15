def minSwaps(arr):
    list1 = list(enumerate(arr))
    print(list1)
    list1 = sorted(list1, key=lambda x:x[1])
    print(list1)
    visited = [0 for i in range(len(arr))]
    ans = 0

    for i in range(len(arr)):
        old_pos = list1[i][0]
        if visited[i] == 1 or old_pos == i:
            continue

        node = i
        cycle = 0

        while not visited[node]:
            visited[node] = 1
            next_node = list1[node][0]
            node = next_node
            cycle += 1

        ans += cycle-1
    return ans

print(minSwaps([5, 4, 3, 2, 1])) # 2
print(minSwaps([2, 4, 5, 1, 3])) # 3
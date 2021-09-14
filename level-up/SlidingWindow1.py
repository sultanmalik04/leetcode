# You have given an array and you need to find all the subarrays that sums to K


def slidingWindow(a, k):
    right = 0
    left = 0
    n = len(a)
    smallest_window = n

    windowSum = 0
    while right <= n-1:
        windowSum += a[right]
        right += 1

        while windowSum > k and left < right:
            windowSum -= a[left]
            left += 1
        
        if windowSum == k:
            print(left, right - 1)

        smallest_window = min(smallest_window, right - left+1)
    print(smallest_window)

slidingWindow([1, 3, 2, 1, 4, 1, 3, 2, 1, 1, 2], 8)
             
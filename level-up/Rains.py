def rains(a):
    n = len(a)

    # Compute L arr which will contain the maximum height in the left direction at ith position
    L = [0 for i in range(n)]
    R = [0 for i in range(n)]
    L[0] = a[0]
    R[n-1] = a[n-1]
    for i in range(1, n):
        L[i] = max(L[i-1], a[i])
        R[n-i-1] = max(R[n-i], a[n-i-1])
    
    total_water = 0
    # Calculate the total water stored 
    for i in range(n):
        total_water += min(L[i], R[i]) - a[i]
    
    return total_water


print(rains([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
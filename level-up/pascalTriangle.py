def pascalTriangle(numRows):
    res = []
    if numRows == 0:
        return res
    
    first = [1]
    res.append(first)
    for i in range(1, numRows):
        row = [1]
        prev = res[i-1]
        for j in range(1, i):
            row.append(prev[j-1] + prev[j])
        row.append(1)
        res.append(row)
    return res

print(pascalTriangle(5)) # [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]


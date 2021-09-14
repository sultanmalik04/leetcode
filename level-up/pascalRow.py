def pascalRow(rowIndex):
    row = [1]
    res = 1
    
    for i in range(rowIndex):
        res *= rowIndex-i
        res //= i+1
        row.append(res)
        
    return row

print(pascalRow(4)) # [1, 4, 6, 4, 1]
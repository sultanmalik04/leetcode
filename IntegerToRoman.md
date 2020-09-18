## Python
Using Single loop
```python
class Solution:
    def intToRoman(self, num: int) -> str:
        s = ''
        while num > 0:
    
            if num >= 1000:
                s += "M"
                num -= 1000
                
            elif num >= 900 and num < 1000:
                s += "CM"
                num -= 900
                
            elif num >= 500 and num < 900:
                s += "D"
                num -= 500
                
            elif num >= 400 and num < 500:
                s += "CD"
                num -= 400
                
            elif num >= 100 and num < 400:
                s += "C"
                num -= 100
                
            elif num >= 90 and num < 100:
                s += "XC"
                num -= 90
                
            elif num >= 50 and num < 90:
                s += "L"
                num -= 50
                
            elif num >= 40 and num < 50:
                s += "XL"
                num -= 40
                
            elif num >= 10 and num < 40:
                s += "X"
                num -= 10
                
            elif num >= 9 and num < 10:
                s += "IX"
                num -= 9
                
            elif num >= 5 and num < 9:
                s += "V"
                num -= 5
                
            elif num >= 4 and num < 5:
                s += "IV"
                num -= 4
                
            else:
                s += "I"
                num -= 1
                
        return s
```
Using two loop
```python
class Solution:
    def intToRoman(self, num: int) -> str:
        dict = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
        s = ''
        for int_key, roman in dict.items():
            while (num >= int_key):
                s += roman
                num -= int_key
        return s
```
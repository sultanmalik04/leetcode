## Python
```python
    class Solution(object):
        def addBinary(self, a, b):
            """
            :type a: str
            :type b: str
            :rtype: str
            """
            i, j = len(a)-1, len(b)-1
            carry = 0
            result = ''
            while i >= 0 or j >= 0:
                sum = carry
                if i >= 0:
                    sum +=  int(a[i])
                if j >= 0:
                    sum += int(b[j])
                result += str(sum%2)
                carry  = sum//2
                i -= 1
                j -= 1
            if carry > 0:
                result += str(carry)
            return result[::-1]
```

## Java
```java
    class Solution {
        public String addBinary(String a, String b) {
            StringBuilder result = new StringBuilder();
            int i = a.length() - 1;
            int j = b.length() - 1;
            int carry = 0;
            while (i >= 0 || j >= 0){
                int sum = carry;
                if (i >= 0) sum += a.charAt(i--) - '0';
    			if (j >= 0) sum += b.charAt(j--) - '0';
                result.append(sum % 2);
                carry = sum / 2;
            }
            if (carry != 0) 
                result.append(carry);
            
            return result.reverse().toString();
        }
    }
```
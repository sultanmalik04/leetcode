## Python
```python
from itertools import permutations 

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        for i in permutations(nums):
            ret.append(list(i))
        return ret
```
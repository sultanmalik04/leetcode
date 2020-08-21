class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j, k = 0, 0, 0
        l1, l2 = len(nums1), len(nums2)
        nums = [None]*(l1+l2)
        while i < l1 and j < l2:
            if nums1[i] <= nums2[j]:
                nums[k] = nums1[i]
                i += 1
                k += 1
            else:
                nums[k] = nums2[j]
                j += 1
                k += 1

        while i < l1:
            nums[k] = nums1[i]
            i += 1
            k += 1
        while j < l2:
            nums[k] = nums2[j]
            j += 1
            k += 1
        l = len(nums)
        if l % 2 == 0:
            return (nums[l//2 - 1] + nums[l//2])/2
        return nums[l//2]

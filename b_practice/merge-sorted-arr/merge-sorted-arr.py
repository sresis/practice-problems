class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx1 = 0
        idx2 = 0
        num1_copy = nums1[:m]
        print(num1_copy)
        nums1[:] = []
        while idx2 < n and idx1 < m:
            if nums2[idx2] < num1_copy[idx1]:
                nums1.append(nums2[idx2])
                idx2 += 1
            else:
                nums1.append(num1_copy[idx1])
                idx1 += 1
        if idx1 < m:
            nums1[idx1 + idx2:] = num1_copy[idx1:]
        elif idx2 < n:
            nums1[idx2 + idx1:] = nums2[idx2:]
                
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # merge the arrays
        idx1 = 0
        idx2 = 0
        new_arr = []
        while idx1 < len(nums1) or idx2 < len(nums2):
            # if both still inbounds
            if idx1 < len(nums1) and idx2 < len(nums2):
                if nums1[idx1] < nums2[idx2]:
                    new_arr.append(nums1[idx1])
                    idx1 += 1
                else:
                    new_arr.append(nums2[idx2])
                    idx2 += 1
            elif idx1 < len(nums1):
                new_arr.append(nums1[idx1])
                idx1 += 1
            else:
                new_arr.append(nums2[idx2])
                idx2 += 1
        # then get the median of the new array
        # if odd, take value
        # if even, take average of middle 2        
        length = len(new_arr)
        mid = length // 2
        if length % 2 == 0:
            val = (new_arr[mid] + new_arr[mid-1]) / 2
            return val
        else:
            return float(new_arr[mid])
        

        
        
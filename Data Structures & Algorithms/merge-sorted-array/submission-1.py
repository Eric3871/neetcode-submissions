class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = nums1[:m]
        right = nums2[:n]

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                nums1[k] = left[i]
                i += 1
            else:
                nums1[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums1[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            nums1[k] = right[j]
            j += 1
            k += 1

# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs) -1)
    
    def mergeSortHelper(self, pairs, start, end):
        if (end - start + 1 <= 1):
            return pairs

        #middle index
        middle = (start + end) // 2

        #sort the left 1/2
        self.mergeSortHelper(pairs, start, middle)
        #sort the right 1/2
        self.mergeSortHelper(pairs, middle + 1, end)

        #merge sorted 1/2's
        self.merge(pairs, start, middle, end)

        return pairs

    def merge(self, pairs, start, middle, end):
        #copy the sorted left & right halfs to temp arrays
        L = pairs[start: middle + 1]
        R = pairs[middle + 1: end + 1]

        i = 0
        j = 0
        k = start

        # Merge the two sorted halfs into the original array
        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                pairs[k] = L[i]
                i += 1
            else:
                pairs[k] = R[j]
                j += 1
            k += 1

        # One of the halfs will have elements remaining
        while i < len(L):
            pairs[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            pairs[k] = R[j]
            j += 1
            k += 1

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        for x in range(len(arr)):
            max = 0
            for y in range(x+1, len(arr)):
                if arr[y] > max:
                    max = arr[y]
                arr[x] = max
        
        arr.pop(-1)
        arr.append(-1)

        return arr


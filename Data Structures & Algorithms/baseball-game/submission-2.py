class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        score = [] 
        for x in operations:
            if x == "+":
                score.append(score[-1] + score[-2])    
            elif x == "D":
                score.append(score[-1] * 2)
            elif x == "C":
                score.pop()
            else:
                score.append(int(x))
        
        return sum(score)


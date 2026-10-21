class Solution:
    def isValid(self, s: str) -> bool:
        ans = []
        for x in s:
            if x == "(" or x == "{" or x == "[":
                ans.append(x)
            else:
                if not ans:
                    return False
                if x == ")":
                    if ans[-1] == "(":
                        ans.pop()
                    else: return False
                if x == "]":
                    if ans[-1] == "[":
                        ans.pop()
                    else: return False
                if x == "}":
                    if ans[-1] == "{":
                        ans.pop()
                    else: return False
            
        return bool(len(ans) == 0)
        
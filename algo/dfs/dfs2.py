# https://leetcode.com/problems/generate-parentheses/
def generateParenthesis(self, n: int) -> List[str]:
    ans = []
    left = n
    right = n
    def dfs(left, right, comb):
        if left == 0 and right == 0:
            ans.append(comb)
            return
        if left == 0:
            comb += ")" * right
            ans.append(comb)
            return
        if left > 0:
            dfs(left - 1, right, comb + "(")
        if right > 0 and left < right:
            dfs(left, right - 1, comb + ")")
        
    dfs(left, right, "")
    return ans 

# The space complexity of a recursive call 
# depends on the maximum depth of the recursive call.
# Each level consumes a constant amount of space.
# The above example space complexity is O(n)    
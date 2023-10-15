# https://leetcode.com/problems/merge-intervals
def merge(self, a: List[List[int]]) -> List[List[int]]:
    ans = []
    n = len(a)
    a = sorted(a, key=lambda x: (x[0], x[1]))
    l = a[0][0]
    r = a[0][1]
    for i in range(1, n):
        cur = a[i]
        if r < cur[0]:
            ans.append([l, r])
            l = cur[0]
            r = cur[1]
        else:
            r = max(cur[1], r)
    ans.append([l, r])
    return ans
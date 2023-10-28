from typing import List
# https://leetcode.com/problems/number-of-provinces/
def findCircleNum(isConnected: List[List[int]]) -> int:
    n = len(isConnected)
    UF = {}
    def find(x):
        if UF.setdefault(x, x) != x:
            return find(UF[x])
        else:
            return x
    def union(x, y):
        xRoot = find(x)
        yRoot = find(y)
        # merge root
        if xRoot > yRoot:
            UF[xRoot] = yRoot
        else:
            UF[yRoot] = xRoot
    for i in range(n):
        find(i)
    for i in range(n):
        for j in range(i + 1, n):
            if isConnected[i][j] == 1 and find(i) != find(j):
                union(i, j)
    provinces = set()
    for i in range(n):
        provinces.add(find(i))
    return len(provinces)
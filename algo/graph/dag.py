from typing import List
# directed acyclic graph 
# https://leetcode.com/problems/parallel-courses-iii
# DFS
def minimumTime(n: int, relations: List[List[int]], time: List[int]) -> int:
    from collections import defaultdict
    d = defaultdict(list)
    for _ in relations:
        d[_[0]].append(_[1])
    dp = [-1] * (n + 1)
    def dfs(course):
        if dp[course] != -1:
            return dp[course]
        length = time[course - 1]
        spend = 0
        for _ in d[course]:
            spend = max(spend, dfs(_))
        dp[course] = length + spend
        return length + spend
    for i in range(1, n + 1):
        if dp[i] == -1:
            dfs(i)
    return max(dp)

# kahn’s algorithm
# build graph
# find all nodes with no incoming edge (0 indegree)
# store those with 0 indegree to a queue and BFS, sort of delete them from graph
# repeat until queue is empty
# time complexity O(V+E)
def minimumTime(n: int, relations: List[List[int]], time: List[int]) -> int:
    nodes = set([_ for _ in range(1, n + 1)])
    adjacencyList = [[] for _ in range(n + 1)]
    timeSpent = [0] * (n + 1)
    inDegree = [0] * (n + 1)
    for _ in relations:
        nodes.discard(_[1])
        adjacencyList[_[0]].append(_[1])
        inDegree[_[1]] += 1
    nodes = list(nodes)
    while nodes:
        cur = nodes.pop(0)
        if timeSpent[cur] == 0:
            timeSpent[cur] += time[cur - 1]
        for _ in adjacencyList[cur]:
            timeSpent[_] = max(timeSpent[_], timeSpent[cur] + time[_ - 1])
            inDegree[_] -= 1
            if inDegree[_] == 0:
                nodes.append(_)
    return max(timeSpent)
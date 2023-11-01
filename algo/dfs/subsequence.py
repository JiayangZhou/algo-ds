# get all subsequence with length 3
w = [1, 2, 3, 4]
def dfs(res, w, index, sub):
    sub.append(w[index])
    if len(sub) == 3:
        res.append(tuple(sub))
        return
    if index >= len(w):
        return
    for i in range(index + 1, len(w)):
        subCopy = sub.copy()
        dfs(res, w, i, subCopy)
res = []
for i in range(len(w)):
    dfs(res, w, i, [])
print(res)
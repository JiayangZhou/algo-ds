UF = {}
def find(x):
    if UF.setdefault(x, x) != x:
        return find(UF[x])
    else:
        return x

def union(x, y):
    xRoot = find(x)
    yRoot = find(y)
    if xRoot > yRoot:
        UF[xRoot] = yRoot
    else:
        UF[yRoot] = xRoot
        
# another implementation
def find(x):
    if x not in UF:
        UF[x] = x
        return x
    else:
        if UF[x] == x:
            return x
        return find(UF[x])

def union(x, y):
    xRoot = find(x) 
    yRoot = find(y)
    if xRoot < yRoot:
        UF[yRoot] = UF[xRoot]
    else:
        UF[xRoot] = UF[yRoot]
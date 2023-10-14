# https://leetcode.com/problems/zigzag-conversion
def convert(s: str, rows: int) -> str:
    ans = ""
    n = len(s)
    groups = [""] * rows
    index = 0
    if rows == 1: # do consider corner cases!
        return s
    volume = rows + (rows - 2)
    
    while index < n:
        end = index + volume
        i = 0
        right = True
        while index < n and index < end:
            groups[i] += s[index]
            if i == rows - 1:
                right = False
            if right:
                i += 1
            else:
                i -= 1
            index += 1
        
    for g in groups:
        ans += g
    return ans
convert("PAYPALISHIRING", 3) #PAHN APLSIIG YIR
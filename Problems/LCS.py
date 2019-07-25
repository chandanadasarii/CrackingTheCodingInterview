def LCS(s1, s2, i=0, j=0):
    if i >= len(s1) or j >= len(s2):
        return 0
    if s1[i] == s2[j]:
        return 1 + LCS(s1, s2, i+1, j+1)
    else:
        return max(LCS(s1, s2, i+1, j), LCS(s1, s2, i, j+1))

print(LCS('abcbdab', 'bdcaba'))

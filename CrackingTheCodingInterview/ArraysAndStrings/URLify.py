def URLify(s, n):
    if n > len(s):
        return []

    index = len(s)-1

    for i in range(n-1, -1, -1):
        if s[i] == ' ':
            s[index-2:index+1] = '%20'
            index -= 3
        else:
            s[index] = s[i]
            index -= 1
    
    return s

print(URLify(list("Mr John Smith    "), 13))
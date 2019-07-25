def stringCompression(string):
    out = list()
    charcount = 1
    for i in range(len(string)):
        if i+1 < len(string) and string[i] == string[i+1]:
            charcount += 1
        else:
            out.append(string[i])
            out.append(charcount)
            charcount = 1
    
    outstring = ''.join(map(str, out))

    if len(outstring) < len(string):
        return outstring
    else:
        return ''.join(map(str, string))


print(stringCompression(list('aaabbbbbccccaaa')))
print(stringCompression(list('aabcccccaaa')))
print(stringCompression(list('abcd')))
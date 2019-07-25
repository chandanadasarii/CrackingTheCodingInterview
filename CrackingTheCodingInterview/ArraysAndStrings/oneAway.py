def oneAway(source, target):
    if abs(len(source) - len(target)) > 1:
        return False

    i, j = [0,0]
    firstEdit = False

    while (i < len(source) and j < len(target)):
        if source[i] != target[j]:
            if firstEdit:
                return False
            if len(source) == len(target):
                i += 1
                j += 1
            elif len(source) < len(target):
                j += 1
            else:
                i += 1
            firstEdit = True
        else:
            i += 1
            j += 1

    return True

print(oneAway(list(""), list("")))
print(oneAway(list("pale"), list("pal")))
print(oneAway(list("pales"), list("pale")))
print(oneAway(list("pale"), list("bale")))
print(oneAway(list("pale"), list("ple")))
print(oneAway(list("pale"), list("bae")))

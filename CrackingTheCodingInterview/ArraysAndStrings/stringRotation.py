def stringRotation(s1, s2):
    if len(s1) != len(s2):
        return False
    
    s1 = s1+s1

    if s1.find(s2) != -1:
        return True
    else:
        return False

print(stringRotation('waterbottle', 'erbottlewat'))
print(stringRotation('waterboatle', 'erbottlewat'))


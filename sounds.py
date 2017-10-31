def Soundex(strInit, codeLength=4):
    
    ignored = "'.?!@hw"
    groups = (
        (' '),
        ('b', 'f', 'p', 'v'),
        ('c', 'g', 'j', 'k', 'q', 's', 'x', 'z'),
        ('d', 't'),
        ('l',),
        ('m', 'n'),
        ('r',),
        #('a', 'e', 'i', 'o', 'u', 'y')
        )
    strFinal = [strInit.lstrip()[0]]
    strInit = strInit.lower()
    formerVal = 7
    curVal = 7
    for idx, group in enumerate(groups):
        if strInit[0] in group:
            formerVal = idx
    
    inGroups = False
    strInit = ''.join(c for c in strInit if c not in ignored)
    for letter in strInit[1:]:
        for idx, group in enumerate(groups):
            if letter in group:
                curVal = idx
                inGroups = True
        if curVal != formerVal:
            if curVal != 0 and inGroups:
                strFinal.append(str(curVal))
        if not (inGroups):
            curVal = 7
        formerVal = curVal
        inGroups = False

    # len(strFinal) should be forced to codeLength (traditionally 4)
    strLen = len(strFinal)
    if strLen < codeLength:
        strFinal.extend(['0']*codeLength)

    return ''.join(strFinal[:4]) 

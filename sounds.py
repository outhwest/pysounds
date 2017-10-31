##def Soundex(strInit):
##    group1 = ('b', 'f', 'p', 'v')
##    group2 = ('c', 'g', 'j', 'k', 'q', 's', 'x', 'z')
##    group3 = ('d', 't')
##    group4 = ('l',)
##    group5 = ('m', 'n')
##    group6 = ('r',)
##    
##    strFinal = [strInit[0]]
##    formerValue = 0
##    curValue = 0
##    for letter in strInit[1:]:
##        if letter == ' ':
##            curValue = '0'
##        elif letter in group1:
##            curValue = '1'
##        elif letter in group2:
##            curValue = '2'
##        elif letter in group3:
##            curValue = 3
##        elif letter in group4:
##            curValue = 4
##        elif letter in group5:
##            curValue = 5
##        elif letter in group6:
##            curValue = 6
##        if curValue != formerValue:
##            if curValue != 0:
##                strFinal.append(curValue)
##            formerValue = curValue
##    if len(strFinal) == 1:
##        strFinal.append(['0','0', '0'])
##    elif len(strFinal) == 2:
##        strFinal.append(['0', '0'])
##    elif len(strFinal) == 3:
##        strFinal.append('0')
##
##    return str(strFinal[:4])

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
    strFinal = [strInit[0]]
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

def Soundex(strInit):
    group1 = ('b', 'f', 'p', 'v')
    group2 = ('c', 'g', 'j', 'k', 'q', 's', 'x', 'z')
    group3 = ('d', 't')
    group4 = ('l',)
    group5 = ('m', 'n')
    group6 = ('r',)
    
    strFinal = [strInit[0]]
    formerValue = 0
    curValue = 0
    for letter in strInit[1:]:
        if letter == ' ':
            curValue = '0'
        elif letter in group1:
            curValue = '1'
        elif letter in group2:
            curValue = '2'
        elif letter in group3:
            curValue = 3
        elif letter in group4:
            curValue = 4
        elif letter in group5:
            curValue = 5
        elif letter in group6:
            curValue = 6
        if curValue != formerValue:
            if curValue != 0:
                strFinal.append(curValue)
            formerValue = curValue
    if len(strFinal) == 1:
        strFinal.append('0','0', '0')
    elif len(strFinal) == 2:
        strFinal.append('0', '0')
    elif len(strFinal) == 3:
        strFinal.append('0')

    return str(strFinal[:4])

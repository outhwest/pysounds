from itertools import islice

def Soundex(strInit, codeLength=4, start=False):
    
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
    strInit = strInit.lstrip()
    if not start:
        strFinal = [strInit[0]]
    strInit = strInit.lower()
    formerVal = 7
    curVal = 7
    inGroups = False
    for idx, group in enumerate(groups):
        if strInit[0] in group:
            formerVal = idx
            inGroups = True
            if start:
                strFinal = [str(idx)]
    if start and not inGroups:
        strFinal = ['A']
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

def getNGrams(source, n):
    for i in range(len(source)- n + 1):
        yield ''.join(islice(source, i, i + n))

def Metaphone(strInit, initialVowel=True):
    strInit = strInit.upper()
    twoGrams = getNGrams(strInit, 2)
    threeGrams = getNGrams(strInit, 3)
    vowels = "AEIOU"
    #previous and current 2Grams
    twos = [None, next(twoGrams)]
    #previous two and current 3Grams
    threes = [None, None, next(threeGrams)]

    #Deal with the first letter logic
    initialDict = {
        'KN': 'N',
        'GN': 'N',
        'PN': 'N',
        'AE': 'E',
        'WR': 'R'
        }
    
    if twos[1] in initialDict:
        finalList = [initialDict[twos[1]]]
        twos[0] = twos[1]
        try:
            twos[1] = next(twoGrams)
        except:
            twos[1] = None
        threes[1] = threes[2]
        try:
            threes[2] = next(threeGrams)
        except:
            threes[2] = None
    else:
        if initialVowel or (strInit[0] not in vowels):
            finalList = [strInit[0]]
        #ie initialVowel=False and first letter is a value
        else:
            finalList = ['A']

    #after special casing first letter, rest of word is the same
    for c in strInit[1:]:
        #increment the previous ngrams lists so that c is in each ngram
        twos[0] = twos[1]
        threes[0] = threes[1]
        threes[1] = threes[2]
        try:
            twos[1] = next(twoGrams)
        except:
            twos[1] = None
        try:
            threes[2] = next(threeGrams)
        except:
            threes[2] = None
        
        # Check for duplicate adjacent letters and skip when at the second
        if c != 'C' and twos[0] == c*2:
            continue
        if c == 'G':
            pass

    return ''.join(finalList)

def isHomophone(a,b, algorithm=Soundex):
    return algorithm(a) == algorithm(b)

from itertools import islice

### @package sounds
##    @brief Module providing the usual phonetic algorithms
##
##    The goal here is to find homophones using some of the established
##    phonetic algorithms like Soundex, Metaphone, Double Metaphone, etc.
##
##    Future expansion could involve syllable counting and reading levels
##    comparable to Flesch-Kincaid from MS Word
##
    

###    @brief Straightforward implementation of a generalized Soundex algorithm
##
##    strInit is used to generate a code of length codeLength where consonantal
##    sounds are turned into numbered symbols representing like sounds
##
##    @param start False allows the usual Soundex property where the first letter
##    of the code is the first letter of the initial string. Setting to True means
##    the entire code will be digits in the case of a leading consonant, or else
##    a leading 'A' for a leading vowel
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

### @brief Helper function to get character-level n-grams from a source str
##
##  For example, getNGrams("Hello",2) should return a generator for:
##  "He", "el", "ll", "lo"
def getNGrams(source, n):
    for i in range(len(source)- n + 1):
        yield ''.join(islice(source, i, i + n))

### @brief Attempting to implement original Metaphone algorithm
##
##  See a verbal description https://en.wikipedia.org/wiki/Metaphone and
##  some BASIC code http://aspell.net/metaphone/metaphone.basic
##
##  @param initialVowel True differentiates leading vowels, while False
##  forces all leading vowels to "A"
##        
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

### @brief comparison function to put the phonetic algorithms to use
##
##  For now, algorithm is meant to be Soundex or Metaphone or a partial
##  function of either to account for their optional arguments
##  lambda functions could also be passed in for example lambda x: x
##  so truth would only be if they match exactly, case and all
def isHomophone(a,b, algorithm=Soundex):
    return algorithm(a) == algorithm(b)

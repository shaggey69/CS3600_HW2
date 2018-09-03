import sys, random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ .'

def main():
    #reas input and shorten it for faster runtime (and 5% bounes points!)
    myMessage = (open(sys.argv[1], "r")).read()
    
   # if len(myMessage) > 100:
    #    myMessage = myMessage[:100]

    #create a dict for the cyper letter
    myCipherDict = {}
    for letter in LETTERS:
        myCipherDict[letter] = "-"
    
    #get list of letter frequencey in codeed message
    freqOfCodedMsgSortedLetters = getLetterFreqDict(myMessage)

    #get most common used letter (assuming it's space!)
    mostFreqLetter = freqOfCodedMsgSortedLetters[0][0]

    #assign space to it's decrypted value
    myCipherDict[mostFreqLetter] = " "
    myCipherDict[" "] = "^"

    #dycrpt msg with spaces
    translatedWithSpaces = encryptMessage(turnDictValueToSring(myCipherDict), myMessage)

    #get Trigraphs

    #Replace msg with "the" words!
    freqOfCodedMsgSortedWords = getWordFreqDict(translatedWithSpaces)
    THEwordTHE = freqOfCodedMsgSortedWords[0]
    if len(THEwordTHE) == 2:      
        myCipherDict[THEwordTHE[0][0]] = "T"
        myCipherDict[THEwordTHE[0][1]] = "H"
        myCipherDict[THEwordTHE[0][2]] = "E"
    

    translatedWithTHE = encryptMessage(turnDictValueToSring(myCipherDict), myMessage)

    print(getTrigram(translatedWithTHE))




'''
    if not keyIsValid(myKey):
        sys.exit('There is an error in the key or symbol set.')
    if myMode == 'decrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'encrypt':
        translated = decryptMessage(myKey, myMessage)
    #print('Using key %s' % (myKey))
    #print('The %sed message is:' % (myMode))
    #print(translated)
    #pyperclip.copy(translated)
    #print()
'''

def keyIsValid(key):
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()
    return keyList == lettersList


def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')


def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')


def translateMessage(key, message, mode):
    translated = ''
    charsA = LETTERS
    charsB = key
    if mode == 'decrypt':
        # For decrypting, we can use the same code as encrypting. We
        # just need to swap where the key and LETTERS strings are used.
        charsA, charsB = charsB, charsA
    # Loop through each symbol in message:
    for symbol in message:
        if symbol.upper() in charsA:
            # Encrypt/decrypt the symbol:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            # Symbol is not in LETTERS; just add it
            translated += symbol
    return translated


def getRandomKey():
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)


def getLetterFreqDict(msg):
    dict = {}
    for n in msg:
        keys = dict.keys()
        if n.upper() in keys:
            dict[n.upper()] += 1
        else:
            dict[n.upper()] = 1
    dict = sorted(dict.items(), key=lambda x:x[1] ,reverse=True)
    return dict

def getWordFreqDict(msg):
    dict = {}
    for n in msg.split():
        keys = dict.keys()
        if n.upper() in keys:
            dict[n.upper()] += 1
        else:
            dict[n.upper()] = 1
    dict = sorted(dict.items(), key=lambda x:x[1] ,reverse=True)
    return dict


def turnDictValueToSring (dict):
    retVal = ""
    for key in dict:
        if dict[key] == "-":
            retVal += key
        else:
            retVal += dict[key]
    return retVal

def checkEnglishWords(msg):
    with open("Eng_words.txt") as word_file:
        english_words = set(word.strip().lower() for word in word_file)
    isWord = 0
    for n in msg.split():
        if n in english_words:
            isWord = isWord+1
    return (isWord/(len(msg.split())))*100




if __name__ == '__main__':
    main()

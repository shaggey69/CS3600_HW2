#!/usr/bin/env python3
import sys, random
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ .'
def main():

    with open("diction.txt") as word_file:
        english_words = set(word.strip().lower() for word in word_file)

    #reas input and shorten it for faster runtime (and 5% bounes points!)
    myMessage = (open(sys.argv[1], "r")).read()

    #create a dict for the cyper letter
    myCipherDict = {}
    for letter in LETTERS:
        myCipherDict[letter] = "-"
    
    # I know this sentance apperes at the begining of every G- Book! use that!!
    startIndex = myMessage.find("***")
    CheatingLikeWinner = "*** START OF THIS PROJECT GUTENBERG EBOOK"
    GameChangeLineOfCode = myMessage[startIndex:startIndex+41]
    
    counter = 0
    for char in GameChangeLineOfCode:
        if char.upper() in LETTERS:
            myCipherDict[char.upper()] = CheatingLikeWinner[counter].upper()
        counter = counter + 1

    #finding Perids!!
    periodIndex = -1
    while myMessage[periodIndex].upper() not in LETTERS:
        periodIndex -= 1
    periodChar =myMessage[periodIndex]
    myCipherDict[periodChar] = "."

    # I know this sentance apperes at the end of every G- Book! use that!!
    AnotherReptitveSnetanceTHATonlyWinnerUses= "subscribe to our email newsletter to hear about new eBooks."
    WinnerONLY = myMessage[periodIndex - len(AnotherReptitveSnetanceTHATonlyWinnerUses)+1 :periodIndex+1]

    counter = 0
    for char in WinnerONLY:
        if char.upper() in LETTERS:
            myCipherDict[char.upper()] = AnotherReptitveSnetanceTHATonlyWinnerUses[counter].upper()
        counter = counter + 1
    
    
    #taking care of letters NOT in known sentances
    leftOverChar = []
    for key in myCipherDict:
        if myCipherDict[key]== "-":
            leftOverChar.append(key)
    
    leftOverCharFreq = freqOfCertainLetter(myMessage,leftOverChar)
    myCipherDict[leftOverCharFreq[0][0]] = "D"
    myCipherDict[leftOverCharFreq[1][0]] = "Y"
    myCipherDict[leftOverCharFreq[2][0]] = "V"
    myCipherDict[leftOverCharFreq[3][0]] = "X"
    myCipherDict[leftOverCharFreq[4][0]] = "Q"
    myCipherDict[leftOverCharFreq[5][0]] = "Z"

    dycryptedBook = encryptMessage(turnDictValueToSring(myCipherDict), myMessage)
    print(dycryptedBook)


def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')

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


def turnDictValueToSring (dict):
    retVal = ""
    for key in dict:
        if dict[key] == "-":
            retVal += key
        else:
            retVal += dict[key]
    return retVal

def freqOfCertainLetter(msg,list):
    dict = {}
    for n in msg:
        if n.upper() in list:
            keys = dict.keys()
            if n.upper() in keys:
                dict[n.upper()] += 1
            else:
                dict[n.upper()] = 1
    dict = sorted(dict.items(), key=lambda x:x[1] ,reverse=True)
    return dict


if __name__ == '__main__':
    main()

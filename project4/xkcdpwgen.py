#!/usr/bin/env python

import sys, random, getopt

symbolsList = ["~","!","@","#","$","%","^","&","*",".",":",";"]
numbersList = ["0","1","2","3","4","5","6","7","8","9"]
lines = open('words.txt').read().splitlines()

def getRandom(val, options):
    res = []
    for i in range(val):
        res.append(random.choice(options))
    return res

def buildPassword(wordsVal, capitalsVal, numbersVal, symbolsVal):
    #print("wordsVal: ", wordsVal, " capitalsVal: ", capitalsVal, "numbersVal: ", numbersVal, " symbolsVal: ",symbolsVal)
    pwdList = []
    pwdList += getRandom(wordsVal, lines)
    for i in range(capitalsVal):
        if (i >= wordsVal):
            break
        pwdList[i] =pwdList[i].capitalize()
    pwdList += getRandom(numbersVal, numbersList)
    pwdList += getRandom(symbolsVal, symbolsList)
    random.shuffle(pwdList)
    pwd = ''.join(pwdList)
    return (pwd)   


def getIntFromInput(input):
    try:
        return int(input)
    except ValueError:
        print("parameters should be integers")

def generatePassword(argv):
    wordsVal, capitalsVal, numbersVal, symbolsVal = 4, 0, 0, 0
    try:
      opts, args = getopt.getopt(argv,"hw:c:n:s:",["words=", "caps=", "numbers=", "symbols=", "help"])
    except getopt.GetoptError:
      print('try again')
      sys.exit(2)
    for opt, arg in opts:
        if opt == '-w' or opt == "--words":
            wordsVal = getIntFromInput(arg)
        elif opt == '-c' or opt == "--caps":
            capitalsVal = getIntFromInput(arg)
        elif opt == '-n' or opt == "--numbers":
            numbersVal = getIntFromInput(arg)
        elif opt == '-s' or opt == "--symbols":
            symbolsVal = getIntFromInput(arg)
        elif opt == '-h' or opt == "--help":
            return("usage: xkcdpwgen [-h] [-w WORDS] [-c CAPS] [-n NUMBERS] [-s SYMBOLS] \n\n" +
                "Generate a secure, memorable password using the XKCD method\n"+
                "optional arguments:"+
                "-h, --help\t\tshow this help message and exit\n" +
                "-w WORDS, --words WORDS\t\t include WORDS words in the password (default=4)\n"+
                "-c CAPS, --caps CAPS\t\tcapitalize the first letter of CAPS random words (default=0)\n" + 
                "-n NUMBERS, --numbers NUMBERS\t\tinsert NUMBERS random numbers in the password (default=0)\n" +
                "-s SYMBOLS, --symbols SYMBOLS\t\t insert SYMBOLS random symbols in the password(default=0)\n")
    return buildPassword(wordsVal, capitalsVal, numbersVal, symbolsVal)


if __name__ == "__main__":
    print(generatePassword(sys.argv[1:]))

import elements as el
import sys
from pathlib import Path

def checkStrCanBeParsedAsInt(entryString: str):
      
    # check if int(entryString) won't raise a ValueError, but unlike isdigit() or similar will accept negative numbers.
	entryStringStripped = entryString.strip() # newline characters affect the .isdigit() method but not the int() function.

	if len(entryStringStripped) <= 1: # using .isdigit() on an empty string returns False, so no need for a separate check from a single character. 
		return entryStringStripped.isdigit()
	elif entryStringStripped[0].isdigit() or entryStringStripped[0] == "-":
		return entryStringStripped[1:].isdigit()
	else:
		return False

def parseDifficultyFile(filename: str):
    
    # correct file format: name|int
    elementList = []
    errorLine = "" # default value should exist to be overwritten if necessary
    nameIndex, difficultyIndex, minimumSizeOfList = 0, 1, 2 # name and difficulty are attributes of the HeistElement class. List size must have a minimum of both indices to make HeistElement.

    try:
        filePath = Path(__file__).with_name("userInputFiles") / (filename + ".txt")
        fileToRead = filePath.open("r")
        for line in fileToRead:
            splitLine = line.split("|")
            
            if len(splitLine) < minimumSizeOfList:
                errorLine = line
                raise IndexError("Incorrectly formatted line, could not get difficulty, check if | present")
            elif checkStrCanBeParsedAsInt(splitLine[difficultyIndex]) == False:
                errorLine = line
                raise ValueError("Incorrectly formatted difficulty value")
            
            elementList.append(el.HeistElement(splitLine[nameIndex], int(splitLine[difficultyIndex])))

        fileToRead.close()
    except (IndexError, ValueError) as error:
        errorMessage = "Error in file " + filename + ": " + errorLine.strip() + "\n"
        sys.exit(errorMessage + repr(error))

    return elementList

def parseDefenseFile(filename: str):
    
    # correct file format: title|name1,name2,...nameN|int1,int2,...intN
    titleIndex, namesIndex, probabilitiesIndex, mimimumListSize = 0, 1, 2, 3 # See Defense class in elements.py for first 3 variables, 4th is the size of the list needed to make a Defense object.
    defenseList = []
    
    try:
        filePath = Path(__file__).with_name("userInputFiles") / (filename + ".txt")
        fileToRead = filePath.open("r")
        for line in fileToRead:
            splitLine = line.split("|")

            if len(splitLine) < mimimumListSize:
                raise IndexError("Incorrectly formated file")
            
            splitLine[namesIndex], splitLine[probabilitiesIndex] = splitLine[namesIndex].split(","), splitLine[probabilitiesIndex].split(",")

            for i in range(len(splitLine[probabilitiesIndex])):
                if splitLine[probabilitiesIndex][i].strip().isdigit() == False:
                    raise ValueError("Probabilities were not a number!")
                splitLine[probabilitiesIndex][i] = int(splitLine[probabilitiesIndex][i])

            defenseList.append(el.Defence(splitLine[titleIndex], splitLine[namesIndex], splitLine[probabilitiesIndex]))

    except (IndexError, ValueError) as error:
        sys.exit("Defense file could not be parsed: " + repr(error))

    return defenseList

def parseIntegerParameterArgs(intArgs: str, listToUpdate: list):
    separatedArgs = intArgs.split("+")
    smallerList = min(len(separatedArgs), len(listToUpdate))
    for i in range(smallerList):
        if checkStrCanBeParsedAsInt(separatedArgs[i]):
            listToUpdate[i] = int(separatedArgs[i])
        elif separatedArgs[i] != "":
            print("Arg '" + separatedArgs[i] + "' could not be parsed as int, using default value of " + str(listToUpdate[i]) + " instead.")
    return listToUpdate

def parseFilenameArgs(strArgs: str, listToUpdate: list):
    separatedArgs = strArgs.split("+")
    smallerList = min(len(separatedArgs), len(listToUpdate))
    for i in range(smallerList):
        if separatedArgs[i] != "":
            listToUpdate[i] = separatedArgs[i]
    return listToUpdate
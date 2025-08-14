from random import randint
from typing import List

class HeistElement:
    # basically just exists for readability
    def __init__(self, name: str, difficulty: int):
        self.name = name
        self.difficulty = difficulty

class Defence:
     
    def __init__(self, name: str, defenceNames: List[str], probability: List[int]):   

        if len(defenceNames) != len(probability):
            raise IndexError("Argument lists of inequal sizes")
        elif len(probability) == 0:
            raise IndexError("Argument lists empty")
        
        rollTable = [probability[0]]
        for i in range(1, len(probability)):
            rollTable.append(rollTable[i-1] + probability[i])
        
        self.name = name # category of the defense, eg. "Guards" or "Sensors"
        self.defenceNames = defenceNames # individual defense names, eg. if the name is "Guards", we might have "Number of Guards", "Equipment", "Training"
        self.rollTable = rollTable # this is an implicitly sorted list

    def __roll(self):
        roll = randint(1, self.rollTable[-1])
        for i in range(len(self.rollTable)):
            if roll <= self.rollTable[i]:
                return i
            
    def __generateDefenses(self, numRolls: int):
        
        numberOfDefenses = [0] * len(self.defenceNames)

        for _ in range(numRolls):
            defenceAdded = self.__roll()
            numberOfDefenses[defenceAdded] += 1

        return dict(zip(self.defenceNames, numberOfDefenses))
    
    def generateString(self, num: int):
        
        readout = self.name + " " + " "*(9-len(self.name)) + str(num) + "| "
        randomDefenses = self.__generateDefenses(num)
        for defense, count in randomDefenses.items():
            toAdd = defense + ": " + str(count)
            whiteSpace = " " + " " * (15-len(toAdd))
            toAdd = toAdd+whiteSpace
            readout = readout + toAdd

        return readout
import sys
from random import choice, randint
import parsing as pr

# args + constants
inputArgs = sys.argv[1:3] # argv[0] == cyberpunkHeistGen.py argv[1] == #+# argv[2] == str+str+str
INDEX_PARAMETER_ARGS, INDEX_FILENAME_ARGS = 0, 1
BASE_REWARD_VALUE_DEFAULT, REWARD_ROUNDING_VALUE_DEFAULT = 1500, 50 # average monthly individual wage and lowest increment the GM wants to assign reward $ in
TYPICAL_NUM_HEISTERS = 3

# default values
filenames = ["corps", "jobs", "defenses"]
corpFileName, jobFileName, defenseFileName = filenames
rewardParameters = [BASE_REWARD_VALUE_DEFAULT, REWARD_ROUNDING_VALUE_DEFAULT]
baseReward, rewardRounding = rewardParameters

# update default values to be args IF they are valid, else ignore. Only attempt if index exists.
if len(inputArgs) >= 1: baseReward, rewardRounding = pr.parseIntegerParameterArgs(inputArgs[INDEX_PARAMETER_ARGS], rewardParameters)
if len(inputArgs) == 2: corpFileName, jobFileName, defenseFileName = pr.parseFilenameArgs(inputArgs[INDEX_FILENAME_ARGS], filenames)

corpList = pr.parseDifficultyFile(corpFileName)
jobList = pr.parseDifficultyFile(jobFileName)
defenseList = pr.parseDefenseFile(defenseFileName)

while (True):

    selectedCorp, selectedJob = choice(corpList), choice(jobList)

    # combined difficulty score of the current job
    difficulty = int(selectedCorp.difficulty) + int(selectedJob.difficulty)

    # factor of 0.9-3.2~, as jobs get exponentially more involved ($1,500 - $27,900 using default reward and rounding values). 2.25 is a purely arbitrary number that produces a nice looking reward curve.
    reward = round((((difficulty/TYPICAL_NUM_HEISTERS)**2.25)*baseReward)/rewardRounding)*rewardRounding

    # generate the balance of the types of defences, assuming equal priority.
    defensesToGen = [0] * len(defenseList)
    for i in range(difficulty):
        defensesToGen[randint(0,len(defenseList)-1)] += 1

    # Output
    print("Target: " + selectedCorp.name + "\nContract Type: " + selectedJob.name + 
          "\nDifficulty mod: " + str(difficulty) + "\nReward: $" + str(reward))
    
    for i in range(len(defenseList)):
        print(defenseList[i].generateString(defensesToGen[i]))

    print("Generate a new heist?")

    if input().lower() not in ("y", "yes"): break

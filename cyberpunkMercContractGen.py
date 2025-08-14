import sys
from random import choice, randint
import parsing as pr

# args + constants
inputArgs = sys.argv[1:3] # argv[0] == cyberpunkHeistGen.py argv[1] == #+# argv[2] == str+str
INDEX_PARAMETER_ARGS, INDEX_FILENAME_ARGS = 0, 1
BASE_REWARD_VALUE_DEFAULT, REWARD_ROUNDING_VALUE_DEFAULT = 1500, 50 # average monthly individual wage and lowest increment the GM wants to assign reward $ in

# default values
filenames = ["corps", "jobs"]
corpFileName, jobFileName = filenames
rewardParameters = [BASE_REWARD_VALUE_DEFAULT, REWARD_ROUNDING_VALUE_DEFAULT]
baseReward, rewardRounding = rewardParameters

# update default values to be args IF they are valid, else ignore. Only attempt if index exists.
if len(inputArgs) >= 1: baseRewardValue, rewardRounding = pr.parseIntegerParameterArgs(inputArgs[INDEX_PARAMETER_ARGS], rewardParameters)
if len(inputArgs) == 2: corpFileName, jobFileName = pr.parseFilenameArgs(inputArgs[INDEX_FILENAME_ARGS], filenames)

corpList = pr.parseDifficultyFile(corpFileName)
incidentList = pr.parseDifficultyFile(jobFileName)

while (True):

    selectedCorp = choice(corpList)
    contractWeeks = randint(1,4) # 1d4, up to "one business month"

    numSquads = 1
    for i in range(selectedCorp.difficulty):
        if (randint(1,10)<selectedCorp.difficulty): numSquads += 1 # roll 1d10 vs. difficulty score

    pay = round(((baseReward/2.5) * (selectedCorp.difficulty**1.5))/rewardRounding)*rewardRounding # 10 people in a squad / 4 weeks in a month = 2.5x monthly individual wages/squad/week, 1.5 is arbitrary

    incidents = []
    for i in range(round(contractWeeks * 1.5)): # 1.5 is arbitrary.
        if randint(1,12) < selectedCorp.difficulty: # 1d12
            selectedIncident = choice(incidentList)
            incidents.append(selectedIncident.name + ", relevant skill " + ("" if selectedIncident.difficulty > 0 else "+") + str(selectedIncident.difficulty*-1))

    print("Client: " + selectedCorp.name + " (difficulty " + str(selectedCorp.difficulty)
        + ")\nContract length: " + str(contractWeeks) + " business weeks\nWeekly pay per squad: $" + str(pay) + "\nNumber of squads: " + str(numSquads)
        + "\nSquads are " + choice(["strength-equivalent", "numerical-equivalent"]) + " " + choice(["(negotiable)","(non-negotiable)"]) + "\nTotal incidents: " + str(len(incidents)))
    for incident in incidents: print(incident)

    print("Generate another contract?")
    if input().lower() not in ("yes", "y"): break
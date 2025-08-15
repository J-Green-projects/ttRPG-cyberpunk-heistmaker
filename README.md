This is the combined README for both the heist generator and the mercenary contract generator. Please refer to the individual READMEs for a more tailored rundown if you only want that information.

## Quick Start Guide

The basic operation of both programs is to generate a series of challenges (or just costs) and a suitable cash reward for adventurers from an abstract difficulty number using a series of tables and an equation that would be too cumbersome to pull out during play. Both programs are setting and system agnostic, and so with the right tables could generate any dungeon or "guard this building" contract. Both programs can be run without any special command line arguments, but will default to "$1500 is a reasonable amount for a person to make in a month", "I care about rounding to the nearest $50, $50 is actually relevant to my players", and "I want to use the default table files."

### Anatomy of the commands

reward_factor = the amount of money a character should be making in a month, or whatever factor produces rewards that will entice your PCs.<br />
reward_rounding = Round to the nearest factor of this number. Eg. a rounding factor of 50 means $1726 rounds to $1750, a factor of 500 means it rounds to $1500.<br />
corp_file = filename of the potential opponents/employers of your players, without file extension (.txt only!)<br />
job_file = as above, but for the type of tasks you intend your players to accomplish.<br />
defence_file = as above, but for the types of traps and enemies your players might encounter on a heist. This file is only used by cyberpunkHeistGen.py<br />

the command for the heist generator:<br />
python cyberpunkHeistGen.py reward_factor+reward_rounding corp_file+job_file+defence_file<br />
eg. for a base reward of $3000, a rounding factor of $100, and files called corps2, jobs2, and defences2:<br />
python cyberpunkHeistGen.py 3000+100 corps2+jobs2+defenses2

the command for the mercenary contract generator:<br />
python cyberpunkMercContractGen.py reward_factor+reward_rounding corp_file+job_file<br />
eg. using the same values as our heist generator example:<br />
python cyberpunkMercContractGen.py 3000+100 corps2+jobs2

In order to use the default value for some, but not all of these parameters, simply include the + but no actual text. In both cases, the filename section can be omitted, but you have to have something for the rewards.

eg.<br />
python cyberpunkHeistGen.py + corps2++defences2<br />
is interpreted as "use the default value for reward_factor, reward_rounding, change corp_file to corps2, use the default value for job_file, change defense_file to defenses2"<br />
python cyberpunkHeistGen +100<br />
is interpeted as "use the default value for reward_factor, change reward_rounding to 100, use the default value for the table files"

### Table files
The .txt files in the userInputFiles folder are representative of tables being rolled on. Some example files have been included, and use the default filenames. If you're only using these programs for one game/setting, just edit these files rather than use entirely new ones.<br />
corps.txt and jobs.txt use the same structure: "name of thing"|difficulty_number.<br />
It's assumed that for corps.txt difficulty_number goes from 3-8, where 3 is "basically a small business" and 8 is "the most dangerous megacorp in your setting". For jobs.txt it runs from -2 to 3, where -2 is "you might need to go past the front lobby" and 3 is "get to the heart of the facility undetected."<br />
defences.txt uses the structure "category of defence"|"specific defence", "specific defence 2"|chance_of_thing_one, change_of_thing_2<br />
This one is more complicated. The chance represents sides of a die. Using the example file:<br />
Sensors|Cameras,RADAR,ECM Detector,Proximity Sensor,Seismic Sensor|5,1,1,1,1<br />
Cameras are rolled on a 1-5, RADAR on a 6, ECM on a 7, Proximity on an 8, and Seismic sensors on a 9, on a 9-sided die. It's easier to use integer percentage probability values, like "56,11,11,11,11" and to just consider this a 100-sided die roll, but this isn't mandatory.

### The output
The output of this program is enough information to draft up a whole encounter/dungeon if you want to draw maps, but the intent was for heists that could be abstracted to a few rolls. The reason for this program is that in order to do more complicated and difficult heists with big set pieces, they needed money, and as professional heisters, that money was going to come from heists. I wanted something more complicated than a simple "did you do your job?" roll, but could still be accomplished in 5-10 minutes so as not to eat into the time for things that I had actually prepared in depth. I also wanted to give them options for these jobs, as opposed to just telling them what their characters did. See the individual READMEs for specifics of interpretation and what information you should give your players and the specific text outputs of each program.

- Running the program -

This program needs 3 .txt files to run correctly. These specify the players' opponents, their mission, and the hazards they face.
These files are by default "corps.txt", "jobs.txt", and "defenses.txt".

The default command to run the program from your command line is: python cyberpunkHeistGen.py

You can change the reward modifier, reward rounding factor, corp file, job file, and defense file. The structure of the argument is as follows:

python cyberpunkHeistGen.py reward_modifier+reward_rounding_factor corp_filename+job_filename+defense_filename

The default reward modifier is 1500, and the default reward rounding factor is 50.

In order to change just the filenames, you will need to include one + delimiter prior to the string of filenames, eg.

python cyberpunkHeistGen.py + corps2+jobs2+defenses2

Or if you just wanted to change the corps and defenses file, you would instead write python cyberpunkHeistGen.py + corps2++defenses2

Once running, the program will automatically generate one heist, and ask if you would like to repeat another.
If you like the heist, copy/paste it somewhere convenient before entering anything. If not, enter "yes" or "y" to generate another heist, or anything else to exit the program.
The program does not have an internal save function. This is because the expectation is that the user will generate 10 or so heists and pick their favourites.
Asking to save each time would cost more time and effort than just copy/pasting.

- Interpreting the output -

Your file will have an output that looks something like this:

Target: ACME Corporation
Contract Type: some task
Difficulty mod: X
Reward: $someNumber
Sensors   X| Cameras: X      RADAR: X        Proximity Detector: X 
Traps     X| Laser Grid: X   Locks: X        Turrets: X      
Guards    X| Guard Count: X  Kit: X          Skill: X

Target is the opponent generated. Contract Type is the task performed.
"Why would someone pay for this task to be performed against the opponent?" is left up to the GM.
Reward is the payment, and works off of the assumption that average monthly pay is $1500 per person, and that normally each heist requires at least three people.
The number of people on a heist is impossible to fully account for given the range of power levels of heisters in any given setting.
This can be remedied by simply changing the reward factor by the number of heisters expected in general by the setting. 
Eg. 5 heisters = multiply the desired reward modifier by 5/3.
Reward modifier is the first argument, and is designed to be as easy to change as possible.
If the reward modifier is high, change the rounding factor to work with easier numbers - 50 is quite granular and intended for a gritty setting.

Target, contract type, and reward should be provided to the players. Difficulty should not be provided as a number, but as a vague descriptor.

The individual defenses are split into categories by line, and category totals are provided. The numbers represent "overall level of threat", not individual counts.
If something does not appear, that means it isn't a threat that requires a roll from the players to avoid, rather than "it just isn't there". The sample readout includes 
locks and cameras, which are present in any modern building. What a 0 would mean is a roll with a substantial bonus (outdated, easy to bypass locks), or cameras on a visible 
swivel that can be evaded like a stealth section in a video game: just by looking and moving slowly.
On the opposite side of things, Cameras: 4 could represent particularly good placement requiring a penalized stealth roll, or special infrared/multispectral cameras.

- Structure of a file -

Opponent file (default: corps.txt) should consist of nothing but:
example opponent name|X

Where X is some integer between 3 and 8. The higher the number, the stronger the opponent and the more intense their defenses.

Task file (default: jobs.txt) should consist of nothing but:
example task name|Y

Where Y is some integer between -2 and 3. The higher the number, the more difficult the task and the more likely you are to encounter defenses.

X + Y = difficulty = number of defenses in total -> how much players get rewarded.

As long as X + Y cannot equal 0 or less, and don't go too far past 11, the specifics of what they are do not matter too much.
Eg. if every opponent had an X of 6, but Y went from +5 to -5, the balance would remain the same.
If every X went from 5 to 7, and Y from -4 to 4, the balance would again not be affected.

defenses file (default: defenses.txt) should consist of nothing but:
some category|name1, name2,...,nameX|int1,int2...,intX

name1 and int1 are paired.

The way defenses are chosen is essentially the same as a random encounter table. The difficulty level = the number of rolls on this table.
For ease of use, treat intX as being the percent chance nameX is drawn, and make sure all ints add to 100.
The way this table works is that the total of all ints is the size of the die being rolled. A roll of int1 or less = name1 being drawn.
A roll of more than int1 but equal to or less than int1+int2 results in name2 being drawn.
A roll of more than int1+int2 but equal to or less than int1+int2+int3 results in name3 being drawn, and so-on.
With this in mind, you can make your table however you like, but the "treat as percentage and everything adds to 100" is the most human-readable.


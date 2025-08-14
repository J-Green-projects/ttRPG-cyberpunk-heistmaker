- Running the program -

This program needs 2 .txt files to run correctly. These specify the players' employer, and the hazards they face.
These files are by default "corps.txt", and "jobs.txt" 

The default command to run the program from your command line is: python cyberpunkMercContractGen.py

You can change the reward modifier, reward rounding factor, corp file, and job file. The structure of the argument is as follows:

python cyberpunkMercContractGen.py reward_modifier+reward_rounding_factor corp_filename+job_filename

eg. assuming we wanted a reward modifier of 3000, a rounding factor of 1000, and to use a corpfile called corps2.txt and a jobfile named jobs2.txt:
python cyberpunkMercContractGen.py 3000+1000 corps2+jobs2

If you wish to only change the corp/job file, simply include a + prior to the argument, as order is important.
python cyberpunkMercContractGen + corps2+jobs2

Note that to change only the reward factor, you do not need to include a second +, eg.
python cyberpunkMercContractGen 3000+1000
is sufficient

- Interpreting the Output -

Your file will have an output that looks something like this:

Client: ACME corporation (difficulty X)
Contract length X days (X business weeks)
Weekly pay per squad: $X
Number of squads: X
Squads are (strength/numerical)-equivalent (non-negotiable/negotiable)
Total incidents: X
Some job, relevant skill #
...
Some job, relevant skill #

Contract length is the actual amount of time the contract will take, whilst (X business weeks) tells you the number of pay-periods that will occur.
Weekly pay per squad is how much revenue each squad generates per pay period. The default assumption is $1500/month, which may not be what you are looking for.
To modify this without changing the code, use the reward modifier argument. Note that the pay is given on a per-week basis, but is based on a per-month average.
When using much larger numbers, the rounding factor of nearest $50 may prove too granular, and the reward rounding factor argument changes this.

Number of squads is NOT the number of squads required, but rather the abstract representation of an "average squad of infantry".
The line under this tells you how to interpret that. "Numerical" means skill and equipment are irrelevant, whilst "strength" means that they are.
The meaning of "strength" equivalence is that one squad of elite troops is as valuable as a larger number of less elite troops.
The meaning of "numerical" equivalence is that the only thing that matters is how many mercenaries clock in.
This readout can be challenging, because not every system/setting has some kind of obvious objective standard. The basic idea is "The municipal police".
Whether or not a contract is negotiable means whether or not the client is willing to budge on whether the contract is numerical or strength equivalent.
If a contract is negotiable, then it's an unmodified roll against whatever the "business" or "negotiation" skill is in your system to change.
If a contract is non-negotiable, then either the client won't budge because they need something specific, or the negotiation roll is heavily penalized.

Total incidents give the GM a variety of random events for the PCs' troops to deal with. Each incident is dealt with by one roll.
A modifier for that roll is given, but the expectation is that the average modifier works out to 0, so you don't have to use it if it proves cumbersome.

The assumption of modifiers is a 3d6, roll under system. If you are going to convert this number, it can be a little complicated.

If you have a uniform distribution (you're rolling 1 die, eg. D20, D100), each +/- 1 should equal about +/- 5% chance of success (+/- 5 on D100, +/- 1 on D20)
If you have a binomial distribution (a dice pool system), there is not one solution so treating any negative as -1 die, and any positive as +1 die is the safest option.
If you have a normal distribution (2d6, 3d6, 2d10 etc.), the process is more involved but more accurate to intent. Divide the number of dice by 3, and the average roll by 3.5
Multiply these two numbers together, and round towards zero.
2d6 = 2/3 * 3.5/3.5 = 2/3
3d6 = 3/3 * 3.5/3.5 = 1
2d10 = 2/3 * 5.5/3.5 = 1.04 = 1

Make one of these checks each for each incident. Success results in no issue, results of failure are determined by the GM. 
A critical failure is "you get fired", a critical success is "you get paid double", or something roughly equivalent.
On any failure, the GM assigns casualties as is appropriate for their system/game.

- Structure of a file -

Employer file (default: corps.txt) should consist of nothing but:
example employer name|X

Where X is some integer between 3 and 8. The higher the number, the more powerful the employer (and the more likely there are to be incidents)

Incident file (default: jobs.txt) should consist of nothing but:
example task name|Y

Where Y is some integer between -2 and 3. The higher the number, the more difficult the task is to perform (and the worse it is if successful!)
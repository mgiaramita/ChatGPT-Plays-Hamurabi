[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://black.readthedocs.io/en/stable/_static/license.svg)](https://github.com/psf/black/blob/main/LICENSE)

# ChatGPT Plays Hammurabi

```
   ____ _           _    ____ ____ _____                  
  / ___| |__   __ _| |_ / ___|  _ \_   _|                 
 | |   | '_ \ / _` | __| |  _| |_) || |                   
 | |___| | | | (_| | |_| |_| |  __/ | |                   
  \____|_| |_|\__,_|\__|\____|_|    |_|                   
 |  _ \| | __ _ _   _ ___                                 
 | |_) | |/ _` | | | / __|                                
 |  __/| | (_| | |_| \__ \                                
 |_|  _|_|\__,_|\__, |___/                        _     _ 
 | | | | __ _ _ |___/_  _ __ ___  _   _ _ __ __ _| |__ (_)
 | |_| |/ _` | '_ ` _ \| '_ ` _ \| | | | '__/ _` | '_ \| |
 |  _  | (_| | | | | | | | | | | | |_| | | | (_| | |_) | |
 |_| |_|\__,_|_| |_| |_|_| |_| |_|\__,_|_|  \__,_|_.__/|_|
                                                          
```
##### ChatGPT attempts to play through the 1973 version of Hammurabi (aka King of Sumeria / The Sumer Game)

## <sub> What is it?

* Another command line tool for the [OpenAI API - Docs](https://platform.openai.com/docs/introduction).
* Allows ChatGPT to play through the classic game [Hammurabi (1973)](https://en.wikipedia.org/wiki/Hamurabi_(video_game)).
* It will try its best to play through the game. You can continue or stop the game at each step in execution.

```
   ____ _           _    ____ ____ _____                  
  / ___| |__   __ _| |_ / ___|  _ \_   _|                 
 | |   | '_ \ / _` | __| |  _| |_) || |                   
 | |___| | | | (_| | |_| |_| |  __/ | |                   
  \____|_| |_|\__,_|\__|\____|_|    |_|                   
 |  _ \| | __ _ _   _ ___                                 
 | |_) | |/ _` | | | / __|                                
 |  __/| | (_| | |_| \__ \                                
 |_|  _|_|\__,_|\__, |___/                        _     _ 
 | | | | __ _ _ |___/_  _ __ ___  _   _ _ __ __ _| |__ (_)
 | |_| |/ _` | '_ ` _ \| '_ ` _ \| | | | '__/ _` | '_ \| |
 |  _  | (_| | | | | | | | | | | | |_| | | | (_| | |_) | |
 |_| |_|\__,_|_| |_| |_|_| |_| |_|\__,_|_|  \__,_|_.__/|_|
                                                          

ChatGPT and Hammurabi are ready to begin.


Congratulations, you are the newest ruler of ancient Samaria, elected
for a ten year term of office. Your duties are to dispense food, direct
farming, and buy and sell land as needed to support your people. Watch
out for rat infestations and the plague! Grain is the general currency,
measured in bushels. The following will help you in your decisions:

  * Each person needs at least 20 bushels of grain per year to survive.

  * Each person can farm at most 10 acres of land.

  * It takes 2 bushels of grain to farm an acre of land.

  * The market price for land fluctuates yearly.

Rule wisely and you will be showered with appreciation at the end of
your term. Rule poorly and you will be kicked out of office!

O great Hammurabi!
You are in year 1 of your ten year rule.
In the previous year 0 people starved to death.
In the previous year 5 people entered the kingdom.
The population is now 100.
We harvested 3000 bushels at 3 bushels per acre.
Rats destroyed 200 bushels, leaving 2800 bushels in storage.
The city owns 1000 acres of land.
Land is currently worth 19 bushels per acre.
There were 0 deaths from the plague.

How many acres of land will you buy? (0 to DECLINE)

> 10
Tokens In: 380, Tokens Out: 1


How many bushels of grain will you feed to the people?

> 1500
Tokens In: 402, Tokens Out: 2


How many acres of land will you plant with seed?

> 1400
Tokens In: 423, Tokens Out: 2


O great Hammurabi, we have but 100 people that can farm the land!
1400 acres are too many for us! We still need more people to do the job!
Please factor our manpower. Again, how much land will you plant?
[HINT: The maximum possible acres of current total labor force that can afford to farm is 1000 acres.]

> 1000
Tokens In: 508, Tokens Out: 2


O great Hammurabi, we have but 1110 bushels to spend farming the land!
1000 acres are too many for us! We lack enough bushels to start our farming!
Please factor our funds. Again, how much land will you plant with seed?
[HINT: The maximum possible acres of current total funds to spend farming is 555.0 acres.]

> 555
Tokens In: 595, Tokens Out: 1


***O great Hammurabi, unluckily a horrible PLAGUE happened! 50.0 people died***
***O brilliant Hammurabi! This year we have NO people starved***
***O great Hammurabi, this year 5 immigrants come to our kingdom***
***O great Hammurabi, this year we harvest 3330 bushels of grain***
***Thank God! No rat infestation occurred this year***
***O great Hammurabi, the price of land will be 19 bushels per acre next year***

O great Hammurabi!
You are in year 2 of your ten year rule.
In the previous year 0 people starved to death.
In the previous year 5 people entered the kingdom.
The population is now 55.
We harvested 3330 bushels at 6 bushels per acre.
Rats destroyed 0 bushels, leaving 3330 bushels in storage.
The city owns 1010 acres of land.
Land is currently worth 19 bushels per acre.
There were 50 deaths from the plague.

How many acres of land will you buy? (0 to DECLINE)

> 0
Tokens In: 845, Tokens Out: 1


How many acres of land will you sell?

> 0
Tokens In: 863, Tokens Out: 1


How many bushels of grain will you feed to the people?

> 1000
Tokens In: 885, Tokens Out: 2


How many acres of land will you plant with seed?

> 500
Tokens In: 906, Tokens Out: 1


***Thank God! No plague this year***
***O great Hammurabi, unfortunately this year we have 5 PEOPLE STARVED***
***O great Hammurabi, due to starvation, NO IMMIGRANTS this year come to our kingdom***
***O great Hammurabi, this year we harvest 3000 bushels of grain***
***Thank God! No rat infestation occurred this year***
***O great Hammurabi, the price of land will be 23 bushels per acre next year***

O great Hammurabi!
You are in year 3 of your ten year rule.
In the previous year 5 people starved to death.
In the previous year 0 people entered the kingdom.
The population is now 50.
We harvested 3000 bushels at 6 bushels per acre.
Rats destroyed 0 bushels, leaving 4330 bushels in storage.
The city owns 1010 acres of land.
Land is currently worth 23 bushels per acre.
There were 0 deaths from the plague.

How many acres of land will you buy? (0 to DECLINE)

> 0
Tokens In: 1149, Tokens Out: 1


How many acres of land will you sell?

> 0
Tokens In: 1167, Tokens Out: 1


How many bushels of grain will you feed to the people?

> 1000
Tokens In: 1189, Tokens Out: 2


How many acres of land will you plant with seed?

> 500
Tokens In: 1210, Tokens Out: 1


***Thank God! No plague this year***
***O brilliant Hammurabi! This year we have NO people starved***
***O great Hammurabi, this year 5 immigrants come to our kingdom***
***O great Hammurabi, this year we harvest 2000 bushels of grain***
***Thank God! No rat infestation occurred this year***
***O great Hammurabi, the price of land will be 19 bushels per acre next year***

O great Hammurabi!
You are in year 4 of your ten year rule.
In the previous year 0 people starved to death.
In the previous year 5 people entered the kingdom.
The population is now 55.
We harvested 2000 bushels at 4 bushels per acre.
Rats destroyed 0 bushels, leaving 4330 bushels in storage.
The city owns 1010 acres of land.
Land is currently worth 19 bushels per acre.
There were 0 deaths from the plague.

How many acres of land will you buy? (0 to DECLINE)

> 0
Tokens In: 1445, Tokens Out: 1


How many acres of land will you sell?

> 0
Tokens In: 1463, Tokens Out: 1


How many bushels of grain will you feed to the people?

> 1000
Tokens In: 1485, Tokens Out: 2


How many acres of land will you plant with seed?

> 500
Tokens In: 1506, Tokens Out: 1


***O great Hammurabi, unluckily a horrible PLAGUE happened! 27.5 people died***
***O brilliant Hammurabi! This year we have NO people starved***
***O great Hammurabi, this year 9 immigrants come to our kingdom***
***O great Hammurabi, this year we harvest 2000 bushels of grain***
***O great Hammurabi, unluckily a horrible RAT INFESTATION happened! 580 bushels of grain were destroyed***
***O great Hammurabi, the price of land will be 19 bushels per acre next year***

O great Hammurabi!
You are in year 5 of your ten year rule.
In the previous year 0 people starved to death.
In the previous year 9 people entered the kingdom.
The population is now 37.
We harvested 2000 bushels at 4 bushels per acre.
Rats destroyed 580 bushels, leaving 3750 bushels in storage.
The city owns 1010 acres of land.
Land is currently worth 19 bushels per acre.
There were 27 deaths from the plague.

How many acres of land will you buy? (0 to DECLINE)

> 0
Tokens In: 1771, Tokens Out: 1


How many acres of land will you sell?

> 0
Tokens In: 1789, Tokens Out: 1


How many bushels of grain will you feed to the people?

> 1000
Tokens In: 1811, Tokens Out: 2


How many acres of land will you plant with seed?

> 500
Tokens In: 1832, Tokens Out: 1


O great Hammurabi, we have but 37 people that can farm the land!
500 acres are too many for us! We still need more people to do the job!
Please factor our manpower. Again, how much land will you plant?
[HINT: The maximum possible acres of current total labor force that can afford to farm is 370 acres.]

> 370
Tokens In: 1914, Tokens Out: 1


***Thank God! No plague this year***
***O brilliant Hammurabi! This year we have NO people starved***
***O great Hammurabi, this year 7 immigrants come to our kingdom***
***O great Hammurabi, this year we harvest 370 bushels of grain***
***O great Hammurabi, unluckily a horrible RAT INFESTATION happened! 62 bushels of grain were destroyed***
***O great Hammurabi, the price of land will be 22 bushels per acre next year***

O great Hammurabi!
You are in year 6 of your ten year rule.
In the previous year 0 people starved to death.
In the previous year 7 people entered the kingdom.
The population is now 44.
We harvested 370 bushels at 1 bushels per acre.
Rats destroyed 62 bushels, leaving 2318 bushels in storage.
The city owns 1010 acres of land.
Land is currently worth 22 bushels per acre.
There were 0 deaths from the plague.

How many acres of land will you buy? (0 to DECLINE)

> 0
Tokens In: 2162, Tokens Out: 1


How many acres of land will you sell?

> 0
Tokens In: 2180, Tokens Out: 1


How many bushels of grain will you feed to the people?

> 1000
Tokens In: 2202, Tokens Out: 2


How many acres of land will you plant with seed?

> 370
Tokens In: 2223, Tokens Out: 1


***Thank God! No plague this year***
***O brilliant Hammurabi! This year we have NO people starved***
***O great Hammurabi, this year 5 immigrants come to our kingdom***
***O great Hammurabi, this year we harvest 1110 bushels of grain***
***Thank God! No rat infestation occurred this year***
***O great Hammurabi, the price of land will be 21 bushels per acre next year***

O great Hammurabi!
You are in year 7 of your ten year rule.
In the previous year 0 people starved to death.
In the previous year 5 people entered the kingdom.
The population is now 49.
We harvested 1110 bushels at 3 bushels per acre.
Rats destroyed 0 bushels, leaving 1688 bushels in storage.
The city owns 1010 acres of land.
Land is currently worth 21 bushels per acre.
There were 0 deaths from the plague.

How many acres of land will you buy? (0 to DECLINE)

> 0
Tokens In: 2458, Tokens Out: 1


How many acres of land will you sell?

> 0
Tokens In: 2476, Tokens Out: 1


How many bushels of grain will you feed to the people?

> 1000
Tokens In: 2498, Tokens Out: 2


How many acres of land will you plant with seed?

> 410
Tokens In: 2519, Tokens Out: 1


O great Hammurabi, we have but 688 bushels to spend farming the land!
410 acres are too many for us! We lack enough bushels to start our farming!
Please factor our funds. Again, how much land will you plant with seed?
[HINT: The maximum possible acres of current total funds to spend farming is 344.0 acres.]

> 344
Tokens In: 2603, Tokens Out: 1


***Thank God! No plague this year***
***O brilliant Hammurabi! This year we have NO people starved***
***O great Hammurabi, this year 5 immigrants come to our kingdom***
***O great Hammurabi, this year we harvest 1032 bushels of grain***
***O great Hammurabi, unluckily a horrible RAT INFESTATION happened! 154 bushels of grain were destroyed***
***O great Hammurabi, the price of land will be 21 bushels per acre next year***

O great Hammurabi!
You are in year 8 of your ten year rule.
In the previous year 0 people starved to death.
In the previous year 5 people entered the kingdom.
The population is now 54.
We harvested 1032 bushels at 3 bushels per acre.
Rats destroyed 154 bushels, leaving 878 bushels in storage.
The city owns 1010 acres of land.
Land is currently worth 21 bushels per acre.
There were 0 deaths from the plague.

How many acres of land will you buy? (0 to DECLINE)

> 0
Tokens In: 2852, Tokens Out: 1


How many acres of land will you sell?

> 0
Tokens In: 2870, Tokens Out: 1


How many bushels of grain will you feed to the people?

> 1000
Tokens In: 2892, Tokens Out: 2


O great Hammurabi, we have but 878 bushels of grain! 1000 bushels exceed our grain reserves!
Again, how much grain will you feed to the people?
[HINT: In order for everyone to survive, current population needs at least total amount of 1080 bushels.]

> 878
Tokens In: 2965, Tokens Out: 1


How many acres of land will you plant with seed?

> 360
Tokens In: 2985, Tokens Out: 1


O great Hammurabi, we have but 0 bushels to spend farming the land!
360 acres are too many for us! We lack enough bushels to start our farming!
Please factor our funds. Again, how much land will you plant with seed?
[HINT: The maximum possible acres of current total funds to spend farming is 0.0 acres.]

> 0
Tokens In: 3069, Tokens Out: 1


***Thank God! No plague this year***
***O great Hammurabi, unfortunately this year we have 10 PEOPLE STARVED***
***O great Hammurabi, due to starvation, NO IMMIGRANTS this year come to our kingdom***
***O great Hammurabi, this year we harvest 0 bushels of grain***
***O great Hammurabi, unluckily a horrible RAT INFESTATION happened! 0 bushels of grain were destroyed***
***O great Hammurabi, the price of land will be 20 bushels per acre next year***

O great Hammurabi!
You are in year 9 of your ten year rule.
In the previous year 10 people starved to death.
In the previous year 0 people entered the kingdom.
The population is now 44.
We harvested 0 bushels at 7 bushels per acre.
Rats destroyed 0 bushels, leaving 0 bushels in storage.
The city owns 1010 acres of land.
Land is currently worth 20 bushels per acre.
There were 0 deaths from the plague.

How many acres of land will you buy? (0 to DECLINE)

> 0
Tokens In: 3324, Tokens Out: 1


How many acres of land will you sell?

> 0
Tokens In: 3342, Tokens Out: 1


How many bushels of grain will you feed to the people?

> 1000
Tokens In: 3364, Tokens Out: 2


O great Hammurabi, we have but 0 bushels of grain! 1000 bushels exceed our grain reserves!
Again, how much grain will you feed to the people?
[HINT: In order for everyone to survive, current population needs at least total amount of 880 bushels.]

> 0
Tokens In: 3436, Tokens Out: 1


How many acres of land will you plant with seed?

> 0
Tokens In: 3456, Tokens Out: 1


***Thank God! No plague this year***
***O great Hammurabi, unfortunately this year we have 44 PEOPLE STARVED***
***O great Hammurabi, we  really regret to inform you that this year 44 people have been starved, which represent more than 45% of total population in your Samaria kingdom. According to our laws, you're now unfortunately given an immediate dismissal request***
========================== G A M E ===== O V E R ==========================
       O great Hammurabi, we're truly regretful that in year 9 of
       your ten year rule, you lost your imperial authority.

                 *** THANK YOU FOR PLAYING HAMMURABI! ***


TERMINATE CONDITION HIT
```

## <sub> How to install.

* Install the latest version of [Python 3](https://www.python.org/downloads).
* Install the OpenAI [Python package](https://pypi.org/project/openai).
* Install [pexpect](https://pypi.org/project/pexpect) to control the Oregon Trail process. 
* Clone the repo.
* Hammurabi can be installed in a number of ways and it depends on your system.
  * Easy to use [Python2 version.](https://github.com/wzhishen/hammurabi)
  * Updated [Python3 version.]()
  * [c port](https://github.com/beyonddream/hamurabi) (untested).

## <sub> How to use.

* Add your OpenAI API key to <b>config.ini</b>.
* Ensure the Hammurabi command in <b>config.ini</b> is correct or update it for your specific install.
* python3 chatgpt_plays_hammurabi.py
  * Run default application.
* python3 chatgpt_plays_hammurabi.py -h
  * Display help message.
* python3 chatgpt_plays_hammurabi.py -m "gpt-4"
  * Use model "gpt-4".
* python3 chatgpt_plays_hammurabi.py -U
  * UNLEASHED mode. This lets ChatGPT play without user interaction until OT process terminates.

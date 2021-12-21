# ANCIENT_INVASION

"Ancient Invasion" is an offline turn-based strategy RPG inspired by "Summoners War: Sky Arena" 
(https://play.google.com/store/apps/details?id=com.com2us.smon.normal.freefull.google.kr.android.common&hl=en&gl=US)
and "Heir of Light" 
(https://play.google.com/store/apps/details?id=com.gamevil.heiroflight.android.google.global.normal&hl=en&gl=US). This game 
involves battles between teams of legendary creatures. Each legendary creature takes turns to make moves during battles.

# Executable File

The executable file is downloadable at 
https://github.com/NativeApkDev/ANCIENT_INVASION/blob/master/ANCIENT_INVASION/dist/ancient_invasion/ancient_invasion.

# Source Code

Python code used to create the game is available in 
https://github.com/NativeApkDev/ANCIENT_INVASION/blob/master/ANCIENT_INVASION/ancient_invasion.py.

# Installation

Enter the command "pip install ANCIENT_INVASION".

# Unit Tests

Python unit tests created using Python's "unittest" module, testing basic functionalities of the game is available in 
https://github.com/NativeApkDev/ANCIENT_INVASION/blob/master/ANCIENT_INVASION/ancient_invasion_tests.py. The tests 
are all automated and related to user inputs in the game.

# How to Use the Executable File?

First, open by double-clicking the file "ancient_invasion". How the executable file looks like is shown in the image
below (the file is enclosed with a red rectangle).

### Image 1
![Executable File](images/Executable%20File.png)

# Getting Started

After you run the game, you will be asked to enter your name. If a saved game data with your name exists, that saved game 
data will be loaded. Else, you will be told to create a new saved game data using your name.

### Image 2
![Getting Started](images/Getting%20Started.png)

# Main Menu

Once you loaded a saved game data or created a new game data, you will be asked whether you want to continue playing 
the game "Ancient Invasion" or not. If you enter "Y", you will be able to do various activities (e.g., battle 
in map areas and dungeons, build on your player base, buy and sell items, etc) in the game. The activity you want to 
do can be chosen by entering an input as instructed in the command line interface (see "Image #4").

### Image 3
![Main Menu 1](images/Main%20Menu%201.png)

### Image 4
![Main Menu 2](images/Main%20Menu%202.png)

# The Game

In the game, you will be able to do any of the actions as shown in "Image 4". The actions are described as below.

* PLAY ADVENTURE MODE -> battle in levels inside either map areas or dungeons against enemy legendary creatures. Each 
level has multiple stages where each stage has a number of enemies you will need to defeat in order to proceed and
eventually clear the levels and gain rewards.
* MANAGE PLAYER BASE -> build, level up, and remove buildings on your player base. Trees can be built for decorations;
obstacles can be removed; and buildings to strengthen legendary creatures (e.g., magic altar), produce resources
(e.g., gold mine and gem mine), increase legendary creatures' EXP (i.e., training area), and so forth can be built.
* MANAGE BATTLE TEAM -> add and remove legendary creatures from your team. By default, the first legendary creature
appearing in the order the legendary creatures were added is the team leader.
* MANAGE LEGENDARY CREATURE INVENTORY -> this allows you to remove legendary creatures which you do not use.
* MANAGE ITEM INVENTORY -> sell items and/or level up runes in the item inventory.
* MAKE A WISH -> gain random rewards (i.e., items or resources such as gold and gems) from making a wish using the 
temple of wishes.
* FUSE LEGENDARY CREATURES -> fuse multiple legendary creatures to gain a stronger one.
* SUMMON LEGENDARY CREATURE -> use a scroll to summon a legendary creature which will be added to your legendary
creature inventory.
* GIVE ITEM -> give an item to a legendary creature to strengthen that legendary creature.
* POWER UP LEGENDARY CREATURE -> strengthen a legendary creature by sacrificing some other legendary creatures as 
power-up materials. This requires a power-up circle.
* EVOLVE LEGENDARY CREATURE -> increase the rating of a legendary creature to make it able to reach higher levels. This 
also requires a power-up circle.
* MANAGE TRAINING AREA -> add and remove legendary creatures from a training area in your player base.
* PLACE RUNE -> place a rune in a legendary creature you have.
* REMOVE RUNE -> remove a rune from a legendary creature you have.
* BUY ITEM -> buy an item from the item shop.
* VIEW STATS -> view your stats in the game (e.g., your level, EXP, amount of EXP you need to have to get to the 
next level, and so forth).

Once you entered one of the actions above at the main menu and then press the button "ENTER" or "RETURN" on your machine, 
further instructions of what you need to do will be shown on the command line interface.
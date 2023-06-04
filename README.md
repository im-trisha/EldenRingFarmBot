# EldenRingFarmBot

## What is it?
This is a python script that will allow you to automatically farm runes on Elden Ring while AFK

## What will your Elden Ring character need?
* The ["Sacred Relic Sword"](https://eldenring.wiki.fextralife.com/Sacred+Relic+Sword)
* Having "Palace Approach Ledge-Road" site of grace, and teleporting there before starting the bot
* Said sword, must one shot the albinaurics, otherwise the killing cycle will not be able to start over again

## How to use
I know that this program will probably and mostly be used by non programmers, so here is a greatly detailled explaination on how to use it:
1. Download [Python 3.11](https://www.python.org/downloads/release/python-3113/), probably any version which supports the required packages is fine[^1], here, you will need to download [Windows installer (64-bit)](https://www.python.org/ftp/python/3.11.3/python-3.11.3-amd64.exe), or the 32-bit version[^2] according to your sistem architecture. Assure to put python on the PATH while installing it, you can do it just by checking the said option
2. Download [this script](https://github.com/GiuseppeFn/EldenRingFarmBot/archive/refs/heads/main.zip)
3. Unzip it (Right click on the file, then click 'Extract')
4. Open the folder where there is the main file
5. You must open the settings.yaml file and edit the grace_timeout value, use your phone as a stopwatch to know what time to put here, and add 2 to 3 seconds customize the other settings, if you dont want to, just put everything back to default controls on Elden Ring and set the ability key to '3'
6. Right click on the folder and open it in the cmd/terminal
8. ONE TIME SETUP (You should run it only the first time you run the script): ```pip3 install -r requirements.txt```
8. Now, you can finally write in the terminal: ```python3 -B main.py```, now the script is started.
9. You can now teleport to the site of grace and set the right weapons, and when you're ready, press the ```start_key``` that you put in the settings (By default the p key)
- Bonus: I suggest you to put the graphics to the minimum, so there will be no stuttering and so no sync error
- Bonus-2: You can stop the script by pressing the ```quit_key``` for a whole cycle (A cycle being a full: Kill the albinaurics-Loading site of grace)

You're ready to go! Just leave it overnight or while you work.

[^1]: Thus being said, the script has only been tested with Python 3.9 and Python 3.11
[^2]: Thus being said, the script has only been tested with 64-bit windows

## Notes
There are some notes thought:
* I made the code in about 30 minutes and after leaving it overnight it works perfectly, but i suppose it isn't flawless
* You can put ```joystick: true``` and the program will emulate a controller instead of your keyboard. Not sure why you would even want to do that but you can, i didn't test it thought
* I will work on making the script a simple executable, so every user will be able to run it without any issue, as soon as i have time. I'm busy most of the time and i decided to make this code public just because maybe it will help someone else.
* ^ Thus being said, please feel free to open an issue in the ```Issues tab``` demanding for new features or just alerting me of an unknown issue.
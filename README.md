# EldenRingFarmBot

## What is it?
This is a python script that will allow you to automatically farm runes on Elden Ring while AFK

## What will your Elden Ring character need?
* The ["Sacred Relic Sword"](https://eldenring.wiki.fextralife.com/Sacred+Relic+Sword)
* Having "Palace Approach Ledge-Road" site of grace, and teleporting there before starting the bot
* Said sword, must one shot the albinaurics, otherwise the killing cycle will not be able to start over again

## How to use - Simple user
1. Download the executable zip from [here](https://github.com/GiuseppeFn/EldenRingFarmBot/releases/latest/download/EldenRingFarmBot.zip)
2. Unzip it by right-clicking it->Extract
2. You must open the settings.yaml file and edit the grace_timeout value, use your phone as a stopwatch to know what time to put here, and add 2 to 3 seconds. Then, customize the other settings, if you dont want to, just put everything back to default controls on Elden Ring and set the ability key to '3'
3. Now you can just run the program by double clicking the executable
4. You must then teleport to the site of grace and set the right weapons and talismans, and when you're ready, press the ```start_key``` that you put in the settings (By default the p key)
- Bonus: I **HIGLY** suggest you to put the graphics to the minimum, so there will be no stuttering and so no sync error

You're finally ready to go! Just leave it overnight or while you work.

## How to use - Programmer
If you want to help me in some way, or just curious about the code, you must run the following:
```
git clone https://github.com/GiuseppeFn/EldenRingFarmBot.git
cd EldenRingFarmBot
python -m venv ./
```
Then, depending on your os:
* Windows: ```.\Scripts\Activate.ps1```
* Unix: ```source ./Scripts/activate```
Finally, you just need to run ```pip install -r requirements.txt```
To build it as an executable, you then just need to run ```pyinstaller --onefile main.py -n EldenRingFarmBot```
And then, if you want to make it as a release: 
```tar -a -c -f ./dist/EldenRingFarmBot.zip ./dist/EldenRingFarmBot.exe ./settings.yaml```


## Notes
There are some notes thought:
* I made the code in about 1 hour and after leaving it overnight it works perfectly, but i suppose it isn't flawless
* You can put ```joystick: true``` and the program will emulate a controller instead of your keyboard, if you're using python to run the script. Not sure why you would even want to do that but you can
* Please feel free to open an issue in the ```Issues tab``` demanding for new features or just alerting me of an unknown issue.

# YOU MUST NOT PAY THIS SOFTWARE. THIS SOFTWARE IS FREE OF CHARGE. IF YOU DID, YOU HAVE BEEN SCAMMED.

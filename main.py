from src.emulator import Keyboard, Joystick, Emulator, WALK_TIMEOUTS
from src.settings import settings

emulator: Emulator = Joystick() if settings.joystick else Keyboard()

Keyboard.wait(settings.start_key)
while not Keyboard.is_pressed(settings.quit_key):
    emulator.back_to_grace(settings.grace_timeout) # We start by going to the site of grace

    emulator.walk(0, 1, WALK_TIMEOUTS[0])  # Forward
    emulator.walk(-1, 0, WALK_TIMEOUTS[1]) # Left
    emulator.walk(0, 1, WALK_TIMEOUTS[2])  # Forward
    emulator.ability(settings.skill_key)   # We got to the first albinaurics batch, we can kill them
    
    emulator.walk(0, 1, WALK_TIMEOUTS[3])  # Forward
    emulator.ability(settings.skill_key)   # We got to the second albinaurics batch, we can kill them
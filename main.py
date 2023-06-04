import logging, sys
from src.emulator import Keyboard, Joystick, Emulator, WALK_TIMEOUTS
from src.settings import get_settings

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    level=logging.INFO,
    handlers=[
        logging.FileHandler('debug.logs'),
        logging.StreamHandler(sys.stdout)
    ]
)

def main() -> None:
    settings = get_settings('settings.yaml')
    emulator: Emulator = Joystick() if settings.joystick else Keyboard()

    logging.info(f'Started {emulator.__class__.__name__} emulator.')

    logging.info(f"Press '{settings.start_key}' to start.")
    Keyboard.wait(settings.start_key)

    logging.info("Starting, to quit press 'CTRL+C' while having the terminal open.")
    
    runs_n = 0
    try:
        while True:
            emulator.back_to_grace(settings.grace_timeout) # We start by going to the site of grace

            emulator.walk(0, 1, WALK_TIMEOUTS[0])  # Forward
            emulator.walk(-1, 0, WALK_TIMEOUTS[1]) # Left
            emulator.walk(0, 1, WALK_TIMEOUTS[2])  # Forward
            emulator.ability(settings.skill_key)   # We got to the first albinaurics batch, we can kill them

            emulator.walk(0, 1, WALK_TIMEOUTS[3])  # Forward
            emulator.ability(settings.skill_key)   # We got to the second albinaurics batch, we can kill them

            runs_n += 1
    except KeyboardInterrupt:
        pass
    
    after_phrase = "I'm sorry Albus..." if runs_n != 0 else "That's great Albus!"
    logging.info(f'Program finished successfully and killed the albinaurics {runs_n} times! {after_phrase}')
    logging.info('Waiting for space to be pressed...')
    Keyboard.wait('space')

if __name__ == '__main__':
    main()
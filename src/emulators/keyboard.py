import time, keyboard as kb, pydirectinput as pdi
from src.emulator import Emulator

POSSIBLE_WALK = [-1, 0, 1]
X_WALKS = {-1: 'a', 0: None, 1: 'd'}
Y_WALKS = {-1: 's', 0: None, 1: 'w'}

class Keyboard(Emulator):
    def press(self, keys: list[str], interval: float, after: float = 0) -> None:
        for key in keys: pdi.keyDown(key)

        time.sleep(interval)
        
        for key in keys: pdi.keyUp(key)

        time.sleep(after)

    def walk(self, x: int, y: int, interval: float):
        assert(x in POSSIBLE_WALK and y in POSSIBLE_WALK)
        self.press([X_WALKS[x], Y_WALKS[y]], interval)

    def ability(self, key: str) -> None:
        # Stringify key because if it is a number like 3 and not '3', it wouldn't work
        self.press(str(key), 0.2, 4)
        
    def back_to_grace(self, timeout: float):
        self.press('g', 0, 0.5)
        self.press('f', 0, 0)
        self.press('e', 0, 0)
        self.press('e', 0, 0)
        time.sleep(timeout)

    
    @staticmethod
    def wait(key: str) -> None:
        kb.wait(key)
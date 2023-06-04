import time, logging, traceback
from src.emulator import Emulator

class Joystick(Emulator):
    BUTTON_BACK = 0x0020
    BUTTON_A = 0x1000
    BUTTON_Y = 0x8000

    def __init__(self):
        try:
            import vgamepad as vg
            self.gamepad = vg.VX360Gamepad()
            self.__press_button(self.BUTTON_A)
        except Exception as e:
            print(e)
            traceback.print_exc()
            logging.critical("At the moment, using joystick mode while using the built executable isn't supported. Please use joystick: false in the settings.")
            exit(-1)

    # TODO: This is ugly. Consider to removing Joystick emulation mode if no one uses it.
    def do(self, action, interval: float, timeout: float, before: dict, after: dict) -> None:
        action(**before)
        self.gamepad.update()
        time.sleep(interval)
        
        if action == self.gamepad.press_button:
            self.gamepad.release_button(**after)
        else:
            action(**after)
        self.gamepad.update()

        time.sleep(timeout)


    def ability(self, _: str):
        self.do(
            self.gamepad.left_trigger,
            interval = 1, timeout = 4, 
            before = {'value':255}, 
            after = {'value':0}
        )

    def walk(self, x: float, y: float, delay: int = 0) -> None:
        self.do(
            self.gamepad.left_joystick_float, 
            interval = delay + 0.3, timeout = 0, # Joystick seems to have a little bit of a pressing delay, so we add .3
            before = {'x_value_float': x, 'y_value_float': y},
            after  = {'x_value_float': 0, 'y_value_float': 0}
        )

    def __press_button(self, button: int, interval: float = 0.1, timeout: float = 0):
        self.do(
            self.gamepad.press_button, 
            interval = interval, timeout = timeout,
            before = {'button': button},
            after = {'button': button},
        )

    def back_to_grace(self, timeout: float):
        self.__press_button(self.BUTTON_BACK, 1)
        self.__press_button(self.BUTTON_Y)
        self.__press_button(self.BUTTON_A, timeout = 0.1)
        self.__press_button(self.BUTTON_A, timeout = 0.1)
        time.sleep(timeout)
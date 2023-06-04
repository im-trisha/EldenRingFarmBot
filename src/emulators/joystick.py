from src.emulator import Emulator
import vgamepad as vg, time

# TODO this code is awfully ugly, i can probably make it prettier
class Joystick(Emulator):
    def __init__(self):
        self.gamepad = vg.VX360Gamepad()
        self.__press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)

    def ability(self, _: str):
        self.gamepad.left_trigger(value=255)
        self.gamepad.update()
        time.sleep(1)
        self.gamepad.left_trigger(value=0)
        self.gamepad.update()
        time.sleep(4)

    def walk(self, x: float, y: float, delay: int = 0) -> None:
        self.gamepad.left_joystick_float(x_value_float=x, y_value_float=y)
        self.gamepad.update()
        time.sleep(delay)
        self.gamepad.left_joystick_float(x_value_float=0, y_value_float=0)
        self.gamepad.update()

    def __press_button(self, button: vg.XUSB_BUTTON, interval: float = 0.1, after: float = 0):
        self.gamepad.press_button(button=button)
        self.gamepad.update()

        time.sleep(interval)
        
        self.gamepad.release_button(button=button)
        self.gamepad.update()

        time.sleep(after)


    def back_to_grace(self, timeout: float):
        self.__press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK, 1)
        self.__press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
        self.__press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A, after = 0.1)
        self.__press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A, after = 0.1)
        time.sleep(timeout)
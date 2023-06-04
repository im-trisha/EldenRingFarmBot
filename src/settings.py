import yaml
from numbers import Number

class Settings:
    def __init__(self, grace_timeout: float, start_key: str, skill_key: str, quit_key: str, joystick: bool) -> None:
        self.grace_timeout = grace_timeout
        self.start_key     = start_key
        self.skill_key     = skill_key
        self.quit_key      = quit_key
        self.joystick      = joystick

    # This function is stupidly ugly to user-proof the input
    @staticmethod
    def from_json(json: dict) -> 'Settings':
        grace_timeout = json.get('grace_timeout', DEFAULT.grace_timeout)
        start_key = json.get('start_key', DEFAULT.start_key)
        skill_key = json.get('skill_key', DEFAULT.skill_key)
        quit_key = json.get('quit_key', DEFAULT.quit_key)
        joystick = json.get('joystick', DEFAULT.joystick)
        return Settings(
            grace_timeout if isinstance(grace_timeout, Number) else DEFAULT.grace_timeout, 
            start_key[0] if isinstance(start_key, str) and len(start_key) >= 1 else DEFAULT.start_key,
            skill_key[0] if isinstance(skill_key, str) and len(skill_key) >= 1 else DEFAULT.skill_key,
            quit_key[0] if isinstance(quit_key, str) and len(quit_key) >= 1 else DEFAULT.quit_key,
            joystick if isinstance(joystick, bool) else DEFAULT.joystick,
        )
    
    def __repr__(self) -> str:
        return f'Settings(start_key: {self.start_key}, skill_key: {self.skill_key} quit_key: {self.quit_key}, joystick: {self.joystick}, grace_timeout: {self.grace_timeout})'

DEFAULT = Settings(10, 'p', 'u', 'k', False)

with open("settings.yaml", "r") as f:
    try:
        settings = Settings.from_json(yaml.safe_load(f))
    except Exception:
        settings = DEFAULT
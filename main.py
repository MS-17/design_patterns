from src.settings_manager import SettingsManager
from src.a.a import A


print("Program main entry")
sm = SettingsManager()
sm.load_settings("settings.json")
print(sm)

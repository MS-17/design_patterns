from src.settings_manager import SettingsManager


print("Program main entry")
sm = SettingsManager()
sm.load_settings("configuration/settings.json")
print(sm)

from src.settings_manager import SettingsManager
from src.models.nomenclature_model import Nomenclature


print("Program main entry")
sm = SettingsManager()
sm.load_settings("configuration/settings.json")
print(sm)

nm = Nomenclature()
nm.name = "Some name"
print(nm.name, type(nm), nm.unique_id)
print(nm == sm)

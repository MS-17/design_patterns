from src.settings_manager import SettingsManager
from src.models.nomenclature.nomenclature_model import Nomenclature
from src.models.base.base_models import BaseModelName, BaseModelUniqueID
from src.models.nomenclature.nomenclature_group_model import NomenclatureGroup
from src.validation.data_validator import DataValidator


# print("Program main entry")
# sm = SettingsManager()
# sm.load_settings("configuration/settings.json")
# print(sm)

# nm = Nomenclature()
# nm.name = "Some name"
# print(nm.name, type(nm), nm.unique_id)
# print(nm == sm)

bn = BaseModelName()
buid = BaseModelUniqueID()
nm = NomenclatureGroup()
print(bn.set_compare_mode(buid))
print(bn == buid)
print(buid.set_compare_mode(bn), buid == bn)
print(buid.unique_id, bn.unique_id)
print(nm.unique_id)

# DataValidator().validate_length("", -1)
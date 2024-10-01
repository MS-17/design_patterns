from src.models.base.base_models import BaseModelUniqueID
from src.models.nomenclature.nomenclature_group_model import NomenclatureGroup
from src.models.measures.measurement_unit_model import MeasurementUnit


class Nomenclature(BaseModelUniqueID):
	"""
	A class that defines a nomenclature model\n
	name: str\n
	nomenclature_group: NomenclatureGroup - a nomenclature group\n 
	measurement_unit: MeasurementUnit - a measurement unit\n
	"""

	def __init__(self, name: str, nomenclature_group: NomenclatureGroup, measurement_unit: MeasurementUnit):
		super().__init__(name)
		self.__nomenclature_group = nomenclature_group
		self.__measurement_unit = measurement_unit

	def set_compare_mode(self, other_object):
		return super().set_compare_mode(other_object)

	def __eq__(self, obj: object) -> bool:
		return self.set_compare_mode(obj)

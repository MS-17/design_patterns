from src.models.base.base_models import BaseModelName
from src.validation.data_validator import DataValidator


class NomenclatureGroup(BaseModelName):
	"""
	A class that defines a nomenclature group model
	"""

	@staticmethod
	def create(name: str = "") -> 'NomenclatureGroup':
		""" Create a nomenclature group instance with the given name (factory staticmethod) """
		DataValidator.validate_field_type(name, str)
		item = NomenclatureGroup()
		item.name = name
		return item

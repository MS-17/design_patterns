from src.models.base.base_models import BaseModelUniqueID
from src.models.nomenclature.nomenclature_group_model import NomenclatureGroup
from src.models.measures.measurement_unit_model import MeasurementUnit
from src.validation.data_validator import DataValidator


class Nomenclature(BaseModelUniqueID):
	"""
	A class that defines a nomenclature model\n
	name: str\n
	full_name: str | None\n
	nomenclature_group: NomenclatureGroup | None - a nomenclature group\n 
	measurement_unit: MeasurementUnit | None - a measurement unit\n
	"""

	def __init__(self, full_name: str | None = None, nomenclature_group: NomenclatureGroup | None = None,
				measurement_unit: MeasurementUnit | None = None) -> None:
		# super().__init__(name)
		DataValidator().validate_field_type(full_name, str, True)
		DataValidator().validate_length(full_name, 255)
		DataValidator().validate_field_type(nomenclature_group, NomenclatureGroup, True)
		DataValidator().validate_field_type(measurement_unit, MeasurementUnit, True)
		self.__full_name = full_name
		self.__nomenclature_group = nomenclature_group
		self.__measurement_unit = measurement_unit

	@property
	def full_name(self) -> str:
		""" Get the nomenclature full name """
		return self.__full_name

	@full_name.setter
	def full_name(self, value: str) -> None:
		""" Set and validate the nomenclature full name """
		DataValidator().validate_field_type(value, str)
		DataValidator().validate_length(value, 255)
		self.__full_name = value

	@property
	def nomenclature_group(self) -> NomenclatureGroup:
		""" Get the nomenclature group """
		return self.__nomenclature_group

	@nomenclature_group.setter
	def nomenclature_group(self, value: NomenclatureGroup) -> None:
		""" Set and validate the nomenclature group """
		DataValidator().validate_field_type(value, NomenclatureGroup)
		self.__nomenclature_group = value

	@property
	def measurement_unit(self) -> MeasurementUnit:
		""" Get the nomenclature measurment unit """
		return self.__measurement_unit

	@measurement_unit.setter
	def measurement_unit(self, value: MeasurementUnit) -> None:
		""" Set and validate the nomenclature measurement unit """
		DataValidator().validate_field_type(value, MeasurementUnit)
		self.__measurement_unit = value


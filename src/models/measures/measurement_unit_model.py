from src.models.base.base_models import BaseModelName
from src.validation.data_validator import DataValidator


class MeasurementUnit(BaseModelName):
	"""
	A class that defines measurement units\n
	name - a unit name (имя ед. изм.)\n
	value - коэф пересчета\n
	base_unit - базовая единица измерения \n
	Ex:\n
		base_unit = MeasurementUnit("gram", 1)\n
		unit = MeasurementUnit("kilogram", 1000, base_unit)\n
	"""

	def __init__(self, name: str, value: float, base_unit: 'MeasurementUnit' = None) -> None:
		DataValidator.validate_field_type(name, str)
		DataValidator.validate_field_type(value, float)
		DataValidator.validate_field_type(base_unit, MeasurementUnit, True)
		super().__init__(name)
		self.__value = value
		self.__base_unit = base_unit
	
	@property
	def value(self) -> float:
		""" Get the measurment unit value """
		return self.__value

	@value.setter
	def value(self, value: float) -> None:
		""" Set and validate the measurment unit value """
		DataValidator.validate_field_type(value, float)
		self.__value = value

	@property
	def base_unit(self) -> 'MeasurementUnit':
		""" Get a measurment unit base unit """
		return self.__base_unit
	
	@base_unit.setter
	def base_unit(self, value: 'MeasurementUnit') -> None:
		""" Set and validate the measurment unit base unit """
		DataValidator.validate_field_type(value, MeasurementUnit)
		self.__base_unit = value

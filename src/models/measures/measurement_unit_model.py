from src.models.base.base_models import BaseModelName


class MeasurementUnit(BaseModelName):
	# __base_unit: float = 0
	# __base_measure_unit: MeasurementUnit = None

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
		super().__init__(name)
		self.__value = value
		self.__base_unit = base_unit
	
	@property
	def value(self) -> float:
		return self.__value

	@value.setter
	def value(self, value: float) -> None:
		self.__value = value

	@property
	def base_unit(self) -> 'MeasurementUnit':
		return self.__base_unit
	
	@base_unit.setter
	def base_unit(self, value: 'MeasurementUnit') -> None:
		self.__base_unit = value

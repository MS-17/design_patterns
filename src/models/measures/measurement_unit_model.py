from src.models.base.base_models import BaseModelName


class MeasurementUnit(BaseModelName):
	# __base_unit: float = 0
	# __base_measure_unit: MeasurementUnit = None

	"""
	A class that defines measurement units
	"""

	def __init__(self, name: str, value: float, base_unit: 'MeasurementUnit' = None):
		"""
		name - a unit name (имя ед. изм.)
		value - коэф пересчета
		base_unit - базовая единица измерения 
		Ex:
			base_unit = MeasurementUnit("gram", 1)
			unit = MeasurementUnit("kilogram", 1000, base_unit)
		"""
		super().__init__(name)
		self.__value = base_unit
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

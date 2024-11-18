from src.abstract_logic import AbstractLogic


class DataRepository(AbstractLogic):
	"""
	Creates a data repository singleton
	"""
	__data: dict = {}

	def __new__(cls):
		if not hasattr(cls, 'instance'):
			cls.instance = super(DataRepository, cls).__new__(cls)
		return cls.instance

	@property
	def data(self) -> dict:
		""" Get a data dictionary """
		return self.__data

	@staticmethod
	def nomenclature_group_key() -> str:
		""" Get a nomenclature group key. Staticmethod. Key: nomenclature_group """
		return "nomenclature_group"

	@staticmethod
	def nomenclature_key() -> str:
		""" Get a nomenclature key. Staticmethod. Key: nomenclatures """		
		return "nomenclatures"

	@staticmethod
	def measurement_unit_key() -> str:
		""" Get a measurement unit key. Staticmethod. Key: measurement_units """		
		return "measurement_units"

	def set_exception(self, ex: Exception) -> None:
		""" Set an exception """
		self._inner_set_exception(ex)
	
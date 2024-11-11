from src.abstract_logic import AbstractLogic
from src.repository.data_repository import DataRepository
from src.models.nomenclature.nomenclature_group_model import NomenclatureGroup
from src.models.nomenclature.nomenclature_model import Nomenclature
# from src.settings_manager import SettingsManager
from src.validation.data_validator import DataValidator


class StartService(AbstractLogic):
	"""
	A serive that is used on the application startup\n
	repository: DataRepository - a data repository instance\n
	settings_manager: SettingsManager - a settings manager instance
	"""

	def __init__(self, repository: DataRepository) -> None: #, settings_manager: SettingsManager):
		super().__init__()
		DataValidator.validate_field_type(repository, DataRepository)
		# DataValidator().validate_field_type(settings_manager, SettingsManager)
		# self.__settings_manager = settings_manager
		self.__repository = repository

	def __create_nomenclature_groups(self) -> None:
		""" Generate a default set of the nomenclature groups """
		items = [NomenclatureGroup.create("Raw materials"), NomenclatureGroup.create("Goods")]	# raw materials - сырье, goods - продукция 
		self.__repository.data[DataRepository.nomenclature_group_key()] = items
		print(self.__repository.data)
	
	def __create_nomenclature(self):
		""" Generate a default nomenclature configuration """
		Nomenclature()
		# self.__repository.data[]

	def __create_measurement_units(self):
		""" Generate a default set of the measurement units """
		...

	def create(self) -> None:
		"""
		Create a default configuration of the application nomenclature, nomenclature groups and measurement units\n
		"""
		self.__create_nomenclature_groups()
		self.__create_nomenclature()
		self.__create_measurement_units()
		# self.__create_recipe()

	def set_exception(self, ex: Exception) -> None:
		self._inner_set_exception(ex)

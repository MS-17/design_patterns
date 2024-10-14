from src.models.base.base_models import BaseModelName
from src.models.settings.settings_model import Settings
from src.validation.data_validator import DataValidator


class Organization(BaseModelName):
	"""
	Initialize an organization model\n
	settings: Settings - a settings object
	"""
	
	def __init__(self, settings: Settings | None = None) -> None:
		if settings is None:
			super().__init__("")
			return
		super().__init__(settings.organization_name)
		# it'd be better to implement the settings fields type and length checks here
		self.__inn = settings.inn
		self.__bik = settings.bik
		self.__bank_account = settings.bank_account
		self.__ownership_form = settings.ownership_form

	@property
	def inn(self) -> str:
		""" Get INN """
		return self.__inn
	
	@inn.setter
	def inn(self, value: str) -> None:
		""" Set and validate INN """
		DataValidator().validate_field_type(value, str)
		DataValidator().validate_length(value, 12)
		self.__inn = value

	@property
	def bik(self) -> str:
		""" Get BIK """
		return self.__bik
	
	@bik.setter
	def bik(self, value: str) -> None:
		""" Set and validate BIK """
		DataValidator().validate_field_type(value, str)
		DataValidator().validate_length(value, 9)
		self.__bik = value
	
	@property
	def bank_account(self) -> str:
		""" Get bank account """
		return self.__bank_account
	
	@bank_account.setter
	def bank_account(self, value: str) -> None:
		""" Set and validate bank account """
		DataValidator().validate_field_type(value, str)
		DataValidator().validate_length(value, 11)
		self.__bank_account = value
	
	@property
	def ownership_form(self) -> str:
		""" Get ownership form """
		return self.__ownership_form
	
	@ownership_form.setter
	def ownership_form(self, value: str) -> None:
		""" Set and validate ownership form """
		DataValidator().validate_field_type(value, str)
		DataValidator().validate_length(value, 5)
		self.__ownership_form = value

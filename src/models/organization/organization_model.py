from src.models.base.base_models import BaseModelName
from src.models.settings.settings_model import Settings


class Organization(BaseModelName):
	"""
	Initialize an organization model\n
	settings: Settings - a settings object
	"""
	
	def __init__(self, settings: Settings) -> None:
		super().__init__(settings.organization_name)
		self.__inn = settings.inn
		self.__bik = settings.bik
		self.__bank_account = settings.bank_account
		self.__ownership_form = settings.ownership_form

	@property
	def inn(self) -> str:
		return self.__inn
	
	@inn.setter
	def inn(self, value: str) -> None:
		self.__inn = value

	@property
	def bik(self) -> str:
		return self.__bik
	
	@bik.setter
	def bik(self, value: str) -> None:
		self.__bik = value
	
	@property
	def bank_account(self) -> str:
		return self.__bank_account
	
	@bank_account.setter
	def bank_account(self, value: str) -> None:
		self.__bank_account = value
	
	@property
	def ownership_form(self) -> str:
		return self.__ownership_form
	
	@ownership_form.setter
	def ownership_form(self, value: str) -> None:
		self.__ownership_form = value

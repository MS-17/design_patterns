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

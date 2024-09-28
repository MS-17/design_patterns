import os, json

from models.settings import Settings


class SettingsManager:
	__file_name: str = ""
	__settings: Settings = None

	def __new__(cls):
		if not hasattr(cls, 'instance'):
			cls.instance = super(SettingsManager, cls).__new__(cls)
		return cls.instance

	def __init__(self) -> None:
		if self.__settings is None:
			self.__settings = self.__default_settings()

	def __default_settings(self) -> Settings:
		_settings = Settings()
		_settings.organization_name = "Org"
		_settings.inn = "11111"
		_settings.bank_account = "22222"
		_settings.correspondent_account = "33333"
		_settings.bik = "44444"
		_settings.ownership_form = "55555"
		return _settings

	"""
	Get file name that contains settings
	"""
	@property
	def file_name(self) -> Settings:
		# do we need a setter for that?
		return self.__file_name

	"""
	Get settings
	"""
	@property
	def settings(self) -> str:
		return self.__settings

	"""
	Load settings from a json file and fill 'Settings' fields with its values
	"""
	def load_settings(self, file_name: str = None) -> None:
		print(os.curdir, __file__)
		


	def __str__(self) -> str:
		return f"File name: {self.file_name}, Settings: ({self.settings})"

sm = SettingsManager()
print(sm.load_settings())



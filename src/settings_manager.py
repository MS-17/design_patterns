import os, json

from src.models.settings.settings_model import Settings


class SettingsManager:
	"""
	A class that loads settings and manages them
	"""
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
		""" Set default settings """
		_settings = Settings()
		_settings.organization_name = "Org"
		_settings.inn = "11111"
		_settings.bank_account = "22222"
		_settings.correspondent_account = "33333"
		_settings.bik = "44444"
		_settings.ownership_form = "55555"
		return _settings

	@property
	def file_name(self) -> str:
		"""	Get a file name that contains settings """
		return self.__file_name

	@file_name.setter
	def file_name(self, value: str) -> None:
		""" Set a file name """
		self.__file_name = value

	@property
	def settings(self) -> Settings:
		""" Get settings """
		return self.__settings

	def load_settings(self, file_name: str = "") -> None:
		"""
		Load settings from a json file and fill 'Settings' fields with its values
		"""
		self.file_name = file_name
		current_path = os.getcwd()
		# current_path = os.path.split(__file__)[0]
		full_name = f"{current_path}{os.sep}{self.file_name}"
		with open(full_name, 'r') as file:
			data = json.load(file)
		fields = dir(self.settings)
		for field in fields:
			if field in data.keys():
				self.settings.__setattr__(field, data[field])

	def __str__(self) -> str:
		return f"File name: {self.file_name}, Settings: ({self.settings})"

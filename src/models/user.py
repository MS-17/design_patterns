from src.exceptions.argument_exception import ArgumentException
from src.validation.data_validator import DataValidator


class User:
	__code: str = ""
	__login: str = ""
	__password: str = ""
	__name: str = ""
	__email: str = ""

	@property
	def code(self):
		return self.__code
	
	@code.setter
	def code(self, value: str):
		self.__code = value

	@property
	def login(self):
		return self.__login
	
	@login.setter
	def login(self, value: str):
		self.__login = value

	@property
	def password(self):
		return self.__password
	
	@password.setter
	def password(self, value: str):
		self.__password = value

	@property
	def name(self):
		return self.__name
	
	@name.setter
	def name(self, value: str):
		self.__name = value

	@property
	def email(self):
		return self.__email
	
	@email.setter
	def email(self, value: str):
		self.__email = value

	@staticmethod
	def create(code: str = "", login: str = "", password: str = "", name: str = "", email: str = ""):
		DataValidator.validate_field_type(code, str)
		DataValidator.validate_field_type(login, str)
		DataValidator.validate_field_type(password, str)
		DataValidator.validate_field_type(name, str)
		DataValidator.validate_field_type(email, str)
		instance = User()
		instance.code = code
		instance.login = login
		instance.password = password
		instance.name = name
		instance.email = email
		return instance

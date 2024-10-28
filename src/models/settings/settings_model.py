from src.validation.data_validator import DataValidator


class Settings:
	"""
	A class that contains app settings\n
	organization_name: str = ""\n
	inn: str = ""\n
	bank_account: str = ""\n
	correspondent_account: str = ""\n
	bik: str = ""\n
	ownership_form: str = ""\n
	"""
	__organization_name: str = ""
	__inn: str = ""
	__bank_account: str = ""
	__correspondent_account: str = ""
	__bik: str = ""
	__ownership_form: str = ""
		
	def __init__(self) -> None:
		pass

	@property
	def organization_name(self) -> str:
		""" Get organization name """
		return self.__organization_name
	
	@organization_name.setter
	def organization_name(self, value: str) -> None:
		""" Set and validate organization name """
		DataValidator.validate_field_type(value, str)
		self.__organization_name = value

	@property
	def inn(self) -> str:
		""" Get INN """
		return self.__inn
	
	@inn.setter
	def inn(self, value: str) -> None:
		""" Set and validate INN """
		DataValidator.validate_field_type(value, str)
		DataValidator.validate_length(value, 12)
		self.__inn = value

	@property
	def bank_account(self) -> str:
		""" Get bank account """
		return self.__bank_account
	
	@bank_account.setter
	def bank_account(self, value: str) -> None:
		""" Set and validate bank account """
		DataValidator.validate_field_type(value, str)
		DataValidator.validate_length(value, 11)
		self.__bank_account = value

	@property
	def correspondent_account(self) -> str:
		""" Get correspondent account """
		return self.__correspondent_account
		
	@correspondent_account.setter
	def correspondent_account(self, value: str) -> None:
		""" Set and validate correspondent account """
		DataValidator.validate_field_type(value, str)
		DataValidator.validate_length(value, 11)
		self.__correspondent_account = value

	@property
	def bik(self) -> str:
		""" Get BIK """
		return self.__bik
	
	@bik.setter
	def bik(self, value: str) -> None:
		""" Set and validate BIK """
		DataValidator.validate_field_type(value, str)
		DataValidator.validate_length(value, 9)
		self.__bik = value

	@property
	def ownership_form(self) -> str:
		""" Get ownership form """
		return self.__ownership_form
	
	@ownership_form.setter
	def ownership_form(self, value: str) -> None:
		""" Set and validate ownership form """
		DataValidator.validate_field_type(value, str)
		DataValidator.validate_length(value, 5)
		self.__ownership_form = value

	def __str__(self) -> str:
		return f"Name: {self.organization_name}, INN: {self.inn}, Bank Acc: {self.bank_account}, " \
			   f"Corr Acc: {self.correspondent_account}, BIK: {self.bik}, Ownership: {self.ownership_form}"

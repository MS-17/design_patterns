class Settings():
	__organization_name: str = ""
	__inn: str = ""
	__bank_account: str = ""
	__correspondent_account: str = ""
	__bik: str = ""
	__ownership_form: str = ""
		
	def __init__(self) -> None:
		pass

	"""
	Organization name
	"""
	@property
	def organization_name(self) -> str:
		return self.__organization_name
	
	@organization_name.setter
	def organization_name(self, value: str) -> None:
		self.__organization_name = value

	"""
	INN
	"""
	@property
	def inn(self) -> str:
		return self.__inn
	
	@inn.setter
	def inn(self, value: str) -> None:
		self.__inn = value

	"""
	Bank account
	"""
	@property
	def bank_account(self) -> str:
		return self.__bank_account
	
	@bank_account.setter
	def bank_account(self, value: str) -> None:
		self.__bank_account = value

	"""
	Correspondent bank account
	"""
	@property
	def correspondent_account(self) -> str:
		return self.__correspondent_account
		
	@correspondent_account.setter
	def correspondent_account(self, value: str) -> None:
		self.__correspondent_account = value

	"""
	BIK
	"""
	@property
	def bik(self) -> str:
		return self.__bik
	
	@bik.setter
	def bik(self, value: str) -> None:
		self.__bik = value

	"""
	The form of ownership
	"""
	@property
	def ownership_form(self) -> str:
		return self.__ownership_form
	
	@ownership_form.setter
	def ownership_form(self, value: str) -> None:
		self.__ownership_form = value

	def __str__(self) -> str:
		return f"Name: {self.organization_name}, INN: {self.inn}, Bank Acc: {self.bank_account}, " \
			   f"Corr Acc: {self.correspondent_account}, BIK: {self.bik}, Ownership: {self.ownership_form}"

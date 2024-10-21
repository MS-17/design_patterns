from abc import ABC, abstractmethod

from src.validation.data_validator import DataValidator


class AbstractLogic(ABC):
	"""
	An abstract class that allows to work with the application logic
	"""
	__error_text: str = ""

	@property
	def error_text(self) -> str:
		""" Get an error text """
		return self.__error_text.strip()

	@error_text.setter
	def error_text(self, message: str) -> None:
		""" Set and validate an error text """
		DataValidator().validate_field_type(message, str)
		self.__error_text = message.strip()

	@property
	def is_error(self) -> bool:
		""" A flag that indicates that there's an error (true if there's an error text) """
		return self.error_text != ""

	def _inner_set_exception(self, ex: Exception) -> None:
		""" Set an error text and validate an exception """
		DataValidator().validate_field_type(ex, Exception)
		self.__error_text = f"Exception occured: {ex}"

	@abstractmethod
	def set_exception(self, ex: Exception) -> None:
		""" An abstract method that loads and processes exceptions """
		pass

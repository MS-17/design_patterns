from src.exceptions.argument_exception import ArgumentException
from typing import Any

class DataValidator:
	"""
	A class that validates object type and length
	"""

	@staticmethod
	def validate_field_type(value: Any, type_: object) -> bool:
		"""
		Check if the value is of the given type\n
		value: Any - an object\n
		type_: object - an expected object type\n
		"""
		if not isinstance(value, type_):
			raise ArgumentException("The field type doesn't correspond to the type provided")
		return True

	@staticmethod
	def validate_length(value: Any, len_: int | None = None) -> bool:
		"""
		Check if the value length is less than or equal the provided length\n
		value: Any - an object\n
		len_: int | None - an object expected length\n
		"""
		if not 0 <= len(str(value)) <= len_:
			raise ArgumentException("The object length is more than its expected length")
		return True

	# @staticmethod
	# def validate_exact_length(value: Any, len_: int | None = None) -> bool:
	# 	"""
	# 	Check if the value length is exactly the same as the provided length 
	# 	value: Any - an object 
	# 	len_: int | None - an object expected length
	# 	"""
	# 	if len(str(value)) != len_:
	# 		raise ArgumentException("The object length is not the same as the length provided")

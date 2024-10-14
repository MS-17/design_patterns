from src.models.base.abstract_reference import AbstractReference
from src.validation.data_validator import DataValidator


class BaseModelName(AbstractReference):
	"""
	A base class that implements the compare instances by name functionality\n
	name: str - name\n
	name string type validation included 
	"""
	
	def __init__(self, name: str = "") -> None:
		super().__init__()
		DataValidator().validate_field_type(name, str)
		DataValidator().validate_length(name, 50)
		self.__name = name
	
	@property
	def name(self) -> str:
		return self.__name
	
	@name.setter
	def name(self, value: str) -> None:
		DataValidator().validate_field_type(value, str)
		DataValidator().validate_length(value, 50)
		self.__name = value

	def set_compare_mode(self, other_object: object) -> bool:
		""" Compare this class instance with another class instance by name """
		if other_object is None: return False
		if not isinstance(other_object, BaseModelName): return False
		return self.name == other_object.name
	

class BaseModelUniqueID(AbstractReference):
	"""
	A base class that implements the compare instances by unique id functionality 
	"""

	def set_compare_mode(self, other_object: object) -> bool:
		""" Compare this class instance with another class instance by unique id """
		return super().set_compare_mode(other_object)
	
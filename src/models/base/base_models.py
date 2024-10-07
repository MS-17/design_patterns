from src.models.base.abstract_reference import AbstractReference


class BaseModelName(AbstractReference):
	"""
	A base class that implements the compare instances by name functionality\n
	name: str - name
	"""
	
	def __init__(self, name: str = "") -> None:
		super().__init__()
		self.__name = name
	
	@property
	def name(self) -> str:
		return self.__name
	
	@name.setter
	def name(self, value: str) -> None:
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
	
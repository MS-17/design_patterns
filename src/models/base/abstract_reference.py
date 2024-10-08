from abc import ABC, abstractmethod
import uuid


class AbstractReference(ABC):
	"""
	An abstract class for all models\n
	unique_id: str - an instance unique identifier
	"""

	def __init__(self) -> None:
		super().__init__()
		self.__unique_id: str = uuid.uuid4().hex

	@property
	def unique_id(self) -> str:
		""" Get an instance unique identifier in hex """
		return self.__unique_id
	
	@unique_id.setter
	def unique_id(self, value: str) -> None:
		self.__unique_id = value

	# @property
	# def name(self) -> str:
	# 	return self.__name
	
	# @name.setter
	# def name(self, value: str) -> None:
	# 	self.__name = value

	@abstractmethod
	def set_compare_mode(self, other_object: object) -> bool:
		""" Compare this class instance with another class instance """
		if other_object is None: return False
		if not isinstance(other_object, AbstractReference): return False
		return self.unique_id == other_object.unique_id

	def __eq__(self, obj: object) -> bool:
		return self.set_compare_mode(obj)
	

# compare modes: by name and by unique id. Implement BaseModelName to make 1 and BaseModelCode to make 2
# For ex, it's simplier to compare measurement units by names not codes that's why we inherit it from BaseModelName
# on the contrary it's better to compare nomenclature by id so it should inhert BaseModelCode

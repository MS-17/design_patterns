from abc import ABC, abstractmethod
import uuid

class AbstractReference(ABC):
	"""
	An abstract class for all models 
	unique_id: str - an instance unique identifier
	"""
	__unique_id: str = uuid.uuid4()

	def __init__(self):
		pass

	@property
	def unique_id(self) -> str:
		""" Get an instance unique identifier """
		return self.__unique_id

	@abstractmethod
	def set_compare_mode(self, other_object) -> bool:
		""" Compare this class instance with another class instance """
		if other_object is None: return False
		if not isinstance(other_object, AbstractReference): return False
		return self.unique_id == other_object.unique_id

	def __eq__(self, obj: object) -> bool:
		return self.set_compare_mode(obj)

from src.abstract_reference import AbstractReference


class Nomenclature(AbstractReference):
	"""
	Nomenclature model
	name: str
	"""
	__name: str = ""

	def __init__(self):
		pass

	@property
	def name(self) -> str:
		return self.__name

	@name.setter
	def name(self, value: str):
		self.__name = value

	def set_compare_mode(self, other_object):
		return super().set_compare_mode(other_object)

	def __eq__(self, obj: object) -> bool:
		return self.set_compare_mode(obj)

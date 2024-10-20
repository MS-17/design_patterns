from src.models.base.base_models import BaseModelName


class NomenclatureGroup(BaseModelName):
	"""
	A class that defines a nomenclature group model
	"""

	@staticmethod
	def default_group_raw_materials():
		""" Default nomenclature group raw materials (сырье) (factory method) """
		item = NomenclatureGroup()
		item.name = "Raw materials"
		return item

	@staticmethod
	def default_group_frozen_items():
		""" Default nomenclature group frozen items (заморозка) (factory method) """
		item = NomenclatureGroup()
		item.name = "Frozen items"
		return item

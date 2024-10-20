import pytest

from src.models.nomenclature.nomenclature_group_model import NomenclatureGroup


class TestNomenclatureGroupModel:
	def test_default_group_raw_materials(self):
		nmg = NomenclatureGroup()
		d = nmg.default_group_raw_materials()
		assert d.name == "Raw materials"

	def test_default_group_frozen_items(self):
			nmg = NomenclatureGroup()
			d = nmg.default_group_frozen_items()
			assert d.name == "Frozen items"

import pytest

from src.models.nomenclature.nomenclature_group_model import NomenclatureGroup
from src.exceptions.argument_exception import ArgumentException


class TestNomenclatureGroupModel:
	def test_create(self):
		nmg = NomenclatureGroup.create("name")
		assert nmg.name == "name"

	def test_create_empty_arg(self):
		nmg = NomenclatureGroup.create()
		assert nmg.name == ""

	def test_create_invalid_arg_type(self):
		with pytest.raises(ArgumentException):
			NomenclatureGroup.create(True)
		with pytest.raises(ArgumentException):
			NomenclatureGroup.create(None)

import pytest, os, json

from src.models.nomenclature.nomenclature_model import Nomenclature
from src.models.nomenclature.nomenclature_group_model import NomenclatureGroup
from src.models.measures.measurement_unit_model import MeasurementUnit
from src.exceptions.argument_exception import ArgumentException


class TestNomenclatureModel:
	def test_initialization(self):
		nmg = NomenclatureGroup()
		mum = MeasurementUnit("gram", 1.0)
		name = "full name"
		nm1 = Nomenclature(name, nmg, mum)
		assert nm1.full_name == name
		assert nm1.nomenclature_group == nmg
		assert nm1.measurement_unit == mum

	def test_init_none(self):
		nm = Nomenclature()
		assert nm.full_name is None
		assert nm.nomenclature_group is None
		assert nm.measurement_unit is None

	def test_init_fields_validation(self):
		# with pytest.raises(ArgumentException):
		# 	Nomenclature(1)
		with pytest.raises(ArgumentException):
			Nomenclature("1" * 256)
		# with pytest.raises(ArgumentException):
		# 	Nomenclature("1", 1.0)
		# with pytest.raises(ArgumentException):
		# 	Nomenclature("1", NomenclatureGroup(), {})

	def test_setters(self):
		nm = Nomenclature()
		name = "name"
		mum = MeasurementUnit("gram", 1.0)
		nmg = NomenclatureGroup()
		nm.full_name = name
		nm.measurement_unit = mum
		nm.nomenclature_group = nmg
		assert nm.full_name == name
		assert nm.measurement_unit == mum
		assert nm.nomenclature_group == nmg

	def test_setters_type_validation(self):
		nm = Nomenclature()
		with pytest.raises(ArgumentException):
			nm.full_name = 1.0
		with pytest.raises(ArgumentException):
			nm.measurement_unit = True
		with pytest.raises(ArgumentException):
			nm.nomenclature_group = {}

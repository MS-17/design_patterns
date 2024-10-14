import pytest

from src.models.measures.measurement_unit_model import MeasurementUnit
from src.exceptions.argument_exception import ArgumentException


class TestMeasurementUnitModel:
	def test_init(self):
		name = "kilogram"
		value = 1000.0
		base_unit = MeasurementUnit("gram", 1.0)
		mu = MeasurementUnit(name, value, base_unit)
		assert mu.base_unit == base_unit
		assert mu.name == name
		assert mu.value == value

	def test_init_fields_validation(self):
		with pytest.raises(ArgumentException):
			MeasurementUnit(1, 1.0)
		with pytest.raises(ArgumentException):
			MeasurementUnit("1", True)

	def test_setters(self):
		name = "name"
		value = 5.0
		bm = MeasurementUnit("name", 10.0)
		mu = MeasurementUnit("", 1.0)
		mu.name = name
		mu.value = value
		mu.base_unit = bm
		assert mu.name == name
		assert mu.value == value
		assert mu.base_unit == bm

	def test_setters_type_validation(self):
		mu = MeasurementUnit("", 1.0)
		with pytest.raises(ArgumentException):
			mu.name = 1
		with pytest.raises(ArgumentException):
			mu.value = True
		with pytest.raises(ArgumentException):
			mu.base_unit = {}

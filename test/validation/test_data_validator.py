import pytest

from src.validation.data_validator import DataValidator
from src.exceptions.argument_exception import ArgumentException


class TestDataValidator:
	def test_validate_field_type(self):
		value = "a"
		dv = DataValidator().validate_field_type(value, str)
		assert dv == True

	def test_validate_field_type_nullability(self):
		value = None
		assert DataValidator().validate_field_type(value, str, True) == True

	def test_validate_field_type_fail(self):
		value = "a"
		with pytest.raises(ArgumentException):
			dv = DataValidator().validate_field_type(value, int)

	def test_validate_length(self):
		value1 = "438939"
		value2 = ""
		dv1 = DataValidator().validate_length(value1, 6)
		dv2 = DataValidator().validate_length(value1, 7)
		dv3 = DataValidator().validate_length(value2, 0) 
		assert dv1 == True
		assert dv2 == True
		assert dv3 == True

	def test_validate_length_fail(self):
		value = "3984"
		with pytest.raises(ArgumentException):
			dv = DataValidator().validate_length(value, 1)

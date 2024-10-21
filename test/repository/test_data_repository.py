import pytest

from src.repository.data_repository import DataRepository
from src.exceptions.argument_exception import ArgumentException


class TestDataRepository:
	def test_init_singleton(self):
		dr1 = DataRepository()
		dr2 = DataRepository()
		assert id(dr1) == id(dr2)

	def test_data_getter(self):
		dr = DataRepository()
		assert dr.data == {}

	def test_nomenclature_group_key_staticmethod(self):
		assert DataRepository().nomenclature_group_key() == "nomenclature_group"

	def test_error_text_getter_setter(self):
		message = "Error text"
		dr = DataRepository()
		dr.error_text = message
		assert dr.error_text == message

	def test_error_text_setter_validation(self):
		dr = DataRepository()
		with pytest.raises(ArgumentException):
			dr.error_text = 1

	def test_set_exception(self):
		dr = DataRepository()
		dr.set_exception(ArgumentException())
		assert dr.is_error == True
		assert dr.error_text == "Exception occured:"

	def test_set_exception_validation(self):
		dr = DataRepository()
		with pytest.raises(ArgumentException):
			dr.set_exception(1)

import pytest

from src.models.base.base_models import BaseModelName, BaseModelUniqueID
from src.exceptions.argument_exception import ArgumentException


class TestBaseModelName:
	def test_initialization(self):
		name = "name"
		bmn = BaseModelName(name)
		assert bmn.name == name
	
	def test_init_invalid_name_type(self):
		with pytest.raises(ArgumentException):
			bmn = BaseModelName(1)

	def test_init_invalid_name_length(self):
		with pytest.raises(ArgumentException):
			bmn = BaseModelName("1" * 60)

	def test_name_setter(self):
		name = "some name"
		bmn = BaseModelName()
		bmn.name = name
		assert bmn.name == name

	def test_name_setter_invalid_name_type(self):
		bmn = BaseModelName()
		with pytest.raises(ArgumentException):
			bmn.name = 1.0
	
	def test_name_setter_invalid_name_length(self):
		bmn = BaseModelName()
		with pytest.raises(ArgumentException):
			bmn.name = "1" * 60
	
	def test_unique_id(self):
		bmn1 = BaseModelName()
		bmn2 = BaseModelName()
		assert bmn1.unique_id != bmn2.unique_id 

	def test_set_compare_mode(self):
		bmn1 = BaseModelName("name")
		bmn2 = BaseModelName("name")
		bmn3 = BaseModelName("other name")
		a = ""
		assert bmn1.set_compare_mode(None) == False
		assert bmn1.set_compare_mode(a) == False
		assert bmn1.set_compare_mode(bmn2) == True
		assert bmn1.set_compare_mode(bmn3) == False

	def test_eq(self):
		bmn1 = BaseModelName("name")
		bmn2 = BaseModelName("name")
		bmn3 = BaseModelName("other name")
		bmn4 = BaseModelName()
		bmn5 = BaseModelName()
		a = ""
		assert bmn1 == bmn2
		assert bmn1 != bmn3
		assert bmn1 != a
		assert bmn4 == bmn5
		assert bmn1 != bmn5


class TestBaseModelUniqueID:
	def test_uid_setter(self):
		bmu = BaseModelUniqueID()
		id_ = "some unique id"
		bmu.unique_id = id_
		assert bmu.unique_id == id_

	def test_unique_id(self):
		bmu1 = BaseModelUniqueID()
		bmu2 = BaseModelUniqueID()
		assert bmu1.unique_id != bmu2.unique_id

	def test_set_compare_mode(self):
		bmu1 = BaseModelUniqueID()
		bmu2 = BaseModelUniqueID()
		a = ""
		assert bmu1.set_compare_mode(bmu2) == False
		assert bmu1.set_compare_mode(None) == False
		assert bmu1.set_compare_mode(a) == False
		bmu1.unique_id = "a"
		bmu2.unique_id = "a"
		assert bmu1.set_compare_mode(bmu2)
	
	def test_eq(self):
		bmu1 = BaseModelUniqueID()
		bmu2 = BaseModelUniqueID()
		a = ""
		assert bmu1 != bmu2
		assert bmu1 != None
		assert bmu1 != a
		bmu1.unique_id = "a"
		bmu2.unique_id = "a"
		assert bmu1 == bmu2

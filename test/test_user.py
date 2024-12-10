from src.models.user import User
import pytest
from src.exceptions.argument_exception import ArgumentException


class TestUser:
	def test_setters(self):
		code = "code"
		login = "login"
		password = "p9834438"
		name = "name"
		email = "example@gmail.com"
		u = User()
		u.code = code
		u.login = login
		u.password = password
		u.name = name
		u.email = email
		assert u.code == code
		assert u.login == login
		assert u.password == password
		assert u.name == name
		assert u.email == email

	def test_create(self):
		code = "code"
		login = "login"
		password = "p9834438"
		name = "name"
		email = "example@gmail.com"
		u = User.create(code, login, password, name, email)
		assert u.code == code
		assert u.login == login
		assert u.password == password
		assert u.name == name
		assert u.email == email

	def test_empty_arg(self):
		with pytest.raises(ArgumentException):
			u = User.create(1)
		with pytest.raises(ArgumentException):
			u = User.create("", 1)
		with pytest.raises(ArgumentException):
			u = User.create("", "", 1)
		with pytest.raises(ArgumentException):
			u = User.create("", "", "", 1)
		with pytest.raises(ArgumentException):
			u = User.create("", "", "", "", 1)
	
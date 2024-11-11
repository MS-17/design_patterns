import pytest

from src.service.start_service import StartService
from src.settings_manager import SettingsManager
from src.repository.data_repository import DataRepository
from src.exceptions.argument_exception import ArgumentException


class TestStartService:
	def test_init_service(self):
		dr = DataRepository()
		s = StartService(dr)
		assert s is not None

	def test_init_service_validation(self):
		with pytest.raises(ArgumentException):
			StartService(None)

	def test_create(self):
		dr = DataRepository()
		s = StartService(dr)
		s.create()
		print(dr.data)

	def test_set_exception(self):
		dr = DataRepository()
		s = StartService(dr)
		s.set_exception(ArgumentException())
		assert s.error_text == "Exception occured:"

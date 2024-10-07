import pytest, os, json

from src.models.settings.settings_model import Settings
from src.settings_manager import SettingsManager
from src.exceptions.argument_exception import ArgumentException


class TestSettingsModel:
	def test_settings(self):
		s = Settings()
		s.organization_name = "A"
		s.inn = "3498"
		s.bank_account = "39848"
		s.correspondent_account = "39848"
		s.bik = "39488"
		s.ownership_form = "type"
		assert s.organization_name == "A"
		assert s.inn == "3498"
		assert s.bank_account == "39848"
		assert s.correspondent_account == "39848"
		assert s.bik == "39488"
		assert s.ownership_form == "type"

	def test_settings_setters_wrong_value(self):
		s = Settings()
		with pytest.raises(ArgumentException):
			s.inn = "3498394839483"
		with pytest.raises(ArgumentException):
			s.bank_account = "39848394883948398498"
		with pytest.raises(ArgumentException):
			s.correspondent_account = "398483948934893"
		with pytest.raises(ArgumentException):
			s.bik = "39488394838943"
		with pytest.raises(ArgumentException):
			s.ownership_form = "typkladsjf"

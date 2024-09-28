import pytest
from src.models.settings import Settings

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
		
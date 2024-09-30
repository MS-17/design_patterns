import pytest, os, json
# import unittest
from src.models.settings import Settings
from src.settings_manager import SettingsManager


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

	@pytest.mark.parametrize("settings_path", ["configuration/settings.json", "configuration/config.json"])
	def test_settings_manager_load_settings(self, settings_path):
		settings_manager = SettingsManager()
		settings_manager.load_settings(settings_path)
		settings = settings_manager.settings
		with open(settings_path, 'r') as file:
			data = json.load(file)
		assert settings.organization_name == data["organization_name"]
		assert settings.inn == data["inn"]
		assert settings.bank_account == data["bank_account"]
		assert settings.correspondent_account == data["correspondent_account"]
		assert settings.bik == data["bik"]
		assert settings.ownership_form == data["ownership_form"]
		
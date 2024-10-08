import pytest, json, os

from src.settings_manager import SettingsManager
from src.exceptions.argument_exception import ArgumentException


class TestSettingsManager:
	@pytest.mark.parametrize("settings_path", [f"test{os.sep}test_data{os.sep}settings.json", 
												f"test{os.sep}test_data{os.sep}config.json"])
	def test_load_settings(self, settings_path):
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


	def test_load_setting_wrong_fields_length(self):
		settings_manager = SettingsManager()
		with pytest.raises(ArgumentException):
			settings_manager.load_settings(f"test{os.sep}test_data{os.sep}wrong_settings.json")

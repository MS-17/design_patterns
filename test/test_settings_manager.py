import pytest, json

from src.settings_manager import SettingsManager


class TestSettingsManager:
	@pytest.mark.parametrize("settings_path", ["test/test_data/settings.json", "test/test_data/config.json"])
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
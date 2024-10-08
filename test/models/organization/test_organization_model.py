import pytest, os, json

from src.models.organization.organization_model import Organization
from src.settings_manager import SettingsManager


@pytest.fixture(scope="class")
def define_settings():
	file_name = f"test{os.sep}test_data{os.sep}settings_for_organization.json"
	s = SettingsManager()
	s.load_settings(file_name)
	return s.settings, file_name


class TestOrganizationModel:
	def test_initialization(self, define_settings):
		settings = define_settings[0]
		file_name = define_settings[1]
		org = Organization(settings)
		with open(file_name, 'r') as f:
			data = json.load(f)
		assert org.name == data["organization_name"]
		assert org.inn == data["inn"]
		assert org.bik == data["bik"]
		assert org.bank_account == data["bank_account"]
		assert org.ownership_form == data["ownership_form"]

	def test_setters(self, define_settings):
		org = Organization(define_settings[0])
		org.inn = "398493"
		org.bik = "398493"
		org.bank_account = "398493"
		org.ownership_form = "form"
		assert org.inn == "398493"
		assert org.bik == "398493"
		assert org.bank_account == "398493"
		assert org.ownership_form == "form"

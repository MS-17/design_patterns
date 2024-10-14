import pytest, os, json

from src.models.organization.organization_model import Organization
from src.settings_manager import SettingsManager
from src.exceptions.argument_exception import ArgumentException


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
	
	def test_init_none(self):
		org = Organization()
		assert org.name == ""

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

	def test_setters_type_validation(self):
		org = Organization()
		with pytest.raises(ArgumentException):
			org.inn = 1.0
		with pytest.raises(ArgumentException):
			org.bik = True
		with pytest.raises(ArgumentException):
			org.bank_account = {}
		with pytest.raises(ArgumentException):
			org.ownership_form = []

	def test_setters_length_validation(self):
		org = Organization()
		with pytest.raises(ArgumentException):
			org.inn = "39483948938493499384"
		with pytest.raises(ArgumentException):
			org.bik = "39483948938493499384"
		with pytest.raises(ArgumentException):
			org.bank_account = "39483948938493499384"
		with pytest.raises(ArgumentException):
			org.ownership_form = "form1form"

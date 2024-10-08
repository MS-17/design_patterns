import pytest

from src.models.base.abstract_reference import AbstractReference


class TestAbstractReference:
	def test_initialization(self):
		with pytest.raises(TypeError):
			ar = AbstractReference()

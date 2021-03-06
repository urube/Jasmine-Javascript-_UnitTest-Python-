import pytest
import controller
from donor import Donor
import re


class TestDonorStr:

    @pytest.fixture(scope='session')
    def set_data(self):
        donor = Donor('id', 'first_name', 'last_name', 'gender')
        return donor

    def test_a_display_donor__str__exists(self, set_data):
        donor = set_data
        assert type(donor).__str__ is not object.__str__

    def test_b_display_donor__str__returns_string(self, set_data):
        donor = set_data
        returned = str(donor)
        assert isinstance(returned, str)

    def test_c_display_member__str__works(self, set_data):
        donor = set_data
        returned = str(donor)
        assert returned == 'last_name, first_name [gender]'


class TestBloodBankDisplayDonors:

    def test_d_club_display_donors_correct_format(self):
        blood_bank = controller.setup()
        returned = blood_bank.display_donor()
        assert returned == 'Moore, Sandy [F]\nMcDonald, Daniel [M]\nWatson, ' \
                           'Cathy [F]\nBurk, John [M]\nWatts, Jonathan [M]\n'

    def test_e_club_display_last_name(self):
        blood_bank = controller.setup()
        returned = blood_bank.display_donor()
        expected = r'^Moore.*\nMcDonald.*\nWatson.*\nBurk.*\nWatts.*\n'
        assert re.search(expected, returned)

    def test_f_club_display_punctuation_after_last_name(self):
        blood_bank = controller.setup()
        returned = blood_bank.display_donor()
        expected = r'[,]'
        assert re.search(expected, returned)

    def test_g_club_display_space_after_punctuation(self):
        blood_bank = controller.setup()
        returned = blood_bank.display_donor()
        expected = r'[,\s]'
        assert re.search(expected, returned)

    def test_h_club_display_first_name(self):
        blood_bank = controller.setup()
        returned = blood_bank.display_donor()
        expected = r'.*Sandy.*\n.*Daniel.*\n.*Cathy.*\n.*John.*\n.*Jonathan.*'
        assert re.search(expected, returned)

    def test_i_club_display_space_after_first_name(self):
        blood_bank = controller.setup()
        returned = blood_bank.display_donor()
        expected = r'[,\s]'
        assert re.search(expected, returned)

    def test_j_club_display_ids(self):
        blood_bank = controller.setup()
        returned = blood_bank.display_donor()
        expected = r'[F]'
        assert re.search(expected, returned)

    def test_k_club_end_line(self):
        blood_bank = controller.setup()
        returned = blood_bank.display_donor()
        expected = r'\n'
        assert re.search(expected, returned)


if __name__ == '__main__':
    pytest.main(['-vv', '-s', 'pytest_question03.py'])

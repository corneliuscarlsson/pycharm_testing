from unittest import TestCase
from gender_converter import convert_gender

class Test(TestCase):
    def test_convert_gender_male(self):
        expected = "MALE"
        actual = convert_gender("M")
        self.assertEqual(expected, actual)

    def test_convert_gender_female(self):
        expected = "FEMALE"
        actual = convert_gender("F")
        self.assertEqual(expected, actual)
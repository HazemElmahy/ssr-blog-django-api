from django.test import TestCase

from app.calc import add, subtract


class CalcTest(TestCase):
    def test_add_numbers(self):
        """Test that 2 numbers are added together"""
        self.assertEqual(add(2, 3), 5)

    def test_subtract_numbers(self):
        """Test that numbers are subtracted"""
        self.assertEqual(subtract(10, 2), 8)

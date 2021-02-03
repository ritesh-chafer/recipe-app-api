from django.test import TestCase

from .calc import add, subtract

class CalcTests(TestCase):

    def test_add_numers(self):
        """Test that two numbers are added together"""
        self.assertEqual(add(3,8), 11)
    
    def test_subtract_numers(self):
        """Test that two numbers are subtracted and returns"""
        self.assertEqual(subtract(5,11), 6)
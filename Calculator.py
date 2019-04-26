#master

#示範Git用的程式碼！
import unittest

def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def times(a, b):
    return a * b

def divided(a, b):
    if b != 0:
        return a / b
    return "無限"
	
class TestCalculator(unittest.TestCase):
	def test_int_add(self):
		self.assertEqual(add(9, 3), 12)
			
	def test_int2_add(self):
		self.assertEqual(add(9, 4), 13)
		
	def test_float_add(self):
		self.assertEqual(add(4.2, 3), 7.2)
		
	def test_int_minus(self):
		self.assertEqual(add(9, 3), 6)
		
	def test_int2_minus(self):
		self.assertEqual(add(9, 4), 5)
		
	def test_float_minus(self):
		self.assertEqual(add(4.2, 3.2), 1.0)
		
	def test_int_times(self):
		self.assertEqual(add(9, 3), 27)
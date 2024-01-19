import unittest
from division import dividir

class TestDivision(unittest.TestCase):
 
 def test_multiplicar(self):
    self.assertEqual(dividir(8, 2), 4)
    self.assertEqual(dividir(10, 1), 10)
    self.assertEqual(dividir(20, 10), 2)

if __name__ == '__main__':
 unittest.main()

import unittest
#hola #hola # holag 

from app.multi import multiplicacion

class TestMilti(unittest.TestCase):
    def test_multi(self):
        self.assertEqual(multiplicacion(2,4), 8)

if __name__=='__mian__':
    unittest.main()

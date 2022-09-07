import unittest
import test
class testCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(test.add(1,3),1+3)
        self.assertEqual(test.add(4,8),12)
        self.assertEqual(test.add(6,9),15)
    def test_subtract(self):
        self.assertEqual(test.subtract(1,1),0)
        self.assertEqual(test.subtract(4,8),-4)
        self.assertEqual(test.subtract(5,0),5)
    def test_multiply(self):
        self.assertEqual(test.multiply(1,3),3)
        self.assertEqual(test.multiply(4,8),32)
        self.assertEqual(test.multiply(6,9),54)
    def test_divide(self):
        self.assertEqual(test.divide(1,1),1)
        self.assertEqual(test.divide(4,8),0.5)
        self.assertEqual(test.divide(5,1),5)
        self.assertRaises(ValueError,test.divide,10,0)











if __name__ == "__main__":
    unittest.main()
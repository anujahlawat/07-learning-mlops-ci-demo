import unittest
from app1 import add, sub, mul   #app1.py se import kr rhe h ... 

class TestMathfunctions(unittest.testCase): #yha har fn ka kaam h ek corresponding fn ko test krna ... 
    def test_add(self):
        self.assertEqual(add(4, 5), 9)
        self.assertEqual(add(-1, 1), 0)
    
    def test_sub(self):
        self.assertEqual(sub(4, 5), -1)
        self.assertEqual(sub(-1, 1), 0)

    def test_mul(self):
        self.assertEqual(mul(4, 5), 20)
        self.assertEqual(mul(-1, 1), -1)

if __name__ == '__main__':
    unittest.main()



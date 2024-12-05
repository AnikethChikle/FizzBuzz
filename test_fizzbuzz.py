import unittest
from fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    
    def test_fizzbuzz(self):
        # Testing multiples of 3, 5, and both 3 and 5
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
        
        # Testing numbers that are not multiples of 3 or 5
        self.assertEqual(fizzbuzz(1), "1")
        self.assertEqual(fizzbuzz(2), "2")
        self.assertEqual(fizzbuzz(7), "7")
        
    def test_range(self):
        # Testing the full range from 1 to 100
        for i in range(1, 101):
            result = fizzbuzz(i)
            if i % 3 == 0 and i % 5 == 0:
                self.assertEqual(result, "FizzBuzz")
            elif i % 3 == 0:
                self.assertEqual(result, "Fizz")
            elif i % 5 == 0:
                self.assertEqual(result, "Buzz")
            else:
                self.assertEqual(result, str(i))

if __name__ == '__main__':
    unittest.main()

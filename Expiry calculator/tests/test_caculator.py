import unittest
from expiry_calculator import calculate_expiry_date

class TestCalculateExpiryDate(unittest.TestCase):
    
    def test_calculate_expiry_date(self):
        start_date = "2020-01-01"
        duration = 5
        expected_expiry_date = "2025-01-01"
        result = calculate_expiry_date(start_date, duration, 'years')
        self.assertEqual(result, expected_expiry_date)
        
        
    def test_invalid_unit(self):
        start_date = "2020-01-01"
        duration = 5
        with self.assertRaises(ValueError):
            calculate_expiry_date(start_date, duration, 'days')
        
            

if __name__ == '__main__':
    unittest.main()
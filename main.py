import unittest
from unittest.mock import patch

from math import gcd
from sum_numbers import sum_numbers
from obtain_price import obtain_price
from payment import payment

class TestSumNumbers(unittest.TestCase):

    @patch('sum_numbers.obtain_numbers')
    def test_sum_numbers(self,mock_obtain_numbers):

        # Arrange
        mock_obtain_numbers.return_value = [1,2,3,4,5]
        
        # Act
        result = sum_numbers()

        # Assert
        self.assertEqual(result,15)
        mock_obtain_numbers.assert_called_once()

class TestObtainPrice(unittest.TestCase):

    @patch('obtain_price.price')
    def test_obtain_price(self,mock_obtain_price):

        # Arrange
        mock_obtain_price.return_value = 10
        
        # Act
        result = obtain_price()

        # Assert
        self.assertEqual(result,10)
        mock_obtain_price.assert_called_once()
    
class TestPayment(unittest.TestCase):

    @patch('payment.verify_inventory')
    @patch('payment.payment_process')
    @patch('payment.update_inventory')
    def test_payment(self, mock_verify_inventory, mock_payment_process, mock_update_inventory):

        # Arrange
        mock_verify_inventory.return_value = True
        mock_payment_process.return_value = True
        mock_update_inventory.return_value = True
        
        # Act
        result = payment()

        # Assert
        self.assertEqual(result, True)
        mock_verify_inventory.assert_called_once()
        mock_payment_process.assert_called_once()
        mock_update_inventory.assert_called_once()
    


if __name__ == '__main__':
    unittest.main()
#653380042-6 พิทักษ์พงศ์ สุภาพเพ็ชร sec.2

from unittest.mock import patch
from assignment.source.currency_exchanger import CurrencyExchanger
from assignment.tests.utils import get_mock_currency_api_response
import unittest

class TestCurrencyExchanger(unittest.TestCase):
    def setUp(self):
        self.currency = CurrencyExchanger()
        self.mock_api_response = get_mock_currency_api_response()

    @patch("assignment.source.currency_exchanger.requests")
    def test_get_currency(self, mock_request):
        mock_request.get.return_value = self.mock_api_response

        self.currency.get_currency_rate()

        mock_request.get.assert_called_once()

        self.assertEqual(self.currency.api_response, {'base': 'THB', 'result': {'KRW': 38.69}})

if __name__ == '__main__':
    unittest.main()

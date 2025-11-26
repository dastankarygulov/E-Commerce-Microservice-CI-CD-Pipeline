# test_app.py
import unittest
import json
from app import app

class TestProductCatalog(unittest.TestCase):

    def setUp(self):
        # Set up a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_get_products_success(self):
        # Test the main products endpoint
        response = self.app.get('/products')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertIsInstance(data, list)
        self.assertTrue(len(data) > 0) # Ensure products were returned

    def test_health_check_success(self):
        # Test the health check endpoint
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['status'], 'ok')

if __name__ == '__main__':
    unittest.main()

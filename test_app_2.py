import unittest
from app import app

class TestApp2(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_home_page_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_hello_endpoint(self):
        response = self.client.post('/hello', data={'username': 'testuser'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello testuser', response.data)

    def test_sum_endpoint(self):
        response = self.client.post('/sum', data={'a': '10', 'b': '20'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'30.0', response.data)

    def test_invalid_sum(self):
        response = self.client.post('/sum', data={'a': 'invalid', 'b': '5'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid input', response.data)

if __name__ == "__main__":
    unittest.main()
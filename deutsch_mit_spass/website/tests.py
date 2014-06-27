from django.test import TestCase

class DeutschMitSpassCase(TestCase):
    def test_index(self):
        resp = self.client.get('/website/')
        self.assertEqual(resp.status_code, 200)

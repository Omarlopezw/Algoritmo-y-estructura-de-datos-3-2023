import unittest
class TestEjemplos(unittest.TestCase):

    def setUp(self):
        print('Entra setUp')

    def tearDown(self):
        print('Entra tearDown')

    def test_1(self):
        print('Test: test_1')

    def test_2(self):
        print('Test: test_2')
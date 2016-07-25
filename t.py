import unittest
import random
from flaky import flaky

class TestT(unittest.TestCase):
    def test_foo_1(self):
        self.assertTrue(random.randint(0, 30) <= 10)

    def test_foo_2(self):
        self.assertTrue(random.randint(0, 30) <= 10)

    def test_foo_3(self):
        self.assertTrue(random.randint(0, 30) <= 10)

    def test_foo_4(self):
        self.assertTrue(random.randint(0, 30) <= 10)

    def test_foo_5(self):
        self.assertTrue(random.randint(0, 30) <= 10)

    def test_foo_6(self):
        self.assertTrue(random.randint(0, 30) <= 10)

    def test_foo_7(self):
        self.assertTrue(random.randint(0, 30) <= 10)

    def test_foo_8(self):
        self.assertTrue(random.randint(0, 30) <= 10)

    def test_foo_9(self):
        self.assertTrue(random.randint(0, 30) <= 10)

    def test_foo_10(self):
        self.assertTrue(random.randint(0, 30) <= 10)

# I already have plenty of experience with unittest.
# This is here as a general reminder:

from unittest import TestCase

class TryTesting(TestCase):
    def test_always_passes(self):
        self.assertTrue(True)

    def test_always_fails(self):
        self.assertTrue(False)

# For using pytest you need to pip install it. Here are
# some general examples:

def test_always_passes():
    assert True

def test_always_fails():
    assert False
    
def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"

def test_reversed():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]

def test_some_primes():
    assert 37 in {
        num
        for num in range(1, 50)
        if num != 1 and all(num % div != 0 for div in range(2, num))
    }

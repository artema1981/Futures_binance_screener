from django.test import TestCase
import pytest
# Create your tests here.

def test_example():
    assert 1==1



@pytest.fixture
def fixture_1():
    print('run-fixture-1')
    return 1

def test_example1(fixture_1):
    num = fixture_1
    assert num == 1


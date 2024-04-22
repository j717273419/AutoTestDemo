import pytest


@pytest.fixture
def fixture():
    print('fixture')

def test_fixture1(fixture):
    assert  1 == 1
def test_fixture2():
    assert 2 == 2

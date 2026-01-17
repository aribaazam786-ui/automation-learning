import pytest
@pytest.mark.sanity
def test_sanity1():
    print('Sanity 1')

@pytest.mark.sanity
def test_sanity2():
    assert 2+2==4

@pytest.mark.xfail
def test1():
    print('Hello world')

@pytest.mark.skip(reason="this is a skip")
def test2():
    print('Skip Method')
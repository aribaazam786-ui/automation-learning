import pytest
@pytest.fixture(autouse=True, scope='package')
def setup():
    print('Open Browser')
    print('login')
    yield
    print('logout')
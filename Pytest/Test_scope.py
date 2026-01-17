import pytest
@pytest.fixture(autouse=True, scope='package')
def setup():
    print('Open Browser')
    print('login')
    yield
    print('logout')

class Test_fix:
    def testAddProduct25(self):
        print('Add Product25')

    def testCheckProduct(self):
        print('testCheckProduct')

    def testCheckProduct2(self):
        print('testCheckProduct2')




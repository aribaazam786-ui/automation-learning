import pytest
from selenium import webdriver

@pytest.fixture(autouse=True, scope="function")
def setup(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    request.cls.driver = driver
    yield
    driver.quit()

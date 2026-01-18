from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import pytest_check as check

class TestProduct():
    driver: WebDriver



    def test_AddProd(self):
        self.driver.find_element(By.CSS_SELECTOR, "[placeholder=Username]").send_keys("standard_user")
        self.driver.find_element(By.CSS_SELECTOR, "[placeholder=Password]").send_keys("secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR, '#login-button').click()
        # Add Product
        self.driver.find_element(By.XPATH, '(//button[text()="Add to cart"])[1]').click()
        Price = self.driver.find_element(By.XPATH, '(//div[@class="inventory_item_price"])[1]').text
        # Saving price value and replacing the $
        print(Price)
        Price = Price.replace('$', "")
        p = float(Price)
        print(p)
        check.equal(p,29.99)




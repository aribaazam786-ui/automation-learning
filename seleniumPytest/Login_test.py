from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import pytest_check as check



class TestLogin():
    driver: WebDriver

    def test_blankField(self):
        # Testcase: 2 Blank Fields
        self.driver.find_element(By.XPATH, "//input[@id='login-button']").click()
        Username = self.driver.find_element(By.CLASS_NAME, "error-message-container").text
        print(Username)
        check.equal(Username,"Epic sadface: Username is required")

    def test_check_pass(self):
        self.driver.refresh()
        # TestCase: 3 Username enter to check password validation

        self.driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
        self.driver.find_element(By.XPATH, "//input[@id='login-button']").click()

        val2 = self.driver.find_element(By.CLASS_NAME, "error-message-container").text
        print(val2)
        check.equal(val2,"Epic sadface: Password is required")



    # Testcase: 4 Enter Password to check username
    def test_usernameCheck(self):
        self.driver.refresh()
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
        self.driver.find_element(By.XPATH, "//input[@id='login-button']").click()
        val3 = self.driver.find_element(By.CLASS_NAME, "error-message-container").text
        check.equal(val3,"Epic sadface: Username is required")
        print("PASSED")




    def test_username_pass(self):
        self.driver.refresh()
        self.driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("hello")
        self.driver.find_element(By.XPATH, "//input[@id='login-button']").click()
        val4 = self.driver.find_element(By.CLASS_NAME, "error-message-container").text
        print(val4)
        check.equal(val4, "Epic sadface: Password does not match any user in this service")
        print("PASSED")

    def test_success(self):
            self.driver.refresh()
            # Testcase: 6 Login successfully
            self.driver.find_element(By.CSS_SELECTOR, "[placeholder=Username]").send_keys("standard_user")
            self.driver.find_element(By.CSS_SELECTOR, "[placeholder=Password]").send_keys("secret_sauce")
            self.driver.find_element(By.CSS_SELECTOR, '#login-button').click()
            check.equal(self.driver.current_url,"https://www.saucedemo.com/inventory.html")
            print("PASSED")





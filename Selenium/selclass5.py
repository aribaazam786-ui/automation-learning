import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#declairng XPath
UserName='//*[@id="user-name"]'
Password='//*[@id="password"]'
Submit='//*[@id="login-butto"]'

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.implicitly_wait(60)
#time.sleep(3)
driver.find_element(By.XPATH,UserName).send_keys('standard_user')
driver.find_element(By.XPATH,Password).send_keys('secret_sauce')
driver.find_element(By.XPATH,Submit).click()
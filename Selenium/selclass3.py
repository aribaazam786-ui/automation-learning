#XPATH INTRO
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options=Options()
options.add_argument('--incognito')
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.saucedemo.com")
driver.find_element(By.XPATH,'//input[@type="text"]').send_keys('standard_user')
driver.find_element(By.XPATH,'//input[@placeholder="Password"]').send_keys('secret_sauce')
""""driver.find_element(By.XPATH, '//input[@id="login-button"]').click()"""
driver.find_element(By.XPATH, '//*[contains(@id,"login-button")]').click()
time.sleep(7)

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


options= Options()
options.add_argument('--incognito')
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.saucedemo.com")
time.sleep(3)
print("Navigating to web")
driver.find_element(By.ID,value='user-name').send_keys('standard_user')
driver.find_element(By.ID,value='password').send_keys('secret_sauce')
driver.find_element(By.ID,value='login-button').click()
print("Code Executed")
time.sleep(2)
driver.execute_script("window.open('')")
driver.switch_to.window(driver.window_handles[1])
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

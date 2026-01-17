import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options=Options()
options.add_argument('--incognito')
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.saucedemo.com")
time.sleep(3)
driver.find_element(By.ID, value='user-name').send_keys('standard_user')
driver.find_element(By.ID, value='password').send_keys('secret_sauce')
driver.find_element(By.ID,value='login-button').click()
time.sleep(3)
print(driver.title)

driver.execute_script("window.open('')")
driver.switch_to.window(driver.window_handles[1])
driver.get("https://demoqa.com/")
time.sleep(5)
driver.execute_script("window.scrollTo(0,400)")
time.sleep(5)
print(driver.current_url)

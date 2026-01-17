import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('incognito')

driver = webdriver.Chrome(options=options)

# ---- TAB 1 ----
driver.get("https://saucedemo.com/")
time.sleep(3)
driver.maximize_window()

driver.find_element(By.ID, "login-button").click()
time.sleep(3)

# ---- OPEN NEW TAB ----
driver.execute_script("window.open('');")

# Switch to the new tab
driver.switch_to.window(driver.window_handles[1])

# ---- TAB 2 ----
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(3)

driver.execute_script("window.scrollTo(0, 400);")
time.sleep(3)

driver.find_element(By.ID, "submit").click()
time.sleep(3)

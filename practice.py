from selenium import webdriver
from func import *
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys




chrome_driver_path=r"C:\Users\marry\Downloads\Automation\chromedriver-win64\chromedriver.exe"
service=Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
wait= WebDriverWait(driver, 10)

driver.get("https://www.linkedin.com/login/")
print(driver.title)


time.sleep(5) # import time
username_field= wait.until(EC.visibility_of_element_located((By.XPATH ," //input[@id='username']")))
#Enter the username
human_typing(username_field, 'marium.abid02@gmail.com')
password_field=wait.until(EC.visibility_of_element_located((By.XPATH ," //input[@id='password']")))
#Enter the username
human_typing(password_field,' 12*Jan2002')
time.sleep(5)
sign_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
sign_in_button.click()
print("Login successful")
time.sleep(20)


# Navigate to "My Network"
my_network = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/mynetwork/')]")))
my_network.click()
print("Navigated to My Network")

# Wait for "Connect" buttons to load
connect_buttons = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[text()='Connect']/ancestor::button")))
if connect_buttons:
    connect_buttons[0].click()  # Click the first "Connect" button
    print("Clicked on the first 'Connect' button")
else:
    print("No 'Connect' buttons found")

# Pause to observe actions
time.sleep(5)

# Close the browser
driver.quit()



import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Setting the path of the Chrome driver executable on my system
path = "C:/Users/iamth/Downloads/chromedriver_win32.exe"

# Initialize a new instance of the Chrome browser
driver = webdriver.Chrome(path)

# Navigate to the login page
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(3)

# Find the username input element by name and enter your username
username_input = driver.find_element(By.NAME, "username")
username_input.send_keys("username")

# Find the password input element by name and enter your password
password_input = driver.find_element(By.NAME, "password")
password_input.send_keys("password")

# Click action - the login button
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()
time.sleep(3)

# Close the browser
driver.quit()

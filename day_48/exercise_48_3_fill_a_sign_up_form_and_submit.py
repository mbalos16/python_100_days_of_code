# Exercise 48.2. Fill a sign up form and submit

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# import time

opt = webdriver.ChromeOptions()
opt.binary_location = (
    "/Users/Maria/Desktop/Python/Python Exercises/assets/chrome_driver"
)
driver = webdriver.Chrome(opt)
driver.get("http://secure-retreat-92358.herokuapp.com/")


first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Maria")


last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Balos")

email = driver.find_element(By.NAME, "email")
email.send_keys("mbalos@uoc.edu")

submit = driver.find_element(By.CSS_SELECTOR, "button")
submit.click()

# time.sleep(4000)

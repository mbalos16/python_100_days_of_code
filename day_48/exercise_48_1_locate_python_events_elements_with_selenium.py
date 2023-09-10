# Exercise 48.1. Locate python events elements with selenium

from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.binary_location = (
    "/Users/Maria/Desktop/Python/Python Exercises/assets/chrome_driver"
)
driver = webdriver.Chrome(opt)
driver.get("https://www.python.org/")

ul_elements = driver.find_element(
    By.XPATH, "/html/body/div[1]/div[3]/div/section/div[2]/div[2]/div/ul"
)
li_elements = ul_elements.find_elements(By.TAG_NAME, "li")

objects = {
    index: {
        "time": element.text.split("\n")[0],
        "name": element.text.split("\n")[1],
    }
    for index, element in enumerate(li_elements)
}
print(objects)

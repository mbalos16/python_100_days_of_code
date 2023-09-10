# Exercise 48.2. Get the number of articles in english in wikipedia

from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.binary_location = (
    "/Users/Maria/Desktop/Python/Python Exercises/assets/chrome_driver"
)
driver = webdriver.Chrome(opt)
driver.get("https://en.wikipedia.org/wiki/Main_Page")


number_articles = driver.find_element(
    By.XPATH,
    "/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[1]/div/div[3]/a[1]",
)

print(number_articles.text)

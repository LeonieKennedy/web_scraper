import time
import random 
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("chromedriver.exe")
previous_sender = 1

url = "https://fakedetail.com/fake-android-text-messenger-generator"
driver.get(url)
sender = random.choice(["1", "2"])

button_number = int(sender) + 1

if previous_sender != sender:
    driver.find_element(By.CSS_SELECTOR, ".nav > li:nth-child(2) > a:nth-child(1)").click()

time.sleep(6)

driver.find_element(By.CSS_SELECTOR, ("#profile1_name")).clear()
driver.find_element(By.CSS_SELECTOR, ("#profile1_name")).send_keys("Kevin")

time.sleep(6)
driver.find_element(By.CSS_SELECTOR, ("#profile"+sender+"_message")).clear()
driver.find_element(By.CSS_SELECTOR, ("#profile"+sender+"_message")).send_keys("Test message")
time.sleep(6)

driver.find_element(By.CSS_SELECTOR, ("#tab-person"+sender+" > div > div:nth-child(" + str(button_number) + ") > button")).click()
time.sleep(6)

driver.find_element(By.CSS_SELECTOR, "#snapshot").click()
time.sleep(8)

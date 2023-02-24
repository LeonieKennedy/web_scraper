import time
import random 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


with open('names.txt') as f:
    names = [name.rstrip('\n') for name in f]

with open('sentances.txt') as f:
    sentences = [sentence.rstrip('\n') for sentence in f]
previous_sender = "1"
driver = webdriver.Chrome("chromedriver.exe")

sentence_no = 96
for i in range(0, 30):

    url = "https://fakedetail.com/fake-android-text-messenger-generator"
    driver.get(url)
    driver.implicitly_wait(20)  # seconds

    driver.find_element(By.CSS_SELECTOR, "#profile1_name").clear()
    driver.find_element(By.CSS_SELECTOR, "#profile1_name").send_keys(names[i+23])


    for j in range(0, 4):
        sender = random.choice(["1", "2"])

        button_number = int(sender) + 1

        if previous_sender != sender:
            previous_sender = sender
            print("prev != send")
            driver.find_element(By.CSS_SELECTOR, "#options > div:nth-child(2) > ul > li:nth-child("+sender+") > a").click()

        print("profile_message")
        WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ("#profile"+sender+"_message")))).clear()
        driver.find_element(By.CSS_SELECTOR, ("#profile"+sender+"_message")).send_keys(sentences[sentence_no])

        driver.find_element(By.CSS_SELECTOR, ("#tab-person"+sender+" > div > div:nth-child(" + str(button_number) + ") > button")).click()
        time.sleep(5)

        sentence_no = sentence_no + 1

    time.sleep(15)
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#snapshot"))).click()
    # driver.find_element(By.CSS_SELECTOR, "#snapshot")

    time.sleep(15)
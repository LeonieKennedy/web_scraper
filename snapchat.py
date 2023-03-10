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

driver = webdriver.Chrome("chromedriver.exe")

for i in range(0, 15):
    print(i)
    previous_sender = "1"
    message_no = "2"
    url = "https://fakeinfo.net/fake-snapchat-chat-generator"
    driver.get(url)
    driver.implicitly_wait(10)  # seconds

    driver.find_element(By.CSS_SELECTOR, "#edit-name").clear()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "#edit-name").send_keys(names[random.randint(0, 49)])
    for j in range(1, 7):
        print(j)
        sender = random.choice(["1", "2"])
        print(previous_sender, sender)
        button_number = "2"
        if previous_sender != sender:
            previous_sender = sender
            print("prev != send")
            driver.find_element(By.CSS_SELECTOR, "#options > div:nth-child(2) > ul > li:nth-child("+sender+") > a").click()
        time.sleep(5)

        if sender == "2":
            driver.find_element(By.CSS_SELECTOR, "#edit-person_name").clear()
            time.sleep(3)
            driver.find_element(By.CSS_SELECTOR, "#edit-person_name").send_keys(names[random.randint(0, 49)])
            button_number = "3"
        WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ("#profile"+sender+"_message")))).clear()
        driver.find_element(By.CSS_SELECTOR, ("#profile"+sender+"_message")).send_keys(sentences[random.randint(0, 726)])

        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, ("#tab-person"+sender+" > div > div:nth-child("+button_number+") > button")).click()
        time.sleep(3)
    time.sleep(5)
    button = driver.find_element(By.CSS_SELECTOR, "#snapshot")
    driver.execute_script("arguments[0].click();", button)
    # WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#snapshot"))).click()
    time.sleep(15)

import time
import random 
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("chromedriver.exe")

url = "https://fakedetail.com/fake-android-text-messenger-generator"
driver.get(url)


sender = random.choice(["profile2", "profile1"])
sender = "profile2"

if sender == "profile1":
    active_xpath = "//*[@id='tab-person1']"
    inactive_xpath = "//*[@id='tab-person2']"

else:
    active_xpath = "//*[@id='tab-person2']"
    inactive_xpath = "//*[@id='tab-person1']"

time.sleep(5)

driver.find_element(By.CSS_SELECTOR, ".nav > li:nth-child(2) > a:nth-child(1)").click()
# tab = driver.find_element(By.XPATH, active_xpath)
time.sleep(5)
# set active profile
tab = driver.find_element(By.XPATH, active_xpath)
driver.execute_script("arguments[0].setAttribute('class','tab-pane active')", tab)

# set inactive profile
tab = driver.find_element(By.XPATH, inactive_xpath)
driver.execute_script("arguments[0].setAttribute('class','tab-pane')", tab)
info = tab.get_attribute("class")

time.sleep(200)

driver.find_element("id", (sender+"_name")).clear()
driver.find_element("id", (sender+"_name")).send_keys("Kevin")


driver.find_element("id", (sender+"_message")).clear()
driver.find_element("id", (sender+"_message")).send_keys("Test message")

driver.find_element("name", "Add Message").click()

# driver.find_element("id", "snapshot").click()


# browser = mechanicalsoup.Browser()
# url = "https://fakedetail.com/fake-android-text-messenger-generator"
# generator_page = browser.get(url)
# generator_html = generator_page.soup
#
# form = generator_html.select("main")
# print(form)
#
#
# form.select("input")[0]["value"] = "12:00 am"
# form.select("input")[1]["value"] = "50"
# form.select("input")[2]["value"] = "Kennedy"
#
# new_page = browser.submit(form, generator_page.url)
#
# print(new_page.url)

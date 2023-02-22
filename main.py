import time

import mechanicalsoup
from selenium import webdriver

driver = webdriver.Chrome("chromedriver.exe")

url = "https://fakedetail.com/fake-android-text-messenger-generator"
driver.get(url)

driver.find_element("id", "profile1_name").clear()
driver.find_element("id", "profile1_name").send_keys("Kevin")

driver.find_element("id", "profile1_message").clear()
driver.find_element("id", "profile1_message").send_keys("New message")

driver.find_element("name", "Add Message").click()

time.sleep(100)
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

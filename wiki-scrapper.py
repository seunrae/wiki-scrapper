from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

PATH = "python-scraper/chromedriver"

service = Service(executable_path=PATH)

driver = webdriver.Chrome(service=service)


driver.get("https://www.wikipedia.org/")

search_input = driver.find_element(By.ID, "searchInput")

search_input.send_keys("Special:Random", Keys.ENTER)

time.sleep(3)

title = driver.find_element(By.ID, "firstHeading").text

content = driver.find_element(By.ID, "bodyContent").text

print("Title: ", title,)
print("Content: ", content[:500],"...")

driver.quit()




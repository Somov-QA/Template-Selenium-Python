from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="../webdriver/chromedriver.exe")

driver.get("https://www.google.com/")

search = driver.find_element_by_name("q")
search.send_keys("GeForce 1650")
search.send_keys(Keys.ENTER)

time.sleep(5)

driver.close()
driver.quit()
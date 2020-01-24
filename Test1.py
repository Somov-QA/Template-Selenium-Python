from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\GIT\Template-Selenium-Python\webdriver\chromedriver.exe")

driver.get("https://www.google.com/")

search = driver.find_element_by_name("q")
search.send_keys("GeForce 1650")
search.send_keys(Keys.ENTER)

driver.close()
driver.quit()
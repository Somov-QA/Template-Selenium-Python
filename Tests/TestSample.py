from selenium import webdriver
from Support.PageObjects.GooglePage import GooglePage
from Support.StepObjects.GoogleSteps import GoogleSteps

driver = webdriver.Chrome(executable_path="../webdriver/chromedriver.exe")
driver.get("https://www.google.com/")

tester = GoogleSteps(driver)
tester.setValueInSearch("GeForce 1650")
result = tester.getCountResultSearch()

print("Count: ", result)
assert result != 0
print("Tests finished: SUCCESS")

driver.close()
driver.quit()

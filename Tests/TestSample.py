from selenium import webdriver
from Support.PageObjects.GooglePage import GooglePage
from Support.StepObjects.GoogleSteps import GoogleSteps

driver = webdriver.Chrome(executable_path="../webdriver/chromedriver.exe")
driver.get("https://www.google.com/")

tester = GoogleSteps(driver)
tester.setValueInSearch("GeForce 1650", GooglePage.inputSearchName)
result = tester.getCountResultSearch(GooglePage.searchResultsClass)
print(result)

driver.close()
driver.quit()

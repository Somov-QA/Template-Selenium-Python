from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class GoogleSteps:
    driver = 0

    def __init__(self, webdriver):
        self.driver = webdriver

    def setValueInSearch(self, value, nameField):
        searchField = self.driver.find_element_by_name(nameField)
        searchField.send_keys(value)
        searchField.send_keys(Keys.ENTER)

    def getCountResultSearch(self, classResults):
        resultElements = self.driver.find_elements_by_class_name(classResults)
        return len(resultElements)
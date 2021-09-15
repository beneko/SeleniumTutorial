from selenium.webdriver.common.by import By


class HandyWrappers:

    def __init__(self, driver):
        self.driver = driver

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "class_name":
            return By.CLASS_NAME
        elif locator_type == "link_text":
            return By.LINK_TEXT
        elif locator_type == "partial_link_text":
            return By.PARTIAL_LINK_TEXT
        else:
            print("Locator type " + locator_type + " not correct/supported")
        return False

    def get_element(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            print("Element Found")
        except:
            print("Element not found")
        return element

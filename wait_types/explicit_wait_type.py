from traceback import print_stack
from userdefinedmethods.handywrappers import HandyWrappers
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class ExplicitWaitType:

    def __init__(self, driver):
        self.driver = driver
        self.hw = HandyWrappers(driver)

    def wait_for_element(self, locator, locator_type="id",
                       timeout=10, poll_frequency=0.5):
        element = None
        try:
            by_type = self.hw.get_by_type(locator_type)
            print("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((by_type, locator)))
            print("Element appeared on the web page")
        except:
            print("Element not appeared on the web page")
            print_stack()
        return element
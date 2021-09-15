from selenium import webdriver
from userdefinedmethods.handywrappers import HandyWrappers
import time


class UsingWrappers:

    def __init__(self):
        base_url = "https://courses.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw = HandyWrappers(driver)
        driver.get(base_url)

        text_field1 = hw.get_element("name")
        text_field1.send_keys("Test")
        time.sleep(2)
        text_field2 = hw.get_element("//input[@id='name']", "xpath")
        text_field2.clear()


ff = UsingWrappers()


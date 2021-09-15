from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SwitchToFrame:

    def __init__(self):
        base_url = "https://courses.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.execute_script("window.scrollBy(0, 1000);")

        # Switch to frame using Id
        driver.switch_to.frame("courses-iframe")

        # Switch to frame using name
        # driver.switch_to.frame("iframe-name")

        # Switch to frame using numbers
        # driver.switch_to.frame(0)

        time.sleep(2)
        # Search course
        search_box = driver.find_element(By.XPATH, "//input[@id='search']")
        search_box.send_keys("python")
        time.sleep(2)

        # Switch back to the parent frame
        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0, -1000);")
        time.sleep(2)
        driver.find_element(By.ID, "name").send_keys("Test Successful")


ff = SwitchToFrame()

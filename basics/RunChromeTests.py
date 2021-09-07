from selenium import webdriver
import os


class RunChromeTests:

    def test(self):

        driver_location = "chromedriver location"
        os.environ["webdriver.chrome.driver"] = driver_location
        # Initiate the driver instance
        driver = webdriver.Chrome(driver_location)
        # open the url in Chrome
        driver.get("https://www.letskodeit.com")


chromeTest = RunChromeTests()
chromeTest.test()

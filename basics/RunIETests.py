from selenium import webdriver
import os


class RunIETests:

    def test(self):

        driver_location = "C:\\Users\\behza\\PycharmProjects\\libs\\IEDriverServer.exe"
        os.environ["webdriver.ie.driver"] = driver_location
        # Initiate the driver instance
        driver = webdriver.Ie(driver_location)
        # open the url in Internet Explorer
        driver.get("https://www.letskodeit.com")


ieTest = RunIETests()
ieTest.test()

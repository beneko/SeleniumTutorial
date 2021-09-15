from selenium import webdriver
from selenium.webdriver.common.by import By
from explicit_wait_type import ExplicitWaitType


class ExplicitWaitDemo2:

    def __init__(self):
        base_url = "https://www.expedia.com"
        driver = webdriver.Firefox()
        driver.implicitly_wait(.5)
        driver.maximize_window()
        wait = ExplicitWaitType(driver)
        driver.get(base_url)

        driver.find_element(By.XPATH, "//*[@id='wizardMainRegionV2']/div/div/div[2]/div/div/ul/li[2]/a/span").click()

        driver.find_element(By.XPATH, "//*[@id='location-field-leg1-origin-menu']/div[1]/button").click()
        driver.find_element(By.XPATH, "//*[@id='location-field-leg1-origin']").send_keys("San Francisco")

        element_1 = wait.wait_for_element("//*[@id='location-field-leg1-origin-menu']/div[2]/ul/li[1]/button", "xpath")
        element_1.click()

        driver.find_element(By.XPATH, "//*[@id='location-field-leg1-destination-menu']/div[1]/button").click()
        driver.find_element(By.XPATH, "//*[@id='location-field-leg1-destination']").send_keys("New York")

        element_2 = wait.wait_for_element("//*[@id='location-field-leg1-destination-menu']/div[2]/ul/li[1]/button", "xpath")
        element_2.click()

        driver.find_element(By.XPATH, "//*[@id='wizard-flight-pwa-1']/div[3]/div[2]/button").click()


ff = ExplicitWaitDemo2()



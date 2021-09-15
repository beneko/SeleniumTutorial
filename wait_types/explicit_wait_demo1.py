from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class ExplicitWaitDemo1:

    def __init__(self):
        base_url = "https://www.expedia.com"
        driver = webdriver.Firefox()
        driver.implicitly_wait(.5)
        driver.maximize_window()
        driver.get(base_url)

        driver.find_element(By.XPATH, "//*[@id='wizardMainRegionV2']/div/div/div[2]/div/div/ul/li[2]/a/span").click()

        driver.find_element(By.XPATH, "//*[@id='location-field-leg1-origin-menu']/div[1]/button").click()
        driver.find_element(By.XPATH, "//*[@id='location-field-leg1-origin']").send_keys("San Francisco")
        wait_1 = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element_1 = wait_1.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='location-field-leg1-origin-menu']/div[2]/ul/li[1]/button")))
        element_1.click()

        driver.find_element(By.XPATH, "//*[@id='location-field-leg1-destination-menu']/div[1]/button").click()
        driver.find_element(By.XPATH, "//*[@id='location-field-leg1-destination']").send_keys("New York")
        wait_2 = WebDriverWait(driver, 10, poll_frequency=1,
                               ignored_exceptions=[NoSuchElementException,
                                                   ElementNotVisibleException,
                                                   ElementNotSelectableException])
        element_2 = wait_2.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='location-field-leg1-destination-menu']/div[2]/ul/li[1]/button")))
        element_2.click()

        driver.find_element(By.XPATH, "//*[@id='wizard-flight-pwa-1']/div[3]/div[2]/button").click()


ff = ExplicitWaitDemo1()


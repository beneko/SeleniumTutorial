from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def click_and_send_keys():
    base_url = "https://letskodeit.teachable.com"
    driver = webdriver.Firefox()

    driver.maximize_window()

    driver.get(base_url)

    # make a pause of 10 seconds to load the next url
    driver.implicitly_wait(10)

    login_link = driver.find_element(By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']")

    # click on the link
    login_link.click()

    email_field = driver.find_element(By.ID, "user_email")

    # fill the field
    email_field.send_keys("test")

    password_field = driver.find_element(By.ID, "user_password")
    password_field.send_keys("test")

    time.sleep(3)

    # clear the field
    email_field.clear()

    time.sleep(3)

    email_field.send_keys("test")


click_and_send_keys()

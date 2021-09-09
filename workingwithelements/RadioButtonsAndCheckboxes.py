from selenium import webdriver
import time


class RadioButtonsAndCheckboxes:

    def __init__(self):
        base_url = "https://courses.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(10)

        bmw_radio_btn = driver.find_element_by_id("bmwradio")
        bmw_radio_btn.click()

        time.sleep(2)
        benz_radio_btn = driver.find_element_by_id("benzradio")
        benz_radio_btn.click()

        time.sleep(2)
        bmw_checkbox = driver.find_element_by_id("bmwcheck")
        bmw_checkbox.click()

        time.sleep(2)
        benz_checkbox = driver.find_element_by_id("benzcheck")
        benz_checkbox.click()

        print("BMW Radio button is selected? " + str(bmw_radio_btn.is_selected()))
        print("Benz Radio button is selected? " + str(benz_radio_btn.is_selected()))
        print("BMW Checkbox is selected? " + str(bmw_checkbox.is_selected()))
        print("Benz Checkbox is selected? " + str(benz_checkbox.is_selected()))


ff = RadioButtonsAndCheckboxes()

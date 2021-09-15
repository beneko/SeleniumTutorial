from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SwitchToWindow:

    def __init__(self):
        base_url = "https://courses.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)

        # Find parent handle -> Main Window
        parent_handle = driver.current_window_handle
        print("Parent Handle: " + parent_handle)

        # Find open window button and click it
        driver.find_element(By.ID, "openwindow").click()
        time.sleep(2)

        # Find all handles, there should two handles after clicking open window button
        handles = driver.window_handles

        # Switch to window and search course
        for handle in handles:
            print("Handle: " + handle)
            if handle not in parent_handle:
                driver.switch_to.window(handle)
                print("Switched to window:: " + handle)
                search_box = driver.find_element(By.XPATH, "//input[@id='search']")
                search_box.send_keys("python")
                time.sleep(2)
                driver.close()
                break

        # Switch back to the parent handle
        driver.switch_to.window(parent_handle)
        time.sleep(2)
        driver.find_element(By.ID, "name").send_keys("Test Successful")


ff = SwitchToWindow()

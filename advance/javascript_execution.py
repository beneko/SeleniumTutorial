from selenium import webdriver
import time


class JavaScriptExecution:

    def __init__(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.execute_script("window.location = 'https://courses.letskodeit.com/practice';")
        driver.implicitly_wait(3)
        time.sleep(6)

        element = driver.execute_script("return document.getElementById('name');")
        element.send_keys("Test")


ff = JavaScriptExecution()

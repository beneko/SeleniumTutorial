from selenium import webdriver
import time


def test_lets_kode_it():
    base_url = "https://courses.letskodeit.com/practice"
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(base_url)
    driver.implicitly_wait(2)

    # Find the state of the text box
    text_box_element = driver.find_element_by_id("displayed-text")
    # True if visible, False if hidden
    text_box_state = text_box_element.is_displayed()
    # Exception if not present in the DOM
    print("Text is visible? " + str(text_box_state))
    time.sleep(2)

    # Click the Hide button
    driver.find_element_by_id("hide-textbox").click()
    # Find the state of the text box
    text_box_state = text_box_element.is_displayed()
    print("Text is visible? " + str(text_box_state))
    time.sleep(2)

    # Click the Show button
    driver.find_element_by_id("show-textbox").click()
    # Find the state of the text box
    text_box_state = text_box_element.is_displayed()
    print("Text is visible? " + str(text_box_state))
    time.sleep(2)
    # Browser Close
    driver.quit()


test_lets_kode_it()

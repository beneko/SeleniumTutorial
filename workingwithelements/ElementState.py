from selenium import webdriver


def is_enabled():
    base_url = "https://www.google.com"
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(base_url)
    driver.implicitly_wait(3)

    e1 = driver.find_element_by_id("gs_htif0")
    e1_state = e1.is_enabled() # True for enabled and False for disabled
    print("E1 is Enabled? -> " + str(e1_state))

    e2 = driver.find_element_by_id("gs_taif0")
    e2_state = e2.is_enabled()  # True for enabled and False for disabled
    print("E2 is Enabled? -> " + str(e2_state))

    e3 = driver.find_element_by_id("lst-ib")
    e3_state = e3.is_enabled()  # True for enabled and False for disabled
    print("E3 is Enabled? -> " + str(e3_state))

    e3.send_keys("letskodeit")


is_enabled()

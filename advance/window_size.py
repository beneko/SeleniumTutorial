from selenium import webdriver


class WindowSize:

    def __init__(self):
        driver = webdriver.Firefox()
        # driver.maximize_window()
        driver.get("https://courses.letskodeit.com/practice")
        driver.implicitly_wait(3)

        height = driver.execute_script("return window.innerHeight;")
        width = driver.execute_script("return window.innerWidth;")
        print("Height: " + str(height))
        print("Width: " + str(width))
        driver.quit()


ff = WindowSize()


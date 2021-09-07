from selenium import webdriver


class RunFirefoxTests:

    def test(self):
        # Initiate the driver instance
        driver = webdriver.Firefox(executable_path="C:\\Users\\behza\\PycharmProjects\\libs\\geckodriver.exe")

        # open the url in firefox
        driver.get("https://www.letskodeit.com")


firefox = RunFirefoxTests()
firefox.test()

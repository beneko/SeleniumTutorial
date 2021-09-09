from selenium import webdriver


class BrowserInteractions:

    def __init__(self):
        self.base_url = "https://courses.letskodeit.com/practice"
        self.driver = webdriver.Firefox()
        self.driver.get(self.base_url)

        # Window Maximize
        self.driver.maximize_window()

        # Open the Url
        self.driver.get(self.base_url)
        # Get Title
        title = self.driver.title
        print("Title of the web page is: " + title)

        # Get Current Url
        current_url = self.driver.current_url
        print("Current Url of the web page is: " + current_url)

        # Browser Refresh
        self.driver.refresh()
        print("Browser Refreshed 1st time")

        self.driver.get(self.driver.current_url)
        print("Browser Refreshed 2nd time")

        # Open another Url
        self.driver.get("https://sso.teachable.com/secure/42299/users/sign_in?reset_purchase_session=1")
        current_url = self.driver.current_url
        print("Current Url of the web page is: " + current_url)

        # Browser Back
        self.driver.back()
        print("Go one step back in browser history")
        current_url = self.driver.current_url
        print("Current Url of the web page is: " + current_url)

        # Browser Forward
        self.driver.forward()
        print("Go one step forward in browser history")
        current_url = self.driver.current_url
        print("Current Url of the web page is: " + current_url)
        # Get Page Source
        page_source = self.driver.page_source
        print(page_source)

        # Browser Close / Quit
        # driver.close()
        self.driver.quit()


ff = BrowserInteractions()

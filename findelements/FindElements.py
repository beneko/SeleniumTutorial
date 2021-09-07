from selenium import webdriver
from selenium.webdriver.common.by import By

class FindElements:
    def __init__(self):
        self.base_url = "https://courses.letskodeit.com/practice"
        self.driver = webdriver.Firefox()
        self.driver.get(self.base_url)

    def find_element_by_id(self, id):

        element_by_id = self.driver.find_element_by_id(id)
        if element_by_id is not None:
            print("We found an element by id: {} ".format(id))

    def find_element_by_name(self, name):

        element_by_name = self.driver.find_element_by_name(name)
        if element_by_name is not None:
            print("We found an element by name: {} ".format(name))

    def find_element_by_xpath(self, xpath):

        element_by_xpath = self.driver.find_element_by_xpath(xpath)
        if element_by_xpath is not None:
            print("We found an element by xpath: {} ".format(xpath))

    def find_element_by_css(self, css):

        element_by_css = self.driver.find_element_by_css_selector(css)
        if element_by_css is not None:
            print("We found an element by css selector: {} ".format(css))

    def find_element_by_link_text(self, link):

        element_by_link = self.driver.find_element_by_link_text(link)
        if element_by_link is not None:
            print("We found an element by link text: {} ".format(link))

    def find_element_by_partial_link_text(self, link):
        element_by_partial_link = self.driver.find_element_by_partial_link_text(link)
        if element_by_partial_link is not None:
            print("We found an element by partial link text: {} ".format(link))

    def find_element_by_class_name(self, class_name):
        element_by_class_name = self.driver.find_element_by_class_name(class_name)
        if element_by_class_name is not None:
            print("We found an element by class name: {} ".format(class_name))

    def find_element_by_tag_name(self, tag_name):
        element_by_tag_name = self.driver.find_element_by_tag_name(tag_name)
        text = element_by_tag_name.text
        if element_by_tag_name is not None:
            print("We found an element by tag name: {} and the text inside of this tag is: {}".format(tag_name, text))

    def find_element(self, by , value):
        element = self.driver.find_element(by, value)
        if element is not None:
            print("We found an element by {} de {}".format(by, value))

    def find_elements(self, by, value):
        elements = self.driver.find_elements(by, value)
        if elements is not None:
            print("We found {} element(s) by {} of {}".format(len(elements), by, value))


firefox = FindElements()

firefox.find_element_by_id("name")
firefox.find_element_by_name("show-hide")
firefox.find_element_by_xpath("/html//input[@id='name']")
firefox.find_element_by_css("#displayed-text")
firefox.find_element_by_link_text("SIGN IN")
firefox.find_element_by_partial_link_text("ALL")
firefox.find_element_by_class_name("displayed-class")
firefox.find_element_by_tag_name("h1")

firefox.find_element(By.ID, "name")
firefox.find_element(By.NAME, "show-hide")
firefox.find_element(By.XPATH, "/html//input[@id='name']")
firefox.find_element(By.CSS_SELECTOR, "#displayed-text")
firefox.find_element(By.LINK_TEXT, "SIGN IN")
firefox.find_element(By.PARTIAL_LINK_TEXT, "ALL")
firefox.find_element(By.CLASS_NAME, "displayed-class")
firefox.find_element(By.TAG_NAME, "h1")


firefox.find_elements(By.ID, "name")
firefox.find_elements(By.NAME, "show-hide")
firefox.find_elements(By.XPATH, "/html//input[@id='name']")
firefox.find_elements(By.CSS_SELECTOR, "#displayed-text")
firefox.find_elements(By.LINK_TEXT, "SIGN IN")
firefox.find_elements(By.PARTIAL_LINK_TEXT, "ALL")
firefox.find_elements(By.CLASS_NAME, "displayed-class")
firefox.find_elements(By.TAG_NAME, "h1")
firefox.find_elements(By.TAG_NAME, "input")


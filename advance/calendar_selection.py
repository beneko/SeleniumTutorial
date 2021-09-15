from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class CalendarSelection:

    def test1(self):
        base_url = "https://www.expedia.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        # Click flights tab
        driver.find_element_by_xpath("//span[@class='uitk-tab-text'][contains(text(),'Flights')]").click()
        # Find departing field
        departing_field = driver.find_element_by_xpath("//button[@data-name='d1']")
        # Click departing field
        departing_field.click()
        # Find the date to be selected
        date_to_select = driver.find_element(By.XPATH, "//table[@class='uitk-date-picker-weeks'][1]//button[@data-day=30]")
        # Click the date
        date_to_select.click()
        # click button done
        driver.find_element(By.XPATH, "//button[@data-stid='apply-date-picker']").click()

    def test2(self):
        base_url = "https://www.expedia.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        # Click flights tab
        driver.find_element_by_xpath("//span[@class='uitk-tab-text'][contains(.,'Flights')]").click()
        # Click departing field
        driver.find_element_by_xpath("//button[@data-name='d1']").click()
        # find whole month
        cal_month = driver.find_element(By.XPATH, "//table[@class='uitk-date-picker-weeks'][1]/tbody")
        # take whole month a list
        all_valid_dates_btn = cal_month.find_elements(By.TAG_NAME, "button")

        time.sleep(2)
        # find a day in list
        for date in all_valid_dates_btn:
            if date.get_attribute("data-day") == "30":
                date.click()
                break

        # click button done
        driver.find_element(By.XPATH, "//button[@data-stid='apply-date-picker']").click()


ff = CalendarSelection()
# ff.test1()
ff.test2()

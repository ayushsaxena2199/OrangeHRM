from data.reading_excel import logout_locators
from _library.Selenium_Wrapper import SeleniumWrapper
from POM.login import Login
import time

locator = logout_locators()


class Logout(Login):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.selenium_wrapper = SeleniumWrapper(self.driver)

    def clk_on_dashboard(self):
        self.selenium_wrapper.wait_till_ele_is_visible(locator['MyProfile_btn'])
        self.selenium_wrapper.clk_on_ele(locator['MyProfile_btn'])

    def clk_on_logout(self):
        self.selenium_wrapper.wait_till_ele_is_visible(locator['logout_btn'])
        self.selenium_wrapper.clk_on_ele(locator['logout_btn'])
        time.sleep(3)





import time
from data.reading_excel import login_details
from _library.Selenium_Wrapper import SeleniumWrapper

locator = login_details()


class Login:
    def __init__(self, driver):
        self.driver = driver
        self.selenium_wrapper = SeleniumWrapper(self.driver)

    def enter_email(self, username):
        self.selenium_wrapper.enter_keys(locator['email'], username)

    def enter_pwd(self, pwd):
        self.selenium_wrapper.enter_keys(locator['pwd'], pwd)

    def clk_login(self):
        self.selenium_wrapper.clk_on_ele(locator['submit btn'])
        time.sleep(2)

    def login_successful(self):
        self.selenium_wrapper.wait_till_ele_is_visible(locator['dashboard_visible'])
        self.selenium_wrapper.ele_is_displayed(locator['dashboard_visible'])





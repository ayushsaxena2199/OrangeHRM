import time
from data.reading_excel import info_locator
from POM.login import Login
from _library.Selenium_Wrapper import SeleniumWrapper

locator = info_locator()


class MyInfo(Login):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.selenium_wrapper = SeleniumWrapper(self.driver)

    def clk_on_myinfo(self):
        self.selenium_wrapper.clk_on_ele(locator['myinfo_btn'])
        time.sleep(2)

    def enter_fst_name(self, fstname):
        self.selenium_wrapper.clr_textfield(locator['frst_nme'])
        time.sleep(1)
        self.selenium_wrapper.enter_keys(locator['frst_nme'], fstname)
        time.sleep(2)

    def enter_last_name(self, lstname):
        self.selenium_wrapper.clk_on_ele(locator['lst_nme'])
        self.selenium_wrapper.clr_textfield(locator['lst_nme'])
        time.sleep(1)
        self.selenium_wrapper.enter_keys(locator['lst_nme'], lstname)
        time.sleep(2)

    def clk_on_submit(self):
        self.selenium_wrapper.clk_on_ele(locator['submit_btn'])
        time.sleep(2)






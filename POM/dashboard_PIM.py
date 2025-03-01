import time

from data.reading_excel import pim_locator
from POM.login import Login
from _library.Selenium_Wrapper import SeleniumWrapper

locator = pim_locator()


class PIMAddUser(Login):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.selenium_wrapper = SeleniumWrapper(self.driver)

    def clk_on_pim(self):
        self.selenium_wrapper.wait_till_ele_is_visible(locator['clk_on_pim'])
        self.selenium_wrapper.clk_on_ele(locator['clk_on_pim'])
        time.sleep(3)

    def clk_add_user(self):
        self.selenium_wrapper.wait_till_ele_is_visible(locator['clk_on_add_emp'])
        self.selenium_wrapper.clk_on_ele(locator['clk_on_add_emp'])

    def enter_fstname(self, firstname):
        self.selenium_wrapper.wait_till_ele_is_visible(locator['enter_fstname'])
        self.selenium_wrapper.enter_keys(locator['enter_fstname'], firstname)

    def enter_lstname(self, lastname):
        self.selenium_wrapper.wait_till_ele_is_visible(locator['enter_lstname'])
        self.selenium_wrapper.enter_keys(locator['enter_lstname'], lastname)

    def enter_emp_id(self, emp_id):

        self.selenium_wrapper.wait_till_ele_is_visible(locator['enter_empId'])
        self.selenium_wrapper.clr_textfield(locator['enter_empId'])

        self.selenium_wrapper.wait_till_ele_is_visible(locator['enter_empId'])
        self.selenium_wrapper.enter_keys(locator['enter_empId'], emp_id)

    def enter_img_path(self, img_path):

        self.selenium_wrapper.wait_till_ele_is_visible(locator['clk_add_profile'])
        self.selenium_wrapper.enter_keys(locator['clk_add_profile'], img_path)

    def clk_save(self):

        self.selenium_wrapper.wait_till_ele_is_visible(locator['save_btn'])
        self.selenium_wrapper.clk_on_ele(locator['save_btn'])
        time.sleep(8)





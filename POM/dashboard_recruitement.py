from _library.Selenium_Wrapper import SeleniumWrapper
from POM.login import Login
from data.reading_excel import recruit_locator

locator = recruit_locator()


class RecruitementAddCandidate(Login):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.selenium_wrapper = SeleniumWrapper(self.driver)

    def add_candidate(self):
        self.selenium_wrapper.wait_till_ele_is_visible(locator['recruitment_btn'])
        self.selenium_wrapper.clk_on_ele(locator['recruitment_btn'])

        self.selenium_wrapper.wait_till_ele_is_visible(locator['add_cand'])
        self.selenium_wrapper.clk_on_ele(locator['add_cand'])





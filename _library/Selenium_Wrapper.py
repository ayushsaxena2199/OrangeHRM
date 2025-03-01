from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class SeleniumWrapper:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def clk_on_ele(self, logical_name):
        self.driver.find_element(*logical_name).click()

    def enter_keys(self, logical_name, data):
        self.driver.find_element(*logical_name).send_keys(data)

    def scroll_to_ele(self, logical_name):
        ele = self.driver.find_element(*logical_name)
        action_chn_obj = ActionChains(self.driver)
        action_chn_obj.scroll_to_element(ele).perform()

    def ele_is_displayed(self, logical_name):
        self.driver.find_element(*logical_name).is_displayed()

    def wait_till_ele_is_visible(self, logical_name):
        ele = self.driver.find_element(*logical_name)
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.visibility_of(ele))

    def clr_textfield(self, logical_name):
        self.driver.find_element(*logical_name).clear()


    def pop_up(self):
        alert_obj = self.driver.switch_to.alert
        alert_obj.accept()
        alert_obj.dismiss()




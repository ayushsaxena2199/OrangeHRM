import time
from POM.dashboard_myinfo import MyInfo


def test_myinfo(_driver):
    info = MyInfo(_driver)
    info.enter_email('Admin')
    info.enter_pwd('admin123')
    info.clk_login()
    time.sleep(2)
    info.clk_on_myinfo()
    info.enter_fst_name('Ayush')
    info.enter_last_name('Saxena')
    info.clk_on_submit()


import time

from POM.dashboard_PIM import PIMAddUser


def test_add_user(_driver):
    pim = PIMAddUser(_driver)
    pim.enter_email('Admin')
    pim.enter_pwd('admin123')
    pim.clk_login()
    path = r'C:\Users\ASUS\Downloads\demopic.jpg'
    time.sleep(3)
    pim.clk_on_pim()
    time.sleep(3)
    pim.clk_add_user()
    pim.enter_fstname('Ayush')
    pim.enter_lstname('Saxena')
    pim.enter_emp_id('20349')
    pim.enter_img_path(path)
    time.sleep(8)
    pim.clk_save()



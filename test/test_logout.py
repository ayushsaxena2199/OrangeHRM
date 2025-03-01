from POM.logout import Logout


def test_logout(_driver):
    logout = Logout(_driver)
    logout.enter_email('Admin')
    logout.enter_pwd('admin123')
    logout.clk_login()
    logout.clk_on_dashboard()
    logout.clk_on_logout()


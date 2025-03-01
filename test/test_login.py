import pytest
from POM.login import Login


@pytest.mark.parametrize("username,pwd", [('Admin', 'admin123'), ('Admin', 'admin123')])
def test_login(_driver, username, pwd):
    login = Login(_driver)
    login.enter_email(username)
    login.enter_pwd(pwd)
    login.clk_login()
    login.login_successful()

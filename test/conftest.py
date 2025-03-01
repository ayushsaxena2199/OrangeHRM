import pytest
from selenium import webdriver
import time

opts = webdriver.ChromeOptions()
opts.add_argument('--disable-notifications')
opts.add_experimental_option('detach', True)


@pytest.fixture()
def _driver():
    driver = webdriver.Chrome(options=opts)
    driver.maximize_window()
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    time.sleep(1)
    yield driver
    driver.quit()

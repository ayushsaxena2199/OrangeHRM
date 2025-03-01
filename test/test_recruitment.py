import time
from POM.dashboard_recruitement import RecruitementAddCandidate


def test_recruitment(_driver):
    recruit = RecruitementAddCandidate(_driver)
    recruit.enter_email('Admin')
    recruit.enter_pwd('admin123')
    recruit.clk_login()
    recruit.add_candidate()
    time.sleep(3)


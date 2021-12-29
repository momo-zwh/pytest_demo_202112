from time import sleep

from base.base_driver import init_driver, find_toast
from page.page import Page


class TestBack:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        sleep (3)
        self.driver.quit ()

    def test_back(self):
        self.page.save_maillist.press_back()
        print(find_toast(self.driver, "退出"))

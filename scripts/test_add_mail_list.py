from time import sleep
import yaml
import pytest
from appium import webdriver

from base.base_analyze import analyze_file
from page.page import Page



class TestAddmailist:

    def setup(self):
        desired_caps = dict ()
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '192.168.56.102:5555'
        desired_caps['appPackage'] = 'com.android.contacts'
        desired_caps['appActivity'] = '.activities.PeopleActivity'
        # 不重置应用
        desired_caps['noReset'] = True

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        self.page = Page(self.driver)


    def teardown(self):
        sleep(3)
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_file("contact_data.yaml", "test_add_contact"))
    def test_add_contact(self, args):
        name = args["name"]
        phone = args["phone"]

        self.page.contacts().click_newly_build_button()

        # self.page.add_number().click_local_save()

        self.page.add_number().send_send_name(name)

        self.page.add_number().send_send_phone(phone)

        # 点击返回按钮
        self.page.add_number().press_back()

        # 断言
        assert name == self.page.save_maillist.get_name_title()

    #
    # @pytest.mark.parametrize("args", analyze_file("test_add_contact1"))
    # def test_add_contact1(self, args):
    #     name = args["name"]
    #     phone = args["phone"]
    #
    #     self.page.contacts().click_newly_build_button()
    #
    #     # self.page.add_number().click_local_save()
    #
    #     self.page.add_number().send_send_name(name)
    #
    #     self.page.add_number().send_send_phone(phone)





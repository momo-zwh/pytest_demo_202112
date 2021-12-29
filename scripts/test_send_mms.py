from time import sleep

import pytest
import yaml

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


# data_key是要解析的yaml文件中字典的一级key
# def analyze_file(data_key):
#     with open("./data/TestSendMms.yaml", "r") as f:
#         data = yaml.load(f, Loader=yaml.FullLoader)
#         dict_data = data[data_key]
#         list_data = list()
#         for i in dict_data.values():
#             list_data.append(i)
#         return list_data


class TestSendMms:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        sleep(3)
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_file("TestSendMms.yaml", "TestSendMms1"))
    def test_send_mms(self, args):
        phone = args["phone"]
        text = args["text"]
        assert 1
        # 点击新建短信按钮
        # self.page.mms_home.click_newmessage()
        # # 输入接收人
        # self.page.send_mms.input_receiver(phone)
        # # 输入信息内容
        # self.page.send_mms.input_send_mms(text)
        # # 点击发送
        # self.page.send_mms.click_sending_button()

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    def test_send1(self):
        assert 1
        # try:
        #     assert 0
        # except AssertionError:
        #     pass

    def test_send2(self):
        assert 0

    def test_send3(self):
        assert 1

    def test_send4(self):
        assert 1

    def test_send5(self):
        assert 1


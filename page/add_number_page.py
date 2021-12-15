from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AddNumber(BaseAction):

    # 点击本地保存
    local_save = By.XPATH, "//*[@text='本地保存']"
    # 输入姓名
    send_name = By.XPATH, "//*[@text='姓名']"
    # 输入电话
    send_phone = By.XPATH, "//*[@text='电话']"

    def click_local_save(self):
        self.click(self.local_save)

    def send_send_name(self, content):
        self.input(self.send_name, content)

    def send_send_phone(self, content):
        self.input(self.send_phone, content)

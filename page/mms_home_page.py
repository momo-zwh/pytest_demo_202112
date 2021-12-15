from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MmsHomepage(BaseAction):

    # 新建短信按钮
    newmessage_button = By.XPATH, "//*[@text='新信息']"

    def click_newmessage(self):
        self.click(self.newmessage_button)

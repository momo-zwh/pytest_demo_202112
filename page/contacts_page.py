from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class Contacts(BaseAction):

    # 点击新建联系人
    newly_build_button = By.ID, "com.android.contacts:id/floating_action_button"

    def click_newly_build_button(self):
        self.click(self.newly_build_button)

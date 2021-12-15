from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SaveMaillist(BaseAction):

    # 联系人保存成功后的标题
    name = By.ID, "com.android.contacts:id/large_title"

    # 获取标题中的内容
    def get_name_title(self):
        return self.find_element(self.name).text

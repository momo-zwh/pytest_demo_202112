import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SendMms(BaseAction):
    # 接受者
    receiver = By.ID, "com.android.mms:id/recipients_editor"
    # 输入信息
    send_mms = By.ID, "com.android.mms:id/embedded_text_editor"
    # 发送按钮
    sending_button = By.ID, "com.android.mms:id/send_button_sms"
    @allure.step(title="输入接收者")  # 用allure添加用例标题
    def input_receiver(self, content):  # content是需要脚本中的输入的信息
        allure.attach("输入接收者:", str(content), allure.attach_type.TEXT)  # 添加类型为TEXT时,可以不写allure.attach_type.TEXT
        self.input(self.receiver, content)

    @allure.step(title="输入消息")
    def input_send_mms(self, content):
        allure.attach("输入消息", content, allure.attach_type.TEXT)  # 用allure添加用例描述
        self.input(self.send_mms, content)

    @allure.step (title="点击发送按钮")
    def click_sending_button(self):
        self.click(self.sending_button)
        allure.attach("截图", self.driver.get_screenshot_as_png(), allure.attach_type.PNG)  # 用allure添加截图



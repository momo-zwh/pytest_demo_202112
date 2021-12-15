from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=10, poll=0.5):
        """
        根据特征,找元素
        :param feature:特征
        :param timeout:超时时间
        :param poll:查找频率
        :return:元素
        """
        """
        feature代表传入的参数,
        by和value:by代表查找元素的方式例如ID或者xpath,value代表查找的元素的具体值ID或则XPath;
        :param feature:
        :return: 然后把查找方式和具体值放入框架中的find方法中作为一个新的find方法封装起来
        """
        by, value = feature
        # element = self.driver.find_element(by, value)
        element = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(by, value))
        return element

    def find_elements(self, feature, timeout=10, poll=0.5):
        by, value = feature

        # element = self.driver.find_element(by, value)
        element = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(by, value))
        return element

    def click(self, feature, timeout=10, poll=0.5):
        self.find_element(feature, timeout, poll).click()

    def input(self, feature, content, timeout=10, poll=0.5):
        self.find_element(feature, timeout, poll).send_keys(content)

    def clear(self, feature, timeout=10, poll=0.5):
        self.find_element(feature, timeout, poll).clear()

    def press_back(self):  # 点击安卓系统返回键
        self.driver.press_keycode(4)

    def press_enter(self):
        self.driver.press_keycode(66)


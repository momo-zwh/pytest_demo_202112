from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def init_driver():
    desired_caps = dict()
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.56.102:5555'
    # app信息
    # desired_caps['appPackage'] = 'com.android.mms'
    # desired_caps['appActivity'] = '.ui.ConversationList'
    desired_caps['appPackage'] = 'com.cyanogenmod.filemanager'
    desired_caps['appActivity'] = '.activities.NavigationActivity'

    # 不重置应用
    desired_caps['noReset'] = True
    # 使用 Uiautomator2 框架
    desired_caps['automationName'] = 'Uiautomator2'

    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


def find_toast(driver, message, timeout=3):
    """
    # message: 预期要获取的toast的部分消息
    """
    message = "//*[contains(@text,'" + message + "')]"  # 使用包含的方式定位

    element = WebDriverWait(driver, timeout, 0.1).until(lambda x: x.find_element(By.XPATH, message))
    return element.text



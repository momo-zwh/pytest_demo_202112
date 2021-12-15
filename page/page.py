from page.add_number_page import AddNumber
from page.contacts_page import Contacts
from page.mms_home_page import MmsHomepage
from page.save_maillist_page import SaveMaillist
from page.send_mms_page import SendMms


class Page:

    def __init__(self, driver):
        self.driver = driver
    @property
    def mms_home(self):
        return MmsHomepage(self.driver)
    @property
    def send_mms(self):
        return SendMms(self.driver)

    def contacts(self):
        return Contacts(self.driver)

    def add_number(self):
        return AddNumber(self.driver)
    @property
    def save_maillist(self):
        return SaveMaillist(self.driver)
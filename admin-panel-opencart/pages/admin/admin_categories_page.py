from selenium.webdriver.common.by import By

from ..base_page import BasePage

class AdminCategoriesPage(BasePage):
    CATEGORY_NAME_INPUT = (By.ID, "input-name1")
    META_TAG_INPUT = (By.ID, "input-meta-title1")
    SAVE_BUTTON = (By.XPATH, "//button[@data-original-title='Save']")

    def create_category(self, name):
        self.click(self.ADD_NEW_BUTTON)
        self.send_keys(self.CATEGORY_NAME_INPUT, name)
        self.send_keys(self.META_TAG_INPUT, name)
        self.click(self.SAVE_BUTTON)
        return self
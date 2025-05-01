from selenium.webdriver.common.by import By

from ..base_page import BasePage

class AdminProductsPage(BasePage):
    PRODUCT_NAME_INPUT = (By.ID, "input-name1")
    META_TAG_INPUT = (By.ID, "input-meta-title1")
    MODEL_INPUT = (By.ID, "input-model")
    PRICE_INPUT = (By.ID, "input-price")
    CATEGORY_SELECT = (By.ID, "input-category")
    SAVE_BUTTON = (By.XPATH, "//button[@data-original-title='Save']")
    FILTER_NAME_INPUT = (By.ID, "input-name")
    FILTER_BUTTON = (By.ID, "button-filter")
    SELECT_ALL_CHECKBOX = (By.XPATH, "//input[@type='checkbox'][@name='selected[]']")
    DELETE_BUTTON = (By.XPATH, "//button[@data-original-title='Delete']")

    def create_product(self, name, model, price, category, description="Good product"):
        self.click(self.ADD_NEW_BUTTON)
        self.send_keys(self.PRODUCT_NAME_INPUT, name)
        self.send_keys(self.META_TAG_INPUT, name)
        self.send_keys(self.MODEL_INPUT, model)
        self.send_keys(self.PRICE_INPUT, price)
        self.select_category(category)
        self.click(self.SAVE_BUTTON)
        return self

    def select_category(self, category_name):
        self.click(self.CATEGORY_SELECT)
        category_option = (By.XPATH, f"//option[contains(text(),'{category_name}')]")
        self.click(category_option)

    def filter_products(self, name):
        self.send_keys(self.FILTER_NAME_INPUT, name)
        self.click(self.FILTER_BUTTON)
        return self

    def delete_products_by_name(self, name):
        self.filter_products(name)
        self.click(self.SELECT_ALL_CHECKBOX)
        self.click(self.DELETE_BUTTON)
        self.driver.switch_to.alert.accept()
        return self
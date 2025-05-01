from selenium.webdriver.common.by import By

from .admin_categories_page import AdminCategoriesPage
from .admin_products_page import AdminProductsPage
from ..base_page import BasePage

class AdminDashboardPage(BasePage):
    CATALOG_MENU = (By.XPATH, "//a[contains(text(),'Catalog')]")
    CATEGORIES_MENU = (By.XPATH, "//a[contains(text(),'Categories')]")
    PRODUCTS_MENU = (By.XPATH, "//a[contains(text(),'Products')]")
    ADD_NEW_BUTTON = (By.XPATH, "//a[@data-original-title='Add New']")

    def open_categories(self):
        self.click(self.CATALOG_MENU)
        self.click(self.CATEGORIES_MENU)
        return AdminCategoriesPage(self.driver)

    def open_products(self):
        self.click(self.CATALOG_MENU)
        self.click(self.PRODUCTS_MENU)
        return AdminProductsPage(self.driver)
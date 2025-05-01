from selenium.webdriver.common.by import By

from .admin_dashboard_page import AdminDashboardPage
from ..base_page import BasePage

class AdminLoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "input-username")
    PASSWORD_INPUT = (By.ID, "input-password")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Login')]")

    def login(self, username, password):
        self.send_keys(self.USERNAME_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        return AdminDashboardPage(self.driver)
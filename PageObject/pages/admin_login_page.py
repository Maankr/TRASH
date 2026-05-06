from pages.base_page import BasePage
from locators.admin_login_locators import AdminLoginLocators


class AdminLoginPage(BasePage):

    def login(self, email, password):
        self.type(AdminLoginLocators.EMAIL, email)
        self.type(AdminLoginLocators.PASSWORD, password)
        self.click(AdminLoginLocators.SUBMIT)

    def is_logged_in(self):
        return self.is_visible(AdminLoginLocators.DASHBOARD)
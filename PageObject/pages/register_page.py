from pages.base_page import BasePage
from locators.register_locators import RegisterLocators


class RegisterPage(BasePage):

    def register(self, firstname, lastname, email, password):
        self.type(RegisterLocators.FIRSTNAME, firstname)
        self.type(RegisterLocators.LASTNAME, lastname)
        self.type(RegisterLocators.EMAIL, email)
        self.type(RegisterLocators.PASSWORD, password)
        self.click(RegisterLocators.SUBMIT)
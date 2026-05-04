from pages.base_page import BasePage
from locators.register_locators import RegisterLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class RegisterPage(BasePage):

    def register(self, firstname, lastname, email, password):

        self.type(RegisterLocators.FIRSTNAME, firstname)
        self.type(RegisterLocators.LASTNAME, lastname)
        self.type(RegisterLocators.EMAIL, email)
        self.type(RegisterLocators.PASSWORD, password)

        self.scroll_to_bottom_and_check_element(RegisterLocators.GDPR_CHECKBOX)

        # отмечаем чекбоксы обязательные при регистрации
        self._check_checkbox(RegisterLocators.GDPR_CHECKBOX)
        self._check_checkbox(RegisterLocators.CUSTOMER_PRIVACY_CHECKBOX)

        self.click(RegisterLocators.SUBMIT)

    def _check_checkbox(self, locator):
        label = self.wait.until(EC.element_to_be_clickable(locator))
        label.click()

    def is_registration_successful(self):
            self.wait.until(EC.visibility_of_element_located(RegisterLocators.USER_NAME))
            self.wait.until(EC.visibility_of_element_located(RegisterLocators.SIGN_OUT_BUTTON))

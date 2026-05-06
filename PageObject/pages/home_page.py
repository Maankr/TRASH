from pages.base_page import BasePage
from locators.home_locators import HomeLocators
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):

    def get_prices(self):
        return [p.text for p in self.finds(HomeLocators.PRICES)]

    def change_currency(self):
        self.click(HomeLocators.CURRENCY_BTN)
        currencies = self.finds(HomeLocators.CURRENCIES)
        self.wait.until(EC.element_to_be_clickable(currencies[1]))
        currencies[1].click()
        self.wait.until(EC.presence_of_element_located(HomeLocators.PRICES))
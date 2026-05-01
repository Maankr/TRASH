from selenium.webdriver.common.by import By


class HomeLocators:
    PRODUCTS = (By.CSS_SELECTOR, ".product-miniature")
    PRICES = (By.CSS_SELECTOR, ".price")

    CURRENCY_BTN = (By.CSS_SELECTOR, ".currency-selector button")
    CURRENCIES = (By.CSS_SELECTOR, ".currency-selector .dropdown-item")
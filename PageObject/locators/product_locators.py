from selenium.webdriver.common.by import By


class ProductLocators:
    ADD_TO_CART = (By.CSS_SELECTOR, "button.add-to-cart")
    CART = (By.CLASS_NAME, "cart-products-count")
from selenium.webdriver.common.by import By


class RegisterLocators:
    FIRSTNAME = (By.ID, "field-firstname")
    LASTNAME = (By.ID, "field-lastname")
    EMAIL = (By.ID, "field-email")
    PASSWORD = (By.ID, "field-password")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
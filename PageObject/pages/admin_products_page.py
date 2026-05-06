from pages.base_page import BasePage
from locators.admin_products_locators import AdminProductsLocators
from selenium.webdriver.support import expected_conditions as EC


class AdminProductsPage(BasePage):

    def open_products(self):
        self.click(AdminProductsLocators.CATALOG)
        self.click(AdminProductsLocators.PRODUCTS)

    def _switch_to_product_iframe(self):
        iframe = self.wait.until(EC.presence_of_element_located(AdminProductsLocators.PRODUCT_IFRAME))
        self.driver.switch_to.frame(iframe)

    def _switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def add_product(self, name):
        self.click(AdminProductsLocators.ADD_PRODUCT)
        self.wait.until(EC.visibility_of_element_located(AdminProductsLocators.WAIT_PRODUCT_ADD))
        self._switch_to_product_iframe()

        self.wait.until(EC.element_to_be_clickable(AdminProductsLocators.ADD_PRODUCT_ADD))
        self.click(AdminProductsLocators.ADD_PRODUCT_ADD)

        self._switch_to_default_content()

        self.wait.until(EC.invisibility_of_element_located(AdminProductsLocators.WAIT_PRODUCT_ADD))
        self.wait.until(EC.presence_of_element_located(AdminProductsLocators.PRODUCT_NAME))
        self.type(AdminProductsLocators.PRODUCT_NAME, name)
        self.click(AdminProductsLocators.SAVE)

    def delete_product(self):
        self.click(AdminProductsLocators.FIND_DELETE)
        self.wait.until(EC.element_to_be_clickable(AdminProductsLocators.DELETE))
        self.click(AdminProductsLocators.DELETE)
        self.wait.until(EC.element_to_be_clickable(AdminProductsLocators.CONFIRM_DELETE))
        self.click(AdminProductsLocators.CONFIRM_DELETE)

    def is_product_added(self):
        self.wait.until(EC.presence_of_element_located(AdminProductsLocators.ADD_SUCCESS))
        return True

    def is_product_deleted(self):
        self.wait.until(EC.presence_of_element_located(AdminProductsLocators.DELETE_SUCCESS))
        return True

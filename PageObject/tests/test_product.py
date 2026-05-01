import random
from pages.admin_login_page import AdminLoginPage
from pages.admin_products_page import AdminProductsPage


def test_add_product(driver, base_url):
    login = AdminLoginPage(driver)
    login.open(base_url + "administration")
    login.login("admin@example.com", "Admin123!")
    assert login.is_logged_in()

    products = AdminProductsPage(driver)
    products.open_products()

    name = "TestProduct" + str(random.randint(1, 1000))
    products.add_product(name)


def test_delete_product(driver, base_url):
    login = AdminLoginPage(driver)
    login.open(base_url + "administration")
    login.login("admin@example.com", "Admin123!")

    products = AdminProductsPage(driver)
    products.open_products()
    products.delete_product()
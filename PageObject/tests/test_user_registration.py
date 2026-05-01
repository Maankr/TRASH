import random
from pages.register_page import RegisterPage


def test_user_registration(driver, base_url):
    page = RegisterPage(driver)
    page.open(base_url + "registration")

    email = f"test{random.randint(1,10000)}@mail.com"

    page.register("John", "Doe", email, "Password123!")
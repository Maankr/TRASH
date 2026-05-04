import random
from pages.register_page import RegisterPage


def test_user_registration(driver, base_url):
    page = RegisterPage(driver)
    page.open(base_url + "registration")

    email = f"test{random.randint(1, 10000)}@mail.com"

    page.register("Nik", "Dfee", email, "Password187654623!")

    # Проверка успешной регистрации
    assert page.is_registration_successful(), "User registration failed"
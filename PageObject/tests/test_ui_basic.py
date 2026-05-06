from pages.home_page import HomePage


def test_home_page(driver, base_url):
    home = HomePage(driver)
    home.open(base_url)

    assert len(home.get_prices()) > 0
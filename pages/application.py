"""Это фикстура. Она админит страницы, раздает доступ к wd."""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.auth_page import LoginPage
from pages.cards_page import CardsPage
from pages.currency_page import CurrencyPage
from pages.deposits_page import DepositsPage


class Application:
    # def __init__(self, base_url: str, headless):
    def __init__(self, base_url: str):
        driver_path = ChromeDriverManager().install()
        # options: Options = Options()
        # options.headless = headless
        # self.wd = webdriver.Chrome(driver_path, options=options)
        self.wd = webdriver.Chrome(driver_path)
        self.base_url = base_url
        self.login = LoginPage(self)
        self.currency = CurrencyPage(self)
        self.deposits = DepositsPage(self)
        self.cards = CardsPage(self)

    def open_main_page(self):
        self.wd.get(self.base_url)

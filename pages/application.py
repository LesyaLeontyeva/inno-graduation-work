"""Это фикстура. Она админит страницы, раздает доступ к wd."""
import logging

import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.auth_page import LoginPage
from pages.cards_page import CardsPage
from pages.credit_page import CreditPage
from pages.currency_page import CurrencyPage
from pages.deposits_page import DepositsPage
from utils.logger import setup

logger = logging.getLogger()


class Application:
    def __init__(self, base_url: str, headless):
        setup("INFO")
        driver_path = ChromeDriverManager().install()
        options = Options()
        # if headless:
        #     options.add_argument("--headless")
        self.wd = webdriver.Chrome(driver_path, options=options)
        self.base_url = base_url
        self.login = LoginPage(self)
        self.currency = CurrencyPage(self)
        self.deposits = DepositsPage(self)
        self.cards = CardsPage(self)
        self.credit = CreditPage(self)

    @allure.step("Открытие главное страницы")
    def open_main_page(self):
        logger.info("Открытие главное страницы")
        self.wd.get(self.base_url)

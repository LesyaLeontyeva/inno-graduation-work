"""Методы страницы Кредиты."""
import allure
from selenium.common.exceptions import NoSuchWindowException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

from locators.credit import CreditLocators
import logging

logger = logging.getLogger()


class CreditPage:
    """Класс с функциями для работы с разделом Кредиты."""

    def __init__(self, app):
        self.app = app
        self.wait = WebDriverWait(self.app.wd, 20)

    @allure.step("Нажимает на кнопку Кредиты")
    def click_on_credit_button(self):
        logger.info("Нажимает на кнопку Кредиты")
        return self.app.wd.find_element(*CreditLocators.CREDIT_BUTTON).click()

    @allure.step("Кликает на выбранный кредит")
    def click_on_credit(self):
        logger.info("Кликает на выбранный кредит")
        self.wait.until(EC.element_to_be_clickable(CreditLocators.CREDIT_NUMBER))
        return self.app.wd.find_element(*CreditLocators.CREDIT_NUMBER).click()

    @allure.step("Нажимает на кнопку Закрыть кредит")
    def click_on_close_credit_button(self):
        logger.info("Нажимает на кнопку Закрыть кредит")
        return self.app.wd.find_element(*CreditLocators.CLOSE_BUTTON).click()

    @allure.step("Выбирает офис")
    def choose_office(self):
        logger.info("Выбирает офис")
        self.wait.until(EC.element_to_be_clickable(CreditLocators.CHOOSE_OFFICE))
        select = Select(self.app.wd.find_element(*CreditLocators.CHOOSE_OFFICE))
        select.select_by_value("001-010")

    @allure.step("Нажимает на кнопку Отправить")
    def submit_button(self):
        logger.info("Нажимает на кнопку Отправить")
        self.wait.until(EC.element_to_be_clickable(CreditLocators.SEND_BUTTON))
        return self.app.wd.find_element(*CreditLocators.SEND_BUTTON).click()

    @allure.step("Нажимает на кнопку Подтвердить")
    def confirm_button(self):
        logger.info("Нажимает на кнопку Подтвердить")
        self.wait.until(
            EC.frame_to_be_available_and_switch_to_it(CreditLocators.CONFIRMATION_FRAME)
        )
        try:
            return self.app.wd.find_element(*CreditLocators.SUBMIT_BUTTON).click()
        except NoSuchWindowException:
            self.wait.until(EC.element_to_be_clickable(CreditLocators.SUBMIT_BUTTON))
            return self.app.wd.find_element(*CreditLocators.SUBMIT_BUTTON).click()

    def get_alert_text(self):
        self.app.wd.switch_to.default_content()
        try:
            self.wait.until(
                EC.visibility_of_element_located(CreditLocators.SUCCESS_ALERT)
            )
            return self.app.wd.find_element(*CreditLocators.SUCCESS_ALERT).text
        except NoSuchElementException:
            self.wait.until(
                EC.visibility_of_element_located(CreditLocators.SUCCESS_ALERT)
            )
            return self.app.wd.find_element(*CreditLocators.SUCCESS_ALERT).text

    @allure.step("Нажимает на кнопку опций")
    def click_on_option(self):
        logger.info("Нажимает на кнопку опций")
        return self.app.wd.find_element(*CreditLocators.OPTION_BUTTON).click()

    @allure.step("Нажимает на кнопку Частично погасить")
    def click_on_partial(self):
        logger.info("Нажимает на кнопку Частично погасить")
        return self.app.wd.find_element(*CreditLocators.REQUEST_BUTTON).click()

    @allure.step("Вводит сумму частичного погашения")
    def input_amount(self, amount):
        logger.info("Вводит сумму частичного погашения")
        self.wait.until(EC.element_to_be_clickable(CreditLocators.INPUT_AMOUNT))
        self.app.wd.find_element(*CreditLocators.INPUT_AMOUNT).send_keys(amount)

    @allure.step("Нажимает на радиобаттон изменения графика платежей")
    def click_on_radiobutton(self):
        logger.info("Нажимает на радиобаттон изменения графика платежей")
        self.wait.until(EC.element_to_be_clickable(CreditLocators.CHOOSE_RADIOBUTTON))
        return self.app.wd.find_element(*CreditLocators.CHOOSE_RADIOBUTTON).click()

    @allure.step("Нажимает на кнопку Соглашения")
    def click_on_checkbox(self):
        logger.info("Нажимает на кнопку Соглашения")
        self.wait.until(EC.element_to_be_clickable(CreditLocators.CHECKBOX))
        return self.app.wd.find_element(*CreditLocators.CHECKBOX).click()

    @allure.step("Нажимает на кнопку Кредитная история")
    def click_on_history(self):
        logger.info("Нажимает на кнопку Кредитная история")
        return self.app.wd.find_element(*CreditLocators.HISTORY_BUTTON).click()

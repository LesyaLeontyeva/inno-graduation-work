"""Методы страницы Валюта."""

from typing import Any

import allure
from selenium.common.exceptions import (
    NoSuchWindowException,
    ElementClickInterceptedException,
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
    ElementNotInteractableException,
)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import logging

from locators.currency import CurrencyLocators

logger = logging.getLogger()


class CurrencyPage:
    """Класс с функциями для работы с разделом Валюта."""

    def __init__(self, app):
        self.app = app
        self.wait = WebDriverWait(self.app.wd, 20)

    @allure.step("Нажимает на кнопку Валюта")
    def click_on_currency_button(self):
        logger.info("Нажимает на кнопку Валюта")
        self.app.wd.switch_to.default_content()
        try:
            self.wait.until(
                EC.element_to_be_clickable(CurrencyLocators.CURRENCY_BUTTON)
            )
            return self.app.wd.find_element(*CurrencyLocators.CURRENCY_BUTTON).click()
        except TimeoutException:
            self.wait.until(
                EC.element_to_be_clickable(CurrencyLocators.CURRENCY_BUTTON)
            )
            return self.app.wd.find_element(*CurrencyLocators.CURRENCY_BUTTON).click()

    @allure.step("Вводит сумму")
    def input_amount(self, amount: int) -> Any:
        logger.info("Вводит сумму")
        self.wait.until(
            EC.frame_to_be_available_and_switch_to_it(CurrencyLocators.FRAME_XPATH)
        )
        try:
            self.wait.until(
                EC.visibility_of_element_located(CurrencyLocators.INPUT_AMOUNT)
            )
            element = self.app.wd.find_element(*CurrencyLocators.INPUT_AMOUNT)
            element.send_keys(amount)
        except (StaleElementReferenceException, ElementNotInteractableException):
            self.wait.until(EC.element_to_be_clickable(CurrencyLocators.INPUT_AMOUNT))
            element = self.app.wd.find_element(*CurrencyLocators.INPUT_AMOUNT)
            element.send_keys(amount)

    @allure.step("Нажимает на кнопку Подтвердить")
    def click_on_submit_button_with_frame(self) -> Any:
        logger.info("Нажимает на кнопку Подтвердить")
        self.wait.until(
            EC.frame_to_be_available_and_switch_to_it(CurrencyLocators.FRAME_XPATH)
        )
        try:
            return self.app.wd.find_element(*CurrencyLocators.SUBMIT_BUTTON).click()
        except ElementClickInterceptedException:
            self.wait.until(EC.element_to_be_clickable(CurrencyLocators.SUBMIT_BUTTON))
            return self.app.wd.find_element(*CurrencyLocators.SUBMIT_BUTTON).click()

    @allure.step("Вводит смс код")
    def input_sms_code(self, code) -> None:
        logger.info("Вводит смс код")
        self.wait.until(
            EC.frame_to_be_available_and_switch_to_it(CurrencyLocators.FRAME_CONFIRM)
        )
        try:
            element = self.app.wd.find_element(*CurrencyLocators.SMS_CODE_INPUT)
            element.send_keys(code)
        except NoSuchWindowException:
            self.wait.until(EC.element_to_be_clickable(CurrencyLocators.SMS_CODE_INPUT))
            element = self.app.wd.find_element(*CurrencyLocators.SMS_CODE_INPUT)
            element.send_keys(code)

    @allure.step("Нажимает на кнопку Подтвердить")
    def click_on_confirm_button(self) -> Any:
        logger.info("Нажимает на кнопку Подтвердить")
        return self.app.wd.find_element(*CurrencyLocators.SMS_CONFIRM_BUTTON).click()

    @allure.step("Закрывает сообщение")
    def click_on_close_alert(self) -> Any:
        logger.info("Закрывает сообщение")
        return self.app.wd.find_element(*CurrencyLocators.CLOSE_ALERT_BUTTON).click()

    def get_alert_text(self) -> str:
        self.wait.until(
            EC.frame_to_be_available_and_switch_to_it(CurrencyLocators.FRAME_XPATH)
        )
        try:
            self.wait.until(
                EC.visibility_of_element_located(CurrencyLocators.SUCCESS_ALERT)
            )
            return self.app.wd.find_element(*CurrencyLocators.SUCCESS_ALERT).text
        except NoSuchElementException:
            self.wait.until(
                EC.visibility_of_element_located(CurrencyLocators.SUCCESS_ALERT)
            )
            return self.app.wd.find_element(*CurrencyLocators.SUCCESS_ALERT).text

    @allure.step("Выбирает фунтовый счет")
    def choose_pound_account(self) -> None:
        logger.info("Выбирает фунтовый счет")
        self.wait.until(
            EC.frame_to_be_available_and_switch_to_it(CurrencyLocators.FRAME_XPATH)
        )
        self.wait.until(EC.element_to_be_clickable(CurrencyLocators.ACCOUNT_SELECTOR))
        self.app.wd.find_element(*CurrencyLocators.ACCOUNT_SELECTOR).click()
        self.wait.until(
            EC.visibility_of_element_located(CurrencyLocators.ACCOUNT_POUND_OPTION)
        )
        return self.app.wd.find_element(*CurrencyLocators.ACCOUNT_POUND_OPTION).click()

    @allure.step("Выбирает рублевый счет")
    def choose_rub_account(self) -> None:
        logger.info("Выбирает рублевый счет")
        self.wait.until(
            EC.frame_to_be_available_and_switch_to_it(CurrencyLocators.FRAME_XPATH)
        )
        self.wait.until(EC.element_to_be_clickable(CurrencyLocators.ACCOUNT_SELECTOR))
        self.app.wd.find_element(*CurrencyLocators.ACCOUNT_SELECTOR).click()
        self.wait.until(EC.element_to_be_clickable(CurrencyLocators.ACCOUNT_RUB_OPTION))
        return self.app.wd.find_element(*CurrencyLocators.ACCOUNT_RUB_OPTION).click()

    @allure.step("Нажимает на кнопку Обменять")
    def click_on_exchange(self) -> Any:
        logger.info("Нажимает на кнопку Обменять")
        return self.app.wd.find_element(*CurrencyLocators.STOCK_EXCHANGE).click()

    @allure.step("Нажимает на кнопку Подтвердить")
    def click_on_submit_button_no_frame(self) -> Any:
        logger.info("Нажимает на кнопку Подтвердить")
        self.wait.until(EC.element_to_be_clickable(CurrencyLocators.SUBMIT_BUTTON))
        return self.app.wd.find_element(*CurrencyLocators.SUBMIT_BUTTON).click()

    @allure.step("Ищет знак вопроса с ошибкой на странице")
    def find_error_sign(self) -> bool:
        logger.info("Ищет знак вопроса с ошибкой на странице")
        self.wait.until(EC.visibility_of_element_located(CurrencyLocators.ERROR_SIGN))
        return self.app.wd.find_element(*CurrencyLocators.ERROR_SIGN).is_displayed()

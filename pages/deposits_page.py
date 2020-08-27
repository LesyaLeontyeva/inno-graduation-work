"""Методы страницы Вклады."""

import time
from typing import Any

import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.deposits import DepositsLocators

import logging

logger = logging.getLogger()


class DepositsPage:
    """Класс с функциями для работы с разделом Вклады."""

    def __init__(self, app):
        self.app = app
        self.wait = WebDriverWait(self.app.wd, 20)

    @allure.step("Нажимает на кнопку Вклады")
    def click_on_deposit_button(self) -> Any:
        logger.info("Нажимает на кнопку Вклады")
        self.app.wd.switch_to.default_content()
        try:
            self.wait.until(
                EC.element_to_be_clickable(DepositsLocators.DEPOSITS_BUTTON)
            )
            return self.app.wd.find_element(*DepositsLocators.DEPOSITS_BUTTON).click()
        except TimeoutException:
            self.wait.until(
                EC.element_to_be_clickable(DepositsLocators.DEPOSITS_BUTTON)
            )
            return self.app.wd.find_element(*DepositsLocators.DEPOSITS_BUTTON).click()

    @allure.step("Нажимает на кнопку Открыть вклад")
    def click_on_open_deposit(self) -> Any:
        logger.info("Нажимает на кнопку Открыть вклад")
        self.wait.until(
            EC.element_to_be_clickable(DepositsLocators.OPEN_DEPOSIT_BUTTON)
        )
        return self.app.wd.find_element(*DepositsLocators.OPEN_DEPOSIT_BUTTON).click()

    @allure.step("Нажимает на выбранный депозит в списке")
    def click_on_first_deposit(self) -> Any:
        logger.info("Нажимает на выбранный депозит в списке")
        self.wait.until(
            EC.element_to_be_clickable(DepositsLocators.OPEN_CHOSEN_DEPOSIT_BUTTON)
        )
        return self.app.wd.find_element(
            *DepositsLocators.OPEN_CHOSEN_DEPOSIT_BUTTON
        ).click()

    @allure.step("Вводит сумму вклада")
    def enter_deposit_amount(self, amount) -> Any:
        logger.info("Вводит сумму вклада")
        self.wait.until(EC.element_to_be_clickable(DepositsLocators.AMOUNT_FIELD))
        return self.app.wd.find_element(*DepositsLocators.AMOUNT_FIELD).send_keys(
            amount
        )

    @allure.step("Нажимает на кнопку Подтвердить")
    def click_submit_button(self) -> Any:
        logger.info("Нажимает на кнопку Подтвердить")
        time.sleep(10)  # попробуй сделать цикл try except
        self.wait.until(EC.element_to_be_clickable(DepositsLocators.SUBMIT_BUTTON))
        return self.app.wd.find_element(*DepositsLocators.SUBMIT_BUTTON).click()

    @allure.step("Нажимает на кнопку Соглашение")
    def check_conditions(self) -> Any:
        logger.info("Нажимает на кнопку Соглашение")
        self.wait.until(
            EC.element_to_be_clickable(DepositsLocators.CONDITIONS_CHECKBOX)
        )
        element = self.app.wd.find_element(*DepositsLocators.CONDITIONS_CHECKBOX)
        element.click()

    @allure.step("Нажимает на кнопку Подтверждение")
    def click_on_confirm_checkbox(self) -> Any:
        logger.info("Нажимает на кнопку Подтверждение")
        self.wait.until(EC.element_to_be_clickable(DepositsLocators.TEST_PATH))
        return self.app.wd.find_element(*DepositsLocators.TEST_PATH).click()

    @allure.step("Нажимает на кнопку Отправить")
    def click_on_confirm(self) -> Any:
        logger.info("Нажимает на кнопку Отправить")
        self.wait.until(EC.element_to_be_clickable(DepositsLocators.CONFIRM_BUTTON))
        return self.app.wd.find_element(*DepositsLocators.CONFIRM_BUTTON).click()

    def get_success_text(self) -> str:
        self.wait.until(
            EC.visibility_of_element_located(DepositsLocators.SUCCESS_ALERT)
        )
        return self.app.wd.find_element(*DepositsLocators.SUCCESS_ALERT).text

    @allure.step("Нажимает на кнопку опций")
    def click_on_option_button(self) -> Any:
        logger.info("Нажимает на кнопку опций")
        self.wait.until(EC.element_to_be_clickable(DepositsLocators.CHOSEN_DEPOSIT))
        return self.app.wd.find_element(*DepositsLocators.CHOSEN_DEPOSIT).click()

    @allure.step("Нажимает на кнопку Закрыть")
    def close_deposit_button(self) -> Any:
        logger.info("Нажимает на кнопку Закрыть")
        self.wait.until(
            EC.element_to_be_clickable(DepositsLocators.CLOSE_DEPOSIT_BUTTON)
        )
        return self.app.wd.find_element(*DepositsLocators.CLOSE_DEPOSIT_BUTTON).click()

"""Методы страницы Карты."""
import logging
from typing import Any

import allure
from selenium.common.exceptions import (
    NoSuchWindowException,
    NoSuchElementException,
    TimeoutException,
)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

from locators.сards import CardsLocators

logger = logging.getLogger()


class CardsPage:
    """Класс с функциями для работы с разделом Карты."""

    def __init__(self, app):
        self.app = app
        self.wait = WebDriverWait(self.app.wd, 20)

    @allure.step("Нажимает на кнопку Карты")
    def click_on_cards_button(self) -> Any:
        logger.info("Нажимает на кнопку Карты")
        self.wait.until(EC.element_to_be_clickable(CardsLocators.CARDS_BUTTON))
        return self.app.wd.find_element(*CardsLocators.CARDS_BUTTON).click()

    @allure.step("Нажимает на кнопку на Заказать карту")
    def order_new_card(self) -> Any:
        logger.info("Нажимает на кнопку на Заказать карту")
        self.wait.until(EC.element_to_be_clickable(CardsLocators.OPEN_NEW_CARD_BUTTON))
        return self.app.wd.find_element(*CardsLocators.OPEN_NEW_CARD_BUTTON).click()

    @allure.step("Выбирает первую опцию из предложенных")
    def choose_first_option(self) -> Any:
        logger.info("Выбирает первую опцию из предложенных")
        self.wait.until(
            EC.element_to_be_clickable(CardsLocators.INCREASE_BONUS_CHECKBOX)
        )
        return self.app.wd.find_element(*CardsLocators.INCREASE_BONUS_CHECKBOX).click()

    @allure.step("Нажимает на кнопку на Заказать кнопку")
    def order_chosen_card(self) -> Any:
        logger.info("Нажимает на кнопку на Заказать кнопку")
        self.wait.until(EC.element_to_be_clickable(CardsLocators.ORDER_BUTTON))
        return self.app.wd.find_element(*CardsLocators.ORDER_BUTTON).click()

    @allure.step("Вводит сумму заработной платы")
    def input_amount(self, amount) -> Any:
        logger.info("Вводит сумму заработной платы")
        self.wait.until(EC.element_to_be_clickable(CardsLocators.AMOUNT_FIELD))
        element = self.app.wd.find_element(*CardsLocators.AMOUNT_FIELD)
        element.send_keys(amount)

    @allure.step("Отмечает первый чекбокс соглашения")
    def choose_first_checkbox(self) -> Any:
        logger.info("Отмечает первый чекбокс соглашения")
        return self.app.wd.find_element(*CardsLocators.FIRST_CHECKBOX).click()

    @allure.step("Отмечает второй чекбокс соглашения")
    def choose_second_button(self) -> Any:
        logger.info("Отмечает второй чекбокс соглашения")
        return self.app.wd.find_element(*CardsLocators.SECOND_CHECKBOX).click()

    @allure.step("Отмечает третий чекбокс соглашения")
    def choose_third_button(self) -> Any:
        logger.info("Отмечает третий чекбокс соглашения")
        return self.app.wd.find_element(*CardsLocators.THIRD_CHECKBOX).click()

    @allure.step("Нажимает на кнопку Отправить")
    def send_request(self) -> Any:
        logger.info("Нажимает на кнопку Отправить")
        self.wait.until(EC.element_to_be_clickable(CardsLocators.SEND_REQUEST))
        return self.app.wd.find_element(*CardsLocators.SEND_REQUEST).click()

    @allure.step("Нажимает на кнопку Подтвердить")
    def confirm_request(self) -> Any:
        logger.info("Нажимает на кнопку Подтвердить")
        self.wait.until(EC.element_to_be_clickable(CardsLocators.SUBMIT_BUTTON))
        return self.app.wd.find_element(*CardsLocators.SUBMIT_BUTTON).click()

    def find_success_alert(self) -> str:
        try:
            self.wait.until(
                EC.visibility_of_element_located(CardsLocators.SUCCESS_ALERT)
            )
            return self.app.wd.find_element(*CardsLocators.SUCCESS_ALERT).text
        except NoSuchWindowException:
            self.wait.until(
                EC.visibility_of_element_located(CardsLocators.SUCCESS_ALERT)
            )
            return self.app.wd.find_element(*CardsLocators.SUCCESS_ALERT).text

    @allure.step("Нажимает на кнопку СМС уведомления")
    def sms_button(self) -> Any:
        logger.info("Нажимает на кнопку СМС уведомления")
        self.wait.until(EC.element_to_be_clickable(CardsLocators.SMS))
        return self.app.wd.find_element(*CardsLocators.SMS).click()

    @allure.step("Нажимает на кнопку 'Подключить'")
    def connect_button(self) -> Any:
        logger.info("Нажимает на кнопку 'Подключить'")
        self.wait.until(EC.element_to_be_clickable(CardsLocators.BUTTON))
        return self.app.wd.find_element(*CardsLocators.BUTTON).click()

    @allure.step("Нажимает на кнопку 'Подтвердить'")
    def submit(self) -> Any:
        logger.info("Нажимает на кнопку 'Подтвердить'")
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(CardsLocators.FRAME))
        try:
            return self.app.wd.find_element(*CardsLocators.CONFIRM).click()
        except NoSuchWindowException:
            self.wait.until(EC.element_to_be_clickable(CardsLocators.CONFIRM))
            return self.app.wd.find_element(*CardsLocators.CONFIRM).click()

    def find_alert_warning(self) -> str:
        return self.app.wd.find_element(*CardsLocators.WARNING_ALERT).text

    @allure.step("Нажимает на кнопку 'Удалить'")
    def click_on_delete_sms(self) -> Any:
        logger.info("Нажимает на кнопку 'Удалить'")
        self.wait.until(EC.element_to_be_clickable(CardsLocators.DELETE))
        return self.app.wd.find_element(*CardsLocators.DELETE).click()

    @allure.step("Нажимает на кнопку 'E-mail уведомления'")
    def click_on_email(self) -> Any:
        logger.info("Нажимает на кнопку 'E-mail уведомления'")
        self.wait.until(EC.element_to_be_clickable(CardsLocators.EMAIL))
        return self.app.wd.find_element(*CardsLocators.EMAIL).click()

    @allure.step("Нажимает  на радиобаттон 'E-mail'")
    def click_on_email_radiobutton(self) -> Any:
        logger.info("Нажимает  на радиобаттон 'E-mail'")
        self.wait.until(EC.element_to_be_clickable(CardsLocators.EMAIL_RADIOBUTTON))
        return self.app.wd.find_element(*CardsLocators.EMAIL_RADIOBUTTON).click()

    @allure.step("Нажимает на список офисов")
    def click_on_office_list(self) -> Any:
        logger.info("Нажимает на список офисов")
        self.wait.until(
            EC.element_to_be_clickable(CardsLocators.CHOOSE_OFFICE_SELECTOR)
        )
        return self.app.wd.find_element(*CardsLocators.CHOOSE_OFFICE_SELECTOR).click()

    @allure.step("Выбирает отделение")
    def choose_office(self) -> None:
        logger.info("Выбирает отделение")
        self.wait.until(
            EC.element_to_be_clickable(CardsLocators.CHOOSE_OFFICE_SELECTOR)
        )
        select = Select(self.app.wd.find_element(*CardsLocators.CHOOSE_OFFICE_SELECTOR))
        select.select_by_value("001-055")

    @allure.step("Нажимаем на кнопку 'Заказать'")
    def order_card(self) -> Any:
        logger.info("Нажимаем на кнопку 'Заказать'")
        self.wait.until(EC.element_to_be_clickable(CardsLocators.ORDER_CARD))
        return self.app.wd.find_element(*CardsLocators.ORDER_CARD).click()

    @allure.step("Нажимаем на кнопку 'Подтвердить'")
    def click_on_confirm_button(self) -> Any:
        logger.info("Нажимаем на кнопку 'Подтвердить'")
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(CardsLocators.FRAME))
        try:
            return self.app.wd.find_element(*CardsLocators.CONFIRM_ORDER).click()
        except NoSuchWindowException:
            self.wait.until(EC.element_to_be_clickable(CardsLocators.CONFIRM_ORDER))
            return self.app.wd.find_element(*CardsLocators.CONFIRM_ORDER).click()

    @allure.step("Нажимаем кнопку 'Подключить e-mail'")
    def click_on_email_connect(self) -> Any:
        logger.info("Нажимаем кнопку 'Подключить e-mail'")
        self.wait.until(EC.element_to_be_clickable(CardsLocators.CONNECT_BUTTON))
        return self.app.wd.find_element(*CardsLocators.CONNECT_BUTTON).click()

    @allure.step("Нажимаем на кнопку 'Оплата в интернете'")
    def click_on_pay_in_internet_button(self) -> Any:
        logger.info("Нажимаем на кнопку 'Оплата в интернете'")
        self.wait.until(EC.element_to_be_clickable(CardsLocators.PAY_IN_INTERNET))
        return self.app.wd.find_element(*CardsLocators.PAY_IN_INTERNET).click()

    @allure.step("Заказываем карту")
    def submit_order_card(self) -> None:
        logger.info("Заказываем карту")
        try:
            self.input_amount(amount=100000)
            self.choose_first_checkbox()
            self.choose_second_button()
            self.choose_third_button()
            self.send_request()
            self.click_on_confirm_button()
        except (NoSuchElementException, TimeoutException):
            self.choose_office()
            self.order_card()
            self.click_on_confirm_button()

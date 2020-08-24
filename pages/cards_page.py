from typing import Any

import allure
from selenium.common.exceptions import NoSuchWindowException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

from locators.сards import CardsLocators


class CardsPage:
    """Класс с функциями для работы с разделом Карты."""

    def __init__(self, app):
        self.app = app
        self.wait = WebDriverWait(self.app.wd, 10)

    @allure.step("Делаем клик на кнопку Карты")
    def click_on_cards_button(self) -> Any:
        self.wait.until(EC.element_to_be_clickable(CardsLocators.CARDS_BUTTON))
        return self.app.wd.find_element(*CardsLocators.CARDS_BUTTON).click()

    @allure.step("Делаем клик на Заказать карту")
    def order_new_card(self) -> Any:
        self.wait.until(EC.element_to_be_clickable(CardsLocators.OPEN_NEW_CARD_BUTTON))
        return self.app.wd.find_element(*CardsLocators.OPEN_NEW_CARD_BUTTON).click()

    @allure.step("Выбираем первую опцию из предложенных")
    def choose_first_option(self) -> Any:
        self.wait.until(
            EC.element_to_be_clickable(CardsLocators.INCREASE_BONUS_CHECKBOX)
        )
        return self.app.wd.find_element(*CardsLocators.INCREASE_BONUS_CHECKBOX).click()

    @allure.step("Делаем клик на Заказать кнопку")
    def order_chosen_card(self) -> Any:
        self.wait.until(EC.element_to_be_clickable(CardsLocators.ORDER_BUTTON))
        return self.app.wd.find_element(*CardsLocators.ORDER_BUTTON).click()

    @allure.step("Вводим сумму заработной платы")
    def input_amount(self, amount) -> Any:
        self.wait.until(EC.element_to_be_clickable(CardsLocators.AMOUNT_FIELD))
        element = self.app.wd.find_element(*CardsLocators.AMOUNT_FIELD)
        element.send_keys(amount)

    @allure.step("Отмечаем первый чекбокс соглашения")
    def choose_first_checkbox(self) -> Any:
        return self.app.wd.find_element(*CardsLocators.FIRST_CHECKBOX).click()

    @allure.step("Отмечаем второй чекбокс соглашения")
    def choose_second_button(self) -> Any:
        return self.app.wd.find_element(*CardsLocators.SECOND_CHECKBOX).click()

    @allure.step("Отмечаем третий чекбокс соглашения")
    def choose_third_button(self) -> Any:
        return self.app.wd.find_element(*CardsLocators.THIRD_CHECKBOX).click()

    @allure.step("Делаем клик на кнопку Отправить")
    def send_request(self) -> Any:
        self.wait.until(EC.element_to_be_clickable(CardsLocators.SEND_REQUEST))
        return self.app.wd.find_element(*CardsLocators.SEND_REQUEST).click()

    @allure.step("Делаем клик на кнопку Подтвердить")
    def confirm_request(self) -> Any:
        self.wait.until(EC.element_to_be_clickable(CardsLocators.SUBMIT_BUTTON))
        return self.app.wd.find_element(*CardsLocators.SUBMIT_BUTTON).click()

    def find_success_alert(self) -> str:
        self.wait.until(EC.visibility_of_element_located(CardsLocators.SUCCESS_ALERT))
        return self.app.wd.find_element(*CardsLocators.SUCCESS_ALERT).text

    @allure.step("Делаем клик на кнопку СМС уведомления")
    def sms_button(self) -> Any:
        self.wait.until(EC.element_to_be_clickable(CardsLocators.SMS))
        return self.app.wd.find_element(*CardsLocators.SMS).click()

    @allure.step("Делаем клик на кнопку 'Подключить'")
    def connect_button(self) -> Any:
        self.wait.until(EC.element_to_be_clickable(CardsLocators.BUTTON))
        return self.app.wd.find_element(*CardsLocators.BUTTON).click()

    @allure.step("Делаем клик на кнопку 'Подтвердить'")
    def submit(self) -> Any:
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(CardsLocators.FRAME))
        try:
            return self.app.wd.find_element(*CardsLocators.CONFIRM).click()
        except NoSuchWindowException:
            self.wait.until(EC.element_to_be_clickable(CardsLocators.CONFIRM))
            return self.app.wd.find_element(*CardsLocators.CONFIRM).click()

    def find_alert_warning(self) -> str:
        return self.app.wd.find_element(*CardsLocators.WARNING_ALERT).text

    @allure.step("Делаем клик на кнопку 'Удалить'")
    def click_on_delete_sms(self) -> Any:
        self.wait.until(EC.element_to_be_clickable(CardsLocators.DELETE))
        return self.app.wd.find_element(*CardsLocators.DELETE).click()

    @allure.step("Делаем клик на кнопку 'E-mail уведомления'")
    def click_on_email(self) -> Any:
        self.wait.until(EC.element_to_be_clickable(CardsLocators.EMAIL))
        return self.app.wd.find_element(*CardsLocators.EMAIL).click()

    @allure.step("Делаем клик на радиобаттон 'E-mail'")
    def click_on_email_radiobutton(self) -> Any:
        self.wait.until(EC.element_to_be_clickable(CardsLocators.EMAIL_RADIOBUTTON))
        return self.app.wd.find_element(*CardsLocators.EMAIL_RADIOBUTTON).click()

    @allure.step("Кликаем на список офисов")
    def click_on_office_list(self) -> Any:
        self.wait.until(
            EC.element_to_be_clickable(CardsLocators.CHOOSE_OFFICE_SELECTOR)
        )
        return self.app.wd.find_element(*CardsLocators.CHOOSE_OFFICE_SELECTOR).click()

    @allure.step("Выбираем отделение")
    def choose_office(self) -> None:
        self.wait.until(
            EC.element_to_be_clickable(CardsLocators.CHOOSE_OFFICE_SELECTOR)
        )
        select = Select(self.app.wd.find_element(*CardsLocators.CHOOSE_OFFICE_SELECTOR))
        select.select_by_value("001-055")

    @allure.step("Кликаем на кнопку 'Заказать'")
    def order_card(self) -> Any:
        self.wait.until(EC.element_to_be_clickable(CardsLocators.ORDER_CARD))
        return self.app.wd.find_element(*CardsLocators.ORDER_CARD).click()

    @allure.step("Кликаем на кнопку 'Подтвердить'")
    def click_on_confirm_button(self) -> Any:
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(CardsLocators.FRAME))
        try:
            return self.app.wd.find_element(*CardsLocators.CONFIRM_ORDER).click()
        except NoSuchWindowException:
            self.wait.until(EC.element_to_be_clickable(CardsLocators.CONFIRM_ORDER))
            return self.app.wd.find_element(*CardsLocators.CONFIRM_ORDER).click()

    @allure.step("Кликаем на кнопку 'Подключить e-mail'")
    def click_on_email_connect(self) -> Any:
        self.wait.until(EC.element_to_be_clickable(CardsLocators.CONNECT_BUTTON))
        return self.app.wd.find_element(*CardsLocators.CONNECT_BUTTON).click()

    @allure.step("Кликаем на кнопку 'Оплата в интернете'")
    def click_on_pay_in_internet_button(self) -> Any:
        self.wait.until(EC.element_to_be_clickable(CardsLocators.PAY_IN_INTERNET))
        return self.app.wd.find_element(*CardsLocators.PAY_IN_INTERNET).click()

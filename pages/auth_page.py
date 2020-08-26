"""Методы авторизации страницы."""
import logging

import allure
from selenium.webdriver.remote.webelement import WebElement

from locators.login import LoginLocators
from model.login import UserData

logger = logging.getLogger()


class LoginPage:
    """Класс с методами авторизации."""

    def __init__(self, app):
        self.app = app

    @allure.step("Вводит логин")
    def input_login(self) -> WebElement:
        logger.info("Вводим логин")
        return self.app.wd.find_element(*LoginLocators.LOGIN_INPUT)

    @allure.step("Вводит пароль")
    def input_password(self) -> WebElement:
        logger.info("Вводим пароль")
        return self.app.wd.find_element(*LoginLocators.PASSWORD_INPUT)

    @allure.step("Кликает на кнопку Войти")
    def click_enter_auth(self) -> None:
        logger.info("Кликаем на кнопку Войти")
        self.app.wd.find_element(*LoginLocators.ENTER_LOGIN_BUTTON).click()

    @allure.step("Вводит смс код")
    def click_enter_sms(self) -> None:
        logger.info("Вводим смс код")
        self.app.wd.find_element(*LoginLocators.ENTER_SMS_BUTTON).click()

    @allure.step("Авторизуется")
    def auth(self, user_data: UserData) -> None:
        logger.info("Авторизуется")
        if user_data.login is not None:
            self.input_login().send_keys(user_data.login)
        if user_data.password is not None:
            self.input_password().send_keys(user_data.password)
        self.click_enter_auth()

    def find_overview_button(self) -> str:
        return self.app.wd.find_element(*LoginLocators.OVERVIEW_BUTTON).text

    def find_error_alert(self) -> str:
        return self.app.wd.find_element(*LoginLocators.ERROR_ALERT).text

    @allure.step("Очищает поле логин")
    def clear_login_field(self) -> None:
        logger.info("Очищает поле логин")
        self.app.wd.find_element(*LoginLocators.LOGIN_INPUT).clear()

    @allure.step("Очищает поле пароль")
    def clear_password_field(self) -> None:
        logger.info("Очищает поле пароль")
        self.app.wd.find_element(*LoginLocators.PASSWORD_INPUT).clear()

    @allure.step("Вводит логин")
    def input_username(self, username):
        logger.info("Вводит логин")
        self.app.wd.find_element(*LoginLocators.LOGIN_INPUT).clear()
        return self.app.wd.find_element(*LoginLocators.LOGIN_INPUT).send_keys(username)

    @allure.step("Вводит пароль")
    def input_pass(self, password):
        logger.info("Вводит пароль")
        self.app.wd.find_element(*LoginLocators.PASSWORD_INPUT).clear()
        return self.app.wd.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(
            password
        )

"""Методы авторизации страницы."""

import allure
from selenium.webdriver.remote.webelement import WebElement

from locators.login import LoginLocators
from model.login import UserData


class LoginPage:
    """Класс с методами авторизации."""

    def __init__(self, app):
        self.app = app

    @allure.step("Вводим логин")
    def input_login(self) -> WebElement:
        return self.app.wd.find_element(*LoginLocators.LOGIN_INPUT)

    @allure.step("Вводим пароль")
    def input_password(self) -> WebElement:
        return self.app.wd.find_element(*LoginLocators.PASSWORD_INPUT)

    @allure.step("Кликаем на Войти")
    def click_enter_auth(self) -> None:
        self.app.wd.find_element(*LoginLocators.ENTER_LOGIN_BUTTON).click()

    @allure.step("Вводим смс")
    def click_enter_sms(self) -> None:
        self.app.wd.find_element(*LoginLocators.ENTER_SMS_BUTTON).click()

    @allure.step("Авторизуемся")
    def auth(self, user_data: UserData) -> None:
        if user_data.login is not None:
            self.input_login().send_keys(user_data.login)
        if user_data.password is not None:
            self.input_password().send_keys(user_data.password)
        self.click_enter_auth()

    def find_overview_button(self) -> str:
        return self.app.wd.find_element(*LoginLocators.OVERVIEW_BUTTON).text

    def find_error_alert(self) -> str:
        return self.app.wd.find_element(*LoginLocators.ERROR_ALERT).text

    @allure.step("Очищаем поле логин")
    def clear_login_field(self) -> None:
        self.app.wd.find_element(*LoginLocators.LOGIN_INPUT).clear()

    @allure.step("Очищаем поле пароль")
    def clear_password_field(self) -> None:
        self.app.wd.find_element(*LoginLocators.PASSWORD_INPUT).clear()

    @allure.step("Ввод логина")
    def input_username(self, username):
        self.app.wd.find_element(*LoginLocators.LOGIN_INPUT).clear()
        return self.app.wd.find_element(*LoginLocators.LOGIN_INPUT).send_keys(username)

    @allure.step("Ввод пароля")
    def input_pass(self, password):
        self.app.wd.find_element(*LoginLocators.PASSWORD_INPUT).clear()
        return self.app.wd.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(
            password
        )

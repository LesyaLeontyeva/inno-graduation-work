"""Тесты на авторизацию."""
import allure
import pytest
from pytest_testrail.plugin import testrail

from constants.login import Login
from model.login import UserData


@allure.suite("Тесты на авторизацию")
class TestAuth:
    """Класс тестов для раздела Карты."""

    @allure.title("Тест на успешную авторизацию")
    @allure.tag("позитивный кейс")
    @testrail("C55")
    def test_auth(self, app) -> None:
        """
        Шаги:
        1. Пользователь переходит на сайт
        2. Пользоавтель делает клик на кнопку "Войти"
        (валидные данные уже заполнены по умолчанию)
        3. Пользователь закрывает системный алерт
        4. Пользователь делает клик на кнопку "Войти"
        5. Проверяем наличие кнопки "Обзор".
        """
        app.open_main_page()
        app.login.click_enter_auth()
        app.login.click_enter_sms()
        assert app.login.find_overview_button() == Login.SUCCESS

    @allure.title("Пользователь вводит неверный логин")
    @allure.tag("негативный кейс")
    @testrail("C56")
    def test_auth_negative_login(self, app) -> None:
        """
        Шаги:
        1. Пользователь переходит на сайт
        2. Пользоавтель вводит любое значение в поле логин
        3. Пользователь НЕ трогает поле пароль (оно уже предзаполнено)
        4. Пользователь делает клик на кнопку "Войти"
        5. Проверяем наличие текста "Неверные данные пользователя (осталось 2 попытки)".
        """
        app.open_main_page()
        user_data = UserData(login="admin", password="demo")
        app.login.clear_login_field()
        app.login.auth(user_data)
        assert app.login.find_error_alert() in Login.ERROR_ALERTS

    @allure.title("Пользователь вводит неверный пароль")
    @allure.tag("негативный кейс")
    @testrail("C57")
    def test_auth_negative_password(self, app) -> None:
        """
        Шаги:
        1. Пользователь переходит на сайт
        2. Пользоавтель ничего не вводит в поле логин
        (поле уже предзаполнено по умолчанию)
        3. Пользователь вводит невалидное значение в поле "пароль"
        4. Пользователь делает клик на кнопку "Войти"
        5. Проверяем наличие текста "Неверные данные пользователя (осталось 2 попытки)".
        """
        app.open_main_page()
        user_data = UserData(login="", password="wrong_password")
        app.login.auth(user_data)
        assert app.login.find_error_alert() in Login.ERROR_ALERTS

    @allure.title("Пользоаватель вводит пустое значение в поле логин")
    @allure.tag("негативный кейс")
    @testrail("C58")
    def test_auth_empty_login(self, app) -> None:
        """
        Шаги:
        1. Пользователь переходит на сайт
        2. Пользователь ничего не вводит в поле логин, очищает поле
        3. Пользователь НЕ трогает поле пароль (оно уже предзаполнено)
        4. Пользователь делает клик на кнопку "Войти"
        5. Проверяем наличие текста "Неверные данные пользователя (осталось 2 попытки)".
        """
        app.open_main_page()
        user_data = UserData(login=None, password="demo")
        app.login.clear_login_field()
        app.login.auth(user_data)
        assert app.login.find_error_alert() in Login.ERROR_ALERTS

    @allure.title("Пользователь вводит пустое значение в поле пароль")
    @allure.tag("негативный кейс")
    @testrail("C59")
    def test_auth_empty_password(self, app) -> None:
        """
        Шаги:
        1. Пользователь переходит на сайт
        2. Пользователь НЕ ничего не вводит в поле логин
        3. Пользователь очищает поле пароль
        4. Пользователь делает клик на кнопку "Войти"
        5. Проверяем наличие текста "Неверные данные пользователя".
        """
        app.open_main_page()
        user_data = UserData(login="", password=None)
        app.login.clear_password_field()
        app.login.auth(user_data)
        assert app.login.find_error_alert() in Login.ERROR_ALERTS

    @allure.title("Пользователь пытается войти с пустями полями логин и пароль")
    @allure.tag("негативный кейс")
    @testrail("C60")
    def test_auth_empty_login_password(self, app) -> None:
        """
        Шаги:
        1. Пользователь переходит на сайт
        2. Пользователь ничего не вводит в поле логин, очищает поле
        3. Пользователь ничего не вводит в поле пароль, очищает поле
        4. Пользователь делает клик на кнопку "Войти"
        5. Проверяем наличие текста "Неверные данные пользователя"
        """
        app.open_main_page()
        app.login.clear_login_field()
        app.login.clear_password_field()
        app.login.click_enter_auth()
        assert app.login.find_error_alert() in Login.ERROR_ALERTS

    @allure.title("Пользователь вводит невалидные данные в поле логин и пароль")
    @allure.tag("негативный кейс")
    @testrail("C73")
    @pytest.mark.parametrize(
        "login, password", [("0980", "6787"), ("data", "&^%%%"), ("___", " 8787  ")]
    )
    def test_auth_wrong_data(self, app, login, password) -> None:
        """
        Шаги:
        1. Пользователь переходит на сайт
        2. Пользователь ничего не вводит в поле логин, вводит некорректные данные
        3. Пользователь ничего не вводит в поле пароль, вводит некорректные данные
        4. Пользователь делает клик на кнопку "Войти"
        5. Проверяем наличие текста "Неверные данные пользователя"
        """
        app.open_main_page()
        app.login.clear_login_field()
        app.login.input_username(login)
        app.login.clear_password_field()
        app.login.input_pass(password)
        app.login.click_enter_auth()
        assert app.login.find_error_alert() in Login.ERROR_ALERTS

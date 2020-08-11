from model.login import UserData
from constants.login import Login


def test_auth(app):
    """
    Шаги:
    1. Пользователь переходит на сайт
    2. Пользоавтель делает клик на кнопку "Войти" (валидные данные уже заполнены по умолчанию)
    3. Пользователь закрывает системный алерт
    4. Пользователь делает клик на кнопку "Войти"
    5. Проверяем наличие кнопки "Обзор"
    """
    app.open_main_page()
    app.login.click_enter_auth()
    app.login.click_enter_sms()
    assert app.login.find_overview_button() == Login.SUCCESS


def test_auth_negative_login(app):
    """
    Шаги:
    1. Пользователь переходит на сайт
    2. Пользоавтель вводит любое значение в поле логин
    3. Пользователь НЕ трогает поле пароль (оно уже предзаполнено)
    4. Пользователь делает клик на кнопку "Войти"
    5. Проверяем наличие текста "Неверные данные пользователя (осталось 2 попытки)"
    """
    app.open_main_page()
    user_data = UserData(login='admin', password='demo')
    app.login.clear_login_field()
    app.login.auth(user_data)
    assert app.login.find_error_alert() in Login.ERROR_ALERTS


def test_auth_negative_password(app):
    """
    Шаги:
    1. Пользователь переходит на сайт
    2. Пользоавтель ничего не вводит в поле логин (поле уже предзаполнено по умолчанию)
    3. Пользователь вводит невалидное значение в поле "пароль"
    4. Пользователь делает клик на кнопку "Войти"
    5. Проверяем наличие текста "Неверные данные пользователя (осталось 2 попытки)"
    """
    app.open_main_page()
    user_data = UserData(login='', password='wrong_password')
    app.login.auth(user_data)
    assert app.login.find_error_alert() in Login.ERROR_ALERTS


def test_auth_empty_login(app):
    """
    Шаги:
    1. Пользователь переходит на сайт
    2. Пользователь ничего не вводит в поле логин, очищает поле
    3. Пользователь НЕ трогает поле пароль (оно уже предзаполнено)
    4. Пользователь делает клик на кнопку "Войти"
    5. Проверяем наличие текста "Неверные данные пользователя (осталось 2 попытки)"
    """
    app.open_main_page()
    user_data = UserData(login=None, password='demo')
    app.login.clear_login_field()
    app.login.auth(user_data)
    assert app.login.find_error_alert() in Login.ERROR_ALERTS


def test_auth_empty_password(app):
    """
    Шаги:
    1. Пользователь переходит на сайт
    2. Пользователь ничего не вводит в поле логин, очищает поле
    3. Пользователь НЕ трогает поле пароль (оно уже предзаполнено)
    4. Пользователь делает клик на кнопку "Войти"
    5. Проверяем наличие текста "Неверные данные пользователя"
    """
    app.open_main_page()
    user_data = UserData(login='', password=None)
    app.login.clear_password_field()
    app.login.auth(user_data)
    assert app.login.find_error_alert() in Login.ERROR_ALERTS


def test_auth_empty_login_password(app):
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

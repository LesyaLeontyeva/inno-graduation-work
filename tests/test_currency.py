"""Тесты на раздел Валюты."""
import allure
from pytest_testrail.plugin import testrail

from constants.currency import Currency


@allure.suite("Тесты на раздел Валюты")
class TestCurrency:
    @allure.title("Тест на успешный обмен валюты с данными по умолчанию")
    @allure.tag("позитивный кейс")
    @testrail("C69")
    def test_currency_exchange(self, authorization):
        """
        1. Пользователь авторизуется
        2. Кликает на кнопку Валюта
        3. Кликает на кнопку Подтвердить
        4. Вводит смс код
        5. Кликает на кнопку Подтвердить в блоке с смс кодом
        6. Видит сообщение о том, что обмен валюты успешно совершен
        """
        authorization.currency.click_on_currency_button()
        authorization.currency.click_on_submit_button_with_frame()
        authorization.currency.input_sms_code(code="0000")
        authorization.currency.click_on_confirm_button()
        assert Currency.SUCCESS_ALERT in authorization.currency.get_alert_text()

    @allure.title("Тест на обмен валюты с выбранным счетом списания")
    @allure.tag("позитивный кейс")
    @testrail("C70")
    def test_change_count_for_exchange(self, authorization):
        """
        1. Пользователь авторизуется
        2. Кликает на кнопку Валюта
        3. Выбирает счет списания
        4. Кликает на кнопку Подтвердить
        5. Вводит смс код
        6. Кликает на кнопку Подтвердить в блоке с смс кодом
        7. Видит сообщение о том, что обмен валюты успешно совершен
        """
        authorization.currency.click_on_currency_button()
        authorization.currency.choose_pound_account()
        authorization.currency.click_on_submit_button_no_frame()
        authorization.currency.input_sms_code(code="0000")
        authorization.currency.click_on_confirm_button()
        assert Currency.SUCCESS_ALERT in authorization.currency.get_alert_text()

    @allure.title("Тест с нулевой суммой списания")
    @allure.tag("негативный кейс")
    @testrail("C71")
    def test_currency_exchange_negative(self, authorization):
        """
        1. Пользователь авторизвался
        2. Кликает на кнопку Валюта
        3. Вводит сумму списания = 0
        4. Видит сообщение об ошибке
        """
        authorization.currency.click_on_currency_button()
        authorization.currency.input_amount(amount=0)
        assert authorization.currency.find_error_sign() is True

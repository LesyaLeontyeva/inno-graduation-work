"""Тесты на раздел Карты."""
import allure
from pytest_testrail.plugin import testrail

from constants.credit import Credit


@allure.suite("Тесты на раздел Кредит")
class TestCredit:
    @allure.title("Тест на полное погашение кредита")
    @allure.tag("позитивный кейс")
    @testrail("C14")
    def test_close_credit(self, app, authorization):
        """
        1. Пользователь авторизуется
        2. Кликает на кноку "Кредиты"
        3. Выбирает кредит в списке и кликает на него
        4. Кликает на кнопку "Закрыть"
        5. Выбирает офис
        6. Кликает на кнопку "Отправить"
        7. Кликает на кнопку "Подтвердить"
        8. Видит сообщение о том, что заявка отправлена
        """
        authorization.credit.click_on_credit_button()
        authorization.credit.click_on_credit()
        authorization.credit.click_on_close_credit_button()
        authorization.credit.choose_office()
        authorization.credit.submit_button()
        authorization.credit.confirm_button()
        assert Credit.SUCCESS_ALERT in authorization.credit.get_alert_text()

    @allure.title("Тест на частичное погашение кредита")
    @allure.tag("позитивный кейс")
    @testrail("C15")
    def test_partial_close_credit(self, app, authorization):
        """
         1. Пользователь авторизуется
         2. Кликает на кноку "Кредиты"
         3. Выбирает кредит и кликает на иконку "шестеренка"
         4. Выбирает из списка опций "Частичное погашение"
         5. Вводит сумму погашения
         6. Кликает на кнопку "Отправить"
         7. Кликает на кнопку "Подтвердить"
         8. Видит сообщение о том, что заявка отправлена
         """
        authorization.credit.click_on_credit_button()
        authorization.credit.click_on_option()
        authorization.credit.click_on_partial()
        authorization.credit.input_amount(amount=10000)
        authorization.credit.click_on_radiobutton()
        authorization.credit.click_on_checkbox()
        authorization.credit.submit_button()
        authorization.credit.confirm_button()
        assert Credit.SUCCESS_ALERT in authorization.credit.get_alert_text()

    @allure.title("Тест на получение кредитной истории")
    @allure.tag("позитивный кейс")
    @testrail("C16")
    def test_credit_history(self, app, authorization):
        """
         1. Пользователь авторизуется
         2. Кликает на кноку "Кредиты"
         3. Выбирает кредит и кликает на иконку "шестеренка"
         4. Выбирает из списка опций "Справка о кредитной истории"
         5. Выбирает офис
         6. Кликает на кнопку "Отправить"
         7. Кликает на кнопку "Подтвердить"
         8. Видит сообщение о том, что заявка отправлена
         """
        authorization.credit.click_on_credit_button()
        authorization.credit.click_on_option()
        authorization.credit.click_on_history()
        authorization.credit.choose_office()
        authorization.credit.submit_button()
        assert Credit.SUCCESS_ALERT in authorization.credit.get_alert_text()

"""Тесты на раздел Вклады."""
import allure
from pytest_testrail.plugin import testrail

from constants.deposits import Deposits


@allure.suite("Тесты на раздел Вклады")
class TestDeposit:
    @allure.title("Тест на успешное открытие вклада")
    @allure.tag("позитивный кейс")
    @testrail("C20")
    def test_open_deposit(self, app, authorization):
        """
        1. Пользователь авторизовывается
        2. Кликает на кнопку Вклады
        3. Кликает на кнопку Открыть вклад
        4. Кликает на кнопку Открыть вклад для выбранного вклада из списка
        5. Пользоавтель вводит сумму
        5. Кликает на кнопку Дальше
        6. Ставит чекбокс с Соглашением
        7. Кликает на кнопку Подтвердить
        8. Видит сообщение о том, что вклад открыт
        """
        authorization.deposits.click_on_deposit_button()
        authorization.deposits.click_on_open_deposit()
        authorization.deposits.click_on_first_deposit()
        authorization.deposits.enter_deposit_amount(amount=10000)
        authorization.deposits.click_submit_button()
        authorization.deposits.click_on_confirm_checkbox()
        authorization.deposits.click_on_confirm()
        assert Deposits.SUCCESS_ALERT in authorization.deposits.get_success_text()

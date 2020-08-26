"""Тесты на раздел Карты."""
import allure
from pytest_testrail.plugin import testrail

from constants.cards import Cards


@allure.suite("Тесты на раздел Карты")
class TestCards:
    @allure.title("Тест на успешный заказ карты")
    @allure.tag("позитивный кейс")
    @testrail("C9")
    def test_order_card(self, app, authorization):
        """
        1. Открываем главную страницу
        2. Кликаем на кнопку "Войти" в окне авторизации
        3. Кликаем на кнопку "Войти" в окне для ввода смс
        4. Кликаем на вкладку "Карты"
        5. Кликаю на кнопку "Заказать новую карту"
        6. Выбирает первую опацию "Повышенные бонусы ярко"
        7. Делаю клик на кнопку "Заказать"
        8. Ввожу сумму дохода ИЛИ Выбираю офис для выдачи карты
        9. Отмечаю три чекбоса ИЛИ кликаю на кнопку "Заказать" в диалоговом окне
        10. Кликаю на кнопку "Подтвердить" для кейса в блоке try
        11. Кликаю на кнопку "Подтвердить" с смс кодом для оброих блоков
        """

        authorization.cards.click_on_cards_button()
        authorization.cards.order_new_card()
        authorization.cards.choose_first_option()
        authorization.cards.order_chosen_card()
        authorization.cards.submit_order_card()
        assert authorization.cards.find_success_alert() == Cards.SUCCESS_ALERT

    @allure.title("Тест подключить смс оповещения к карте")
    @allure.tag("позитивный кейс")
    @testrail("C10")
    def test_connect_sms(self, app, authorization):
        """
        1. Открываем главную страницу
        2. Кликаем на кнопку "Войти" в окне авторизации
        3. Кликаем на кнопку "Войти" в окне для ввода смс
        4. Кликаем на вкладку "Карты"
        5. Кликаем на кнопку "SMS уведомления"
        6. Кликаем на кнопку "Подключить"
        7. Кликаем на кнопку "Подтвердить"
        """
        authorization.cards.click_on_cards_button()
        authorization.cards.sms_button()
        authorization.cards.connect_button()
        authorization.cards.submit()
        assert authorization.cards.find_success_alert() == Cards.CARD_ALERT

    @allure.title("Тест отключить смс оповещения на карте")
    @allure.tag("позитивный кейс")
    @testrail("C11")
    def test_delete_sms_connect(self, app, authorization):
        """
           1. Открываем главную страницу
           2. Кликаем на кнопку "Войти" в окне авторизации
           3. Кликаем на кнопку "Войти" в окне для ввода смс
           4. Кликаем на вкладку "Карты"
           5. Кликаем на кнопку "SMS уведомления"
           6. Кликаем на кнопку "Удалить"
           7. Кликаем на кнопку "Подтвердить"
           """

        authorization.cards.click_on_cards_button()
        authorization.cards.sms_button()
        authorization.cards.click_on_delete_sms()
        authorization.cards.submit()
        assert authorization.cards.find_success_alert() == Cards.SMS_DELETE_ALERT

    @allure.title("Тест подключить email оповещения к карте")
    @allure.tag("позитивный кейс")
    @testrail("C12")
    def test_connect_email(self, app, authorization):
        """
           1. Открываем главную страницу
           2. Кликаем на кнопку "Войти" в окне авторизации
           3. Кликаем на кнопку "Войти" в окне для ввода смс
           4. Кликаем на вкладку "Карты"
           5. Кликаем на кнопку "E-mail уведомления"
           6. Кликаем на радиобаттон "E-mail"
           7. Кликаем на кнопку "Подключить"
           7. Кликаем на кнопку "Подтвердить"
           """
        authorization.cards.click_on_cards_button()
        authorization.cards.click_on_email()
        authorization.cards.click_on_email_radiobutton()
        authorization.cards.click_on_email_connect()
        authorization.cards.submit()
        assert authorization.cards.find_success_alert() == Cards.CARD_ALERT

    @allure.title("Тест подключить к карте оплату в интернете")
    @allure.tag("позитивный кейс")
    @testrail("C13")
    def test_connect_pay_in_internet(self, app, authorization):
        """
           1. Открываем главную страницу
           2. Кликаем на кнопку "Войти" в окне авторизации
           3. Кликаем на кнопку "Войти" в окне для ввода смс
           4. Кликаем на вкладку "Оплата в интернете"
           5. Кликаем на кнопку "Подтвердить"
           """
        authorization.cards.click_on_cards_button()
        authorization.cards.click_on_pay_in_internet_button()
        authorization.cards.click_on_email_connect()
        authorization.cards.submit()
        assert authorization.cards.find_success_alert() == Cards.PAY_IN_INTERNET_ALERT

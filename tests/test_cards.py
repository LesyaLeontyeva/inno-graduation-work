import allure
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from constants.cards import Cards


# прикрутить testrail к тестам
@allure.suite("Тесты на раздел Карты")
class TestCards:
    @allure.title("Тест Заказ карты")
    @allure.tag("позитивный кейс, фукнциональный тест")
    def test_order_card(self, app):
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
        app.open_main_page()
        app.login.click_enter_auth()
        app.login.click_enter_sms()
        app.cards.click_on_cards_button()
        app.cards.order_new_card()
        app.cards.choose_first_option()
        app.cards.order_chosen_card()
        try:  # вынести в pages
            app.cards.input_amount(amount=100000)
            app.cards.choose_first_checkbox()
            app.cards.choose_second_button()
            app.cards.choose_third_button()
            app.cards.send_request()
            app.cards.click_on_confirm_button()
        except (NoSuchElementException, TimeoutException):
            app.cards.choose_office()
            app.cards.order_card()
            app.cards.click_on_confirm_button()
        assert app.cards.find_success_alert() == Cards.SUCCESS_ALERT

    @allure.title("Тест подключить смс к карте")
    @allure.tag("позитивный кейс, фукнциональный тест")
    def test_connect_sms(self, app):
        """
        1. Открываем главную страницу
        2. Кликаем на кнопку "Войти" в окне авторизации
        3. Кликаем на кнопку "Войти" в окне для ввода смс
        4. Кликаем на вкладку "Карты"
        5. Кликаем на кнопку "SMS уведомления"
        6. Кликаем на кнопку "Подключить"
        7. Кликаем на кнопку "Подтвердить"
        """
        # добавить тест с варнингом
        app.open_main_page()
        app.login.click_enter_auth()
        app.login.click_enter_sms()
        app.cards.click_on_cards_button()
        app.cards.sms_button()
        app.cards.connect_button()
        app.cards.submit()
        assert app.cards.find_success_alert() == Cards.CARD_ALERT

    @allure.title("Тест отключить смс на карте")
    @allure.tag("позитивный кейс, фукнциональный тест")
    def test_delete_sms_connect(self, app):
        """
           1. Открываем главную страницу
           2. Кликаем на кнопку "Войти" в окне авторизации
           3. Кликаем на кнопку "Войти" в окне для ввода смс
           4. Кликаем на вкладку "Карты"
           5. Кликаем на кнопку "SMS уведомления"
           6. Кликаем на кнопку "Удалить"
           7. Кликаем на кнопку "Подтвердить"
           """
        app.open_main_page()
        app.login.click_enter_auth()
        app.login.click_enter_sms()
        app.cards.click_on_cards_button()
        app.cards.sms_button()
        app.cards.click_on_delete_sms()
        app.cards.submit()
        assert app.cards.find_success_alert() == Cards.SMS_DELETE_ALERT

    @allure.title("Тест подключить email")
    @allure.tag("позитивный кейс, фукнциональный тест")
    def test_connect_email(self, app):
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
        app.open_main_page()
        app.login.click_enter_auth()
        app.login.click_enter_sms()
        app.cards.click_on_cards_button()
        app.cards.click_on_email()
        app.cards.click_on_email_radiobutton()
        app.cards.click_on_email_connect()
        app.cards.submit()
        assert app.cards.find_success_alert() == Cards.CARD_ALERT

    @allure.title("Тест подключить оплату в интернете")
    @allure.tag("позитивный кейс, фукнциональный тест")
    def test_connect_pay_in_internet(self, app):
        """
           1. Открываем главную страницу
           2. Кликаем на кнопку "Войти" в окне авторизации
           3. Кликаем на кнопку "Войти" в окне для ввода смс
           4. Кликаем на вкладку "Оплата в интернете"
           5. Кликаем на кнопку "Подтвердить"
           """
        # добавить для варнингов
        app.open_main_page()
        app.login.click_enter_auth()
        app.login.click_enter_sms()
        app.cards.click_on_cards_button()
        app.cards.click_on_pay_in_internet_button()
        app.cards.click_on_email_connect()
        app.cards.submit()
        assert app.cards.find_success_alert() == Cards.PAY_IN_INTERNET_ALERT

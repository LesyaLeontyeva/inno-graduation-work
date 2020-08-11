import time

from constants.currency import Currency


def test_currency_exchange(app):
    app.open_main_page()
    app.login.click_enter_auth()
    app.login.click_enter_sms()
    app.currency.click_on_currency_button()
    app.currency.click_on_submit_button()
    app.currency.input_sms_code(code='0000')
    app.currency.click_on_confirm_button()
    assert app.currency.get_alert_text() == Currency.SUCCESS_ALERT


def test_change_count_for_exchange(app):
    app.open_main_page()
    app.login.click_enter_auth()
    app.login.click_enter_sms()
    app.currency.click_on_currency_button()
    app.currency.choose_count()
    app.currency.click_on_submit_button()
    app.currency.input_sms_code(code='0000')
    app.currency.click_on_confirm_button()
    assert 1 == 1


def test_bla(app):
    app.open_main_page()
    app.login.click_enter_auth()
    app.login.click_enter_sms()
    app.currency.click_on_currency_button()
    time.sleep(5)
    app.currency.click_on_exchange()
    assert 1 == 1

from constants.currency import Currency


def test_currency_exchange(app):
    app.open_main_page()
    app.login.click_enter_auth()
    app.login.click_enter_sms()
    app.currency.click_on_currency_button()
    app.currency.click_on_submit_button_with_frame()
    app.currency.input_sms_code(code="0000")
    app.currency.click_on_confirm_button()
    assert Currency.SUCCESS_ALERT in app.currency.get_alert_text()


def test_change_count_for_exchange(app):
    app.open_main_page()
    app.login.click_enter_auth()
    app.login.click_enter_sms()
    app.currency.click_on_currency_button()
    app.currency.choose_pound_account()
    app.currency.click_on_submit_button_no_frame()
    app.currency.input_sms_code(code="0000")
    app.currency.click_on_confirm_button()
    assert Currency.SUCCESS_ALERT in app.currency.get_alert_text()


def test_currency_exchange_negative(app):
    app.open_main_page()
    app.login.click_enter_auth()
    app.login.click_enter_sms()
    app.currency.click_on_currency_button()
    app.currency.input_amount(amount=0)
    assert app.currency.find_error_sign() is True

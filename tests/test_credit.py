from constants.credit import Credit


class TestCredit:
    def test_close_credit(self, app):
        app.open_main_page()
        app.login.click_enter_auth()
        app.login.click_enter_sms()
        app.credit.click_on_credit_button()
        app.credit.click_on_credit()
        app.credit.click_on_close_credit_button()
        app.credit.choose_office()
        app.credit.submit_button()
        app.credit.confirm_button()
        assert Credit.SUCCESS_ALERT in app.credit.get_alert_text()

    def test_partial_close_credit(self, app):
        app.open_main_page()
        app.login.click_enter_auth()
        app.login.click_enter_sms()
        app.credit.click_on_credit_button()
        app.credit.click_on_option()
        app.credit.click_on_partial()
        app.credit.input_amount(amount=10000)
        app.credit.click_on_radiobutton()
        app.credit.click_on_checkbox()
        app.credit.submit_button()
        app.credit.confirm_button()
        assert Credit.SUCCESS_ALERT in app.credit.get_alert_text()

    def test_credit_history(self, app):
        app.open_main_page()
        app.login.click_enter_auth()
        app.login.click_enter_sms()
        app.credit.click_on_credit_button()
        app.credit.click_on_option()
        app.credit.click_on_history()
        app.credit.choose_office()
        app.credit.submit_button()
        assert Credit.SUCCESS_ALERT in app.credit.get_alert_text()

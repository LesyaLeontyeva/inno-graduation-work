from constants.deposits import Deposits


def test_open_deposit(app):
    app.open_main_page()
    app.login.click_enter_auth()
    app.login.click_enter_sms()
    app.deposits.click_on_deposit_button()
    app.deposits.click_on_open_deposit()
    app.deposits.click_on_first_deposit()
    app.deposits.enter_deposit_amount(amount=100000)
    app.deposits.click_submit_button()
    app.deposits.check_conditions()
    app.deposits.click_on_confirm()
    assert Deposits.SUCCESS_ALERT in app.deposits.get_success_text()

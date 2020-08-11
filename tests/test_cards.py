import time


def test_order_card(app):
    app.open_main_page()
    app.login.click_enter_auth()
    app.login.click_enter_sms()
    app.cards.click_on_cards_button()
    app.cards.order_new_card()
    app.cards.choose_first_option()
    app.cards.order_chosen_card()
    app.cards.input_amount(amount=100000)
    app.cards.choose_first_checkbox()
    app.cards.choose_second_button()
    app.cards.choose_third_button()
    time.sleep(6)
    app.cards.send_request()
    app.cards.confirm_request()
    assert 1 == 1

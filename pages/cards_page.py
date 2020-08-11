from locators.сards import CardsLocators


class CardsPage:
    def __init__(self, app):
        self.app = app

    def click_on_cards_button(self):
        return self.app.wd.find_element(*CardsLocators.CARDS_BUTTON).click()

    def order_new_card(self):
        return self.app.wd.find_element(*CardsLocators.OPEN_NEW_CARD_BUTTON).click()

    def choose_first_option(self):
        return self.app.wd.find_element(*CardsLocators.INCREASE_BONUS_CHECKBOX).click()

    def order_chosen_card(self):
        return self.app.wd.find_element(*CardsLocators.ORDER_BUTTON).click()

    def input_amount(self, amount):
        element = self.app.wd.find_element(*CardsLocators.AMOUNT_FIELD)
        element.send_keys(amount)

    def choose_first_checkbox(self):
        return self.app.wd.find_element(*CardsLocators.FIRST_CHECKBOX).click()

    def choose_second_button(self):
        return self.app.wd.find_element(*CardsLocators.SECOND_CHECKBOX).click()

    def choose_third_button(self):
        return self.app.wd.find_element(*CardsLocators.THIRD_CHECKBOX).click()

    def send_request(self):
        return self.app.wd.find_element(*CardsLocators.SEND_REQUEST).click()

    def confirm_request(self):
        return self.app.wd.find_element(*CardsLocators.SUBMIT_BUTTON).click()


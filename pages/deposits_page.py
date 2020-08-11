from locators.deposits import DepositsLocators


class DepositsPage:
    def __init__(self, app):
        self.app = app

    def click_on_deposit_button(self):
        return self.app.wd.find_element(*DepositsLocators.DEPOSITS_BUTTON).click()

    def click_on_open_deposit(self):
        return self.app.wd.find_element(*DepositsLocators.OPEN_DEPOSIT_BUTTON).click()

    def click_on_first_deposit(self):
        return self.app.wd.find_element(*DepositsLocators.OPEN_CHOSEN_DEPOSIT_BUTTON).click()

    def enter_deposit_amount(self, amount):
        element = self.app.wd.find_element(*DepositsLocators.AMOUNT_FIELD)
        element.send_keys(amount)

    def click_submit_button(self):
        return self.app.wd.find_element(*DepositsLocators.SUBMIT_BUTTON).click()

    def check_conditions(self):
        element = self.app.wd.find_element(*DepositsLocators.CONDITIONS_CHECKBOX)
        element.click()

    def click_on_confirm(self):
        return self.app.wd.find_element(*DepositsLocators.CONFIRM_BUTTON).click()


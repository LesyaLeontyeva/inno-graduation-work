from locators.currency import CurrencyLocators


class CurrencyPage:
    def __init__(self, app):
        self.app = app

    def click_on_currency_button(self):
        return self.app.wd.find_element(*CurrencyLocators.CURRENCY_BUTTON).click()

    def input_amount(self, amount: int) -> None:
        element = self.app.wd.find_element(*CurrencyLocators.INPUT_AMOUNT).click()
        element.send_keys(amount)

    def click_on_submit_button(self):
        return self.app.wd.find_element(*CurrencyLocators.SUBMIT_BUTTON).click()

    def input_sms_code(self, code) -> None:
        element = self.app.wd.find_element(*CurrencyLocators.SMS_CODE_INPUT)
        element.send_keys(code)

    def click_on_confirm_button(self) -> str:
        return self.app.wd.find_element(*CurrencyLocators.SMS_CONFIRM_BUTTON).click()

    def click_on_close_alert(self) -> str:
        return self.app.wd.find_element(*CurrencyLocators.CLOSE_ALERT_BUTTON).click()

    def get_alert_text(self) -> str:
        return self.app.wd.find_element(*CurrencyLocators.ALERT_BODY).text

    def choose_count(self):
        return self.app.wd.find_element(*CurrencyLocators.CHOSEN_ACCOUNT).click()

    def click_on_exchange(self):
        return self.app.wd.find_element(*CurrencyLocators.STOCK_EXCHANGE).click()

from selenium.common.exceptions import NoSuchWindowException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

from locators.credit import CreditLocators


class CreditPage:
    def __init__(self, app):
        self.app = app
        self.wait = WebDriverWait(self.app.wd, 10)

    def click_on_credit_button(self):
        return self.app.wd.find_element(*CreditLocators.CREDIT_BUTTON).click()

    def click_on_credit(self):
        self.wait.until(EC.element_to_be_clickable(CreditLocators.CREDIT_NUMBER))
        return self.app.wd.find_element(*CreditLocators.CREDIT_NUMBER).click()

    def click_on_close_credit_button(self):
        return self.app.wd.find_element(*CreditLocators.CLOSE_BUTTON).click()

    def choose_office(self):
        self.wait.until(EC.element_to_be_clickable(CreditLocators.CHOOSE_OFFICE))
        select = Select(self.app.wd.find_element(*CreditLocators.CHOOSE_OFFICE))
        select.select_by_value("001-010")

    def submit_button(self):
        self.wait.until(EC.element_to_be_clickable(CreditLocators.SEND_BUTTON))
        return self.app.wd.find_element(*CreditLocators.SEND_BUTTON).click()

    def confirm_button(self):
        self.wait.until(
            EC.frame_to_be_available_and_switch_to_it(CreditLocators.CONFIRMATION_FRAME)
        )
        try:
            return self.app.wd.find_element(*CreditLocators.SUBMIT_BUTTON).click()
        except NoSuchWindowException:
            self.wait.until(EC.element_to_be_clickable(CreditLocators.SUBMIT_BUTTON))
            return self.app.wd.find_element(*CreditLocators.SUBMIT_BUTTON).click()

    def get_alert_text(self):
        self.app.wd.switch_to.default_content()
        try:
            self.wait.until(
                EC.visibility_of_element_located(CreditLocators.SUCCESS_ALERT)
            )
            return self.app.wd.find_element(*CreditLocators.SUCCESS_ALERT).text
        except NoSuchElementException:
            self.wait.until(
                EC.visibility_of_element_located(CreditLocators.SUCCESS_ALERT)
            )
            return self.app.wd.find_element(*CreditLocators.SUCCESS_ALERT).text

    # new

    def click_on_option(self):
        return self.app.wd.find_element(*CreditLocators.OPTION_BUTTON).click()

    def click_on_partial(self):
        return self.app.wd.find_element(*CreditLocators.REQUEST_BUTTON).click()

    def input_amount(self, amount):
        self.wait.until(EC.element_to_be_clickable(CreditLocators.INPUT_AMOUNT))
        self.app.wd.find_element(*CreditLocators.INPUT_AMOUNT).send_keys(amount)

    def click_on_radiobutton(self):
        self.wait.until(EC.element_to_be_clickable(CreditLocators.CHOOSE_RADIOBUTTON))
        return self.app.wd.find_element(*CreditLocators.CHOOSE_RADIOBUTTON).click()

    def click_on_checkbox(self):
        self.wait.until(EC.element_to_be_clickable(CreditLocators.CHECKBOX))
        return self.app.wd.find_element(*CreditLocators.CHECKBOX).click()

    def click_on_history(self):
        return self.app.wd.find_element(*CreditLocators.HISTORY_BUTTON).click()

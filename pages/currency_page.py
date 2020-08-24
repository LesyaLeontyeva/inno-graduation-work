from typing import Any

from selenium.common.exceptions import (
    NoSuchWindowException,
    ElementClickInterceptedException,
    NoSuchElementException,
)
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.currency import CurrencyLocators
from locators.сards import CardsLocators
from selenium.webdriver.support.ui import Select


class CurrencyPage:
    def __init__(self, app):
        self.app = app
        self.wait = WebDriverWait(self.app.wd, 10)

    def click_on_currency_button(self):
        return self.app.wd.find_element(*CurrencyLocators.CURRENCY_BUTTON).click()

    def input_amount(self, amount: int) -> None:
        element = self.app.wd.find_element(*CurrencyLocators.INPUT_AMOUNT).click()
        element.send_keys(amount)

    def click_on_submit_button(self) -> Any:
        self.wait.until(
            EC.frame_to_be_available_and_switch_to_it(CurrencyLocators.FRAME_XPATH)
        )
        try:
            return self.app.wd.find_element(*CurrencyLocators.SUBMIT_BUTTON).click()
        except ElementClickInterceptedException:
            self.wait.until(EC.element_to_be_clickable(CurrencyLocators.SUBMIT_BUTTON))
            return self.app.wd.find_element(*CurrencyLocators.SUBMIT_BUTTON).click()

    def input_sms_code(self, code) -> None:
        self.wait.until(
            EC.frame_to_be_available_and_switch_to_it(CurrencyLocators.FRAME_CONFIRM)
        )
        try:
            element = self.app.wd.find_element(*CurrencyLocators.SMS_CODE_INPUT)
            element.send_keys(code)
        except NoSuchWindowException:
            self.wait.until(EC.element_to_be_clickable(CurrencyLocators.SMS_CODE_INPUT))
            element = self.app.wd.find_element(*CurrencyLocators.SMS_CODE_INPUT)
            element.send_keys(code)

    def click_on_confirm_button(self) -> Any:
        return self.app.wd.find_element(*CurrencyLocators.SMS_CONFIRM_BUTTON).click()

    def click_on_close_alert(self) -> Any:
        return self.app.wd.find_element(*CurrencyLocators.CLOSE_ALERT_BUTTON).click()

    def get_alert_text(self) -> str:
        self.wait.until(
            EC.frame_to_be_available_and_switch_to_it(CurrencyLocators.FRAME_XPATH)
        )
        try:
            return self.app.wd.find_element(*CurrencyLocators.SUCCESS_ALERT).getText()
        except NoSuchElementException:
            self.wait.until(
                EC.visibility_of_element_located(CurrencyLocators.SUCCESS_ALERT)
            )
            return self.app.wd.find_element(*CurrencyLocators.SUCCESS_ALERT).getText()

    def choose_account(self) -> None:
        select = Select(self.app.wd.find_element(*CardsLocators.CHOOSE_OFFICE_SELECTOR))
        select.select_by_id("debit_acc_simple_40817978154747254911")

    def click_on_exchange(self) -> Any:
        return self.app.wd.find_element(*CurrencyLocators.STOCK_EXCHANGE).click()

    # def switch(self):
    #     iframe = self.app.wd.find_element(*CurrencyLocators.FRAME_XPATH)
    #     self.app.wd.switch_to.frame(iframe)
    #
    # def switch_confirm(self):
    #     self.app.wd.switch_to_frame('confirmIframe97')

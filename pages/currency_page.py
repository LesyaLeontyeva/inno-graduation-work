from typing import Any

from selenium.common.exceptions import (
    NoSuchWindowException,
    ElementClickInterceptedException,
    NoSuchElementException,
    StaleElementReferenceException,
)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.currency import CurrencyLocators


class CurrencyPage:
    def __init__(self, app):
        self.app = app
        self.wait = WebDriverWait(self.app.wd, 10)

    def click_on_currency_button(self):
        return self.app.wd.find_element(*CurrencyLocators.CURRENCY_BUTTON).click()

    def input_amount(self, amount: int) -> Any:
        self.wait.until(
            EC.frame_to_be_available_and_switch_to_it(CurrencyLocators.FRAME_XPATH)
        )
        try:
            element = self.app.wd.find_element(*CurrencyLocators.INPUT_AMOUNT)
            element.send_keys(amount)
        except StaleElementReferenceException:
            self.wait.until(EC.element_to_be_clickable(CurrencyLocators.INPUT_AMOUNT))
            element = self.app.wd.find_element(*CurrencyLocators.INPUT_AMOUNT)
            element.send_keys(amount)

    def click_on_submit_button_with_frame(self) -> Any:
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
            self.wait.until(
                EC.visibility_of_element_located(CurrencyLocators.SUCCESS_ALERT)
            )
            return self.app.wd.find_element(*CurrencyLocators.SUCCESS_ALERT).text
        except NoSuchElementException:
            self.wait.until(
                EC.visibility_of_element_located(CurrencyLocators.SUCCESS_ALERT)
            )
            return self.app.wd.find_element(*CurrencyLocators.SUCCESS_ALERT).text

    def choose_pound_account(self) -> None:
        self.wait.until(
            EC.frame_to_be_available_and_switch_to_it(CurrencyLocators.FRAME_XPATH)
        )
        self.wait.until(EC.element_to_be_clickable(CurrencyLocators.ACCOUNT_SELECTOR))
        self.app.wd.find_element(*CurrencyLocators.ACCOUNT_SELECTOR).click()
        return self.app.wd.find_element(*CurrencyLocators.ACCOUNT_POUND_OPTION).click()

    def choose_rub_account(self) -> None:
        self.wait.until(
            EC.frame_to_be_available_and_switch_to_it(CurrencyLocators.FRAME_XPATH)
        )
        self.wait.until(EC.element_to_be_clickable(CurrencyLocators.ACCOUNT_SELECTOR))
        self.app.wd.find_element(*CurrencyLocators.ACCOUNT_SELECTOR).click()
        return self.app.wd.find_element(*CurrencyLocators.ACCOUNT_RUB_OPTION).click()

    def click_on_exchange(self) -> Any:
        return self.app.wd.find_element(*CurrencyLocators.STOCK_EXCHANGE).click()

    # def switch(self):
    #     iframe = self.app.wd.find_element(*CurrencyLocators.FRAME_XPATH)
    #     self.app.wd.switch_to.frame(iframe)
    #
    # def switch_confirm(self):
    #     self.app.wd.switch_to_frame('confirmIframe97')

    def click_on_submit_button_no_frame(self) -> Any:
        self.wait.until(EC.element_to_be_clickable(CurrencyLocators.SUBMIT_BUTTON))
        return self.app.wd.find_element(*CurrencyLocators.SUBMIT_BUTTON).click()

    def find_error_sign(self) -> bool:
        self.wait.until(EC.visibility_of_element_located(CurrencyLocators.ERROR_SIGN))
        return self.app.wd.find_element(*CurrencyLocators.ERROR_SIGN).is_displayed()

import time
from typing import Any

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.deposits import DepositsLocators


class DepositsPage:
    def __init__(self, app):
        self.app = app
        self.wait = WebDriverWait(self.app.wd, 10)

    def click_on_deposit_button(self) -> Any:
        self.wait.until(EC.element_to_be_clickable(DepositsLocators.DEPOSITS_BUTTON))
        return self.app.wd.find_element(*DepositsLocators.DEPOSITS_BUTTON).click()

    def click_on_open_deposit(self) -> Any:
        self.wait.until(
            EC.element_to_be_clickable(DepositsLocators.OPEN_DEPOSIT_BUTTON)
        )
        return self.app.wd.find_element(*DepositsLocators.OPEN_DEPOSIT_BUTTON).click()

    def click_on_first_deposit(self) -> Any:
        self.wait.until(
            EC.element_to_be_clickable(DepositsLocators.OPEN_CHOSEN_DEPOSIT_BUTTON)
        )
        return self.app.wd.find_element(
            *DepositsLocators.OPEN_CHOSEN_DEPOSIT_BUTTON
        ).click()

    def enter_deposit_amount(self, amount) -> Any:
        self.wait.until(EC.element_to_be_clickable(DepositsLocators.AMOUNT_FIELD))
        return self.app.wd.find_element(*DepositsLocators.AMOUNT_FIELD).send_keys(
            amount
        )

    def click_submit_button(self) -> Any:
        time.sleep(10)  # попробуй сделать цикл try except
        self.wait.until(EC.element_to_be_clickable(DepositsLocators.SUBMIT_BUTTON))
        return self.app.wd.find_element(*DepositsLocators.SUBMIT_BUTTON).click()

    def check_conditions(self) -> Any:
        self.wait.until(
            EC.element_to_be_clickable(DepositsLocators.CONDITIONS_CHECKBOX)
        )
        element = self.app.wd.find_element(*DepositsLocators.CONDITIONS_CHECKBOX)
        element.click()

    def click_on_confirm_checkbox(self) -> Any:
        self.wait.until(EC.element_to_be_clickable(DepositsLocators.TEST_PATH))
        return self.app.wd.find_element(*DepositsLocators.TEST_PATH).click()

    def click_on_confirm(self) -> Any:
        self.wait.until(EC.element_to_be_clickable(DepositsLocators.CONFIRM_BUTTON))
        return self.app.wd.find_element(*DepositsLocators.CONFIRM_BUTTON).click()

    def get_success_text(self) -> str:
        self.wait.until(
            EC.visibility_of_element_located(DepositsLocators.SUCCESS_ALERT)
        )
        return self.app.wd.find_element(*DepositsLocators.SUCCESS_ALERT).text

    def click_on_option_button(self) -> Any:
        self.wait.until(EC.element_to_be_clickable(DepositsLocators.CHOSEN_DEPOSIT))
        return self.app.wd.find_element(*DepositsLocators.CHOSEN_DEPOSIT).click()

    def close_deposit_button(self) -> Any:
        self.wait.until(
            EC.element_to_be_clickable(DepositsLocators.CLOSE_DEPOSIT_BUTTON)
        )
        return self.app.wd.find_element(*DepositsLocators.CLOSE_DEPOSIT_BUTTON).click()

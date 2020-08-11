from selenium.webdriver.common.by import By


class DepositsLocators:
    DEPOSITS_BUTTON = (By.ID, 'deposits-index')
    OPEN_DEPOSIT_BUTTON = (By.ID, 'btn-show-rates')
    OPEN_CHOSEN_DEPOSIT_BUTTON = (By.XPATH, '//tr[1]//td[7]//a[1]')
    AMOUNT_FIELD = (By.ID, 'amount')
    # SUBMIT_BUTTON = (By.ID, "submit-button")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Дальше']")
    CONDITIONS_CHECKBOX = (By.CLASS_NAME, 'short-content')
    CONFIRM_BUTTON = (By.ID, 'confirm')
    SUCCESS_ALERT = (By.XPATH, "//div[@class='alert alert-success']")

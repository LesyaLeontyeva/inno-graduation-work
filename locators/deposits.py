from selenium.webdriver.common.by import By


class DepositsLocators:
    DEPOSITS_BUTTON = (By.ID, "deposits-index")
    OPEN_DEPOSIT_BUTTON = (By.ID, "btn-show-rates")
    OPEN_CHOSEN_DEPOSIT_BUTTON = (By.XPATH, "//tr[1]//td[7]//a[1]")
    AMOUNT_FIELD = (By.ID, "amount")
    SUBMIT_BUTTON = (By.XPATH, "(//button[@class='btn btn-primary'])[2]")
    CONDITIONS_CHECKBOX = (By.NAME, "condition.newDepositConditions")
    CONFIRM_BUTTON = (By.XPATH, "//button[@id='confirm']")
    TEST_PATH = (By.XPATH, "//input[@name='condition.newDepositConditions']")
    SUCCESS_ALERT = (By.XPATH, "//div[@class='alert alert-success']")
    CHOSEN_DEPOSIT = (By.XPATH, "//button[@class='btn btn-mini dropdown-toggle']")
    CLOSE_DEPOSIT_BUTTON = (By.XPATH, "//ul[@class='dropdown-menu']//li//a")
    FRAME = (By.XPATH, "//iframe[@id='confirmation-frame']")
    RATE = (By.ID, "interest-rate")

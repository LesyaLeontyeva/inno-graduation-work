from selenium.webdriver.common.by import By


class CreditLocators:
    CREDIT_NUMBER = (By.XPATH, "//span[contains(text(),'9802222-99L')]")
    CLOSE_BUTTON = (By.ID, "repayment-button")
    CHOOSE_OFFICE = (By.ID, "message-branch")
    SEND_BUTTON = (By.ID, "send-button")
    CONFIRMATION_FRAME = (By.ID, "confirmation-frame")
    SUBMIT_BUTTON = (By.ID, "confirm")
    CREDIT_BUTTON = (By.ID, "loans")
    SUCCESS_ALERT = (By.XPATH, "//div[@class='alert alert-success']")
    OPTION_BUTTON = (
        By.XPATH,
        "//table[@id='credit-card-loans']"
        "//button[@class='btn btn-mini dropdown-toggle']",
    )
    REQUEST_BUTTON = (By.XPATH, "//table[@id='credit-card-loans']//li[1]//a[1]")
    INPUT_AMOUNT = (By.ID, "loanPartialRepaymentAmount")
    CHOOSE_RADIOBUTTON = (By.XPATH, "//input[@value='reduceDuration']")
    CHECKBOX = (By.XPATH, "//input[@name='message.partialRepaymentConditions']")
    HISTORY_BUTTON = (By.XPATH, "//table[@id='credit-card-loans']//li[7]//a[1]")

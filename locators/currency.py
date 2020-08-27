from selenium.webdriver.common.by import By


class CurrencyLocators:
    CURRENCY_BUTTON = (By.ID, "externaltraderoom-index")
    SUBMIT_BUTTON = (
        By.XPATH,
        "//button[@class='btn btn-primary standart pull-left ng-binding']",
    )
    SMS_CODE_INPUT = (By.ID, "otp-input")
    SMS_CONFIRM_BUTTON = (By.ID, "confirm")
    SUCCESS_ALERT = (By.XPATH, "//div[contains(@class,'notice-text muted')]")
    CLOSE_ALERT_BUTTON = (By.CLASS_NAME, "close")
    INPUT_AMOUNT = (By.ID, "debit")
    ALERT_BODY = (By.CLASS_NAME, "panel-body")
    STOCK_EXCHANGE = (By.XPATH, "//a[@id='bankRateExtendedTab']")
    FRAME_XPATH = (By.XPATH, "//iframe[@class='full-page']")
    FRAME_CONFIRM = (By.XPATH, "//iframe[@id='confirmIframe97']")
    ACCOUNT_SELECTOR = (By.ID, "debit_acc_simple")
    ACCOUNT_POUND_OPTION = (By.ID, "debit_acc_simple_40817826154747273294")
    ACCOUNT_RUB_OPTION = (By.ID, "debit_acc_simple_40817810154747260987")
    ERROR_SIGN = (By.ID, "simple-widget-question")
    POUND_TEXT = (By.XPATH, "//div[contains(text(),'40817826154747273294')]")

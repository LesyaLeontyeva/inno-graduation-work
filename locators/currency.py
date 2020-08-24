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

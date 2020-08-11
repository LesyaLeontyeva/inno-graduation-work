from selenium.webdriver.common.by import By


class CurrencyLocators:
    CURRENCY_BUTTON = (By.ID, "externaltraderoom-index")
    # SUBMIT_BUTTON = (By.XPATH, "//button[contains(@class,'btn btn-primary')]")
    # SUBMIT_BUTTON = (By.XPATH, "//button[@ng-disabled='!canCreateDeal()']")
    # SUBMIT_BUTTON = (By.XPATH, "//button[contains(@class,'btn btn-primary')]")
    SUBMIT_BUTTON = (By.XPATH, "//button[@class='btn btn-primary standart pull-left ng-binding']")
    SMS_CODE_INPUT = (By.ID, "otp-input")
    SMS_CONFIRM_BUTTON = (By.ID, "confirm")
    SUCCESS_ALERT = (By.CLASS_NAME, "notice-text muted m-b-2 ng-binding")
    CLOSE_ALERT_BUTTON = (By.CLASS_NAME, "close")
    INPUT_AMOUNT = (By.ID, "debit")
    ALERT_BODY = (By.CLASS_NAME, "panel-body")
    CHOSEN_ACCOUNT = (By.XPATH, "//span[@ng-bind-html='a | balanceFormatter:isForward'])[2]")
    # STOCK_EXCHANGE = (By.ID, "bankRateExtendedTab")
    STOCK_EXCHANGE = (By.XPATH, "//a[@id='bankRateExtendedTab']")
    # STOCK_EXCHANGE = (By.XPATH, "(//a[@class='ng-binding'])[2]")

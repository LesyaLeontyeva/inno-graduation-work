from selenium.webdriver.common.by import By


class LoginLocators:
    LOGIN_INPUT = (By.NAME, 'username')
    PASSWORD_INPUT = (By.NAME, 'password')
    ENTER_LOGIN_BUTTON = (By.ID, 'login-button')
    ENTER_SMS_BUTTON = (By.ID, 'login-otp-button')
    OVERVIEW_BUTTON = (By.ID, 'bank-overview')
    ERROR_ALERT = (By.XPATH, '//*[@class="alert alert-error"]')

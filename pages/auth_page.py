from locators.login import LoginLocators
from model.login import UserData


class LoginPage:
    def __init__(self, app):
        self.app = app

    def input_login(self) -> str:
        return self.app.wd.find_element(*LoginLocators.LOGIN_INPUT)

    def input_password(self) -> str:
        return self.app.wd.find_element(*LoginLocators.PASSWORD_INPUT)

    def click_enter_auth(self) -> None:
        self.app.wd.find_element(*LoginLocators.ENTER_LOGIN_BUTTON).click()

    def click_enter_sms(self) -> None:
        self.app.wd.find_element(*LoginLocators.ENTER_SMS_BUTTON).click()

    def auth(self, user_data: UserData) -> None:
        if user_data.login is not None:
            self.input_login().send_keys(user_data.login)
        if user_data.password is not None:
            self.input_password().send_keys(user_data.password)
        self.click_enter_auth()

    def find_overview_button(self) -> str:
        return self.app.wd.find_element(*LoginLocators.OVERVIEW_BUTTON).text

    def find_error_alert(self) -> str:
        return self.app.wd.find_element(*LoginLocators.ERROR_ALERT).text

    def clear_login_field(self) -> None:
        self.app.wd.find_element(*LoginLocators.LOGIN_INPUT).clear()

    def clear_password_field(self) -> None:
        self.app.wd.find_element(*LoginLocators.PASSWORD_INPUT).clear()

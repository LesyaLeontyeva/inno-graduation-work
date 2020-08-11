from selenium.webdriver.common.by import By


class CardsLocators:
    CARDS_BUTTON = (By.ID, 'cards-overview-index')
    OPEN_NEW_CARD_BUTTON = (
        By.XPATH, "//a[@href='/cards/application'] ")
    INCREASE_BONUS_CHECKBOX = (By.NAME, 'increasedBonusPoints')
    ORDER_BUTTON = (By.XPATH, "//button[@data-ref='85']")
    AMOUNT_FIELD = (By.XPATH, "//input[@name='application.monthlyIncome']")
    FIRST_CHECKBOX = (By.NAME, 'condition.creditHistory')
    SECOND_CHECKBOX = (By.NAME, 'condition.personalDataProcessing')
    THIRD_CHECKBOX = (By.NAME, 'condition.mobileSubscriberDataProcessing')
    SEND_REQUEST = (By.ID, 'inspect')
    SUBMIT_BUTTON = (By.ID, 'confirm')
    SUCCESS_ALERT = (By.XPATH, "//div[@class='alert alert-success']")

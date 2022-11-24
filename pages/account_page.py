from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class Locators:

# далее идет описание локаторов для элементов страницы

    ACCOUNT_LOGOUT_BUTTON = (By.ID, "logout-btn")
    ACCOUNT_LK_BUTTON = (By.ID, "lk-btn")

class AccountHelper(BasePage):
    def logout(self):
        return self.find_element(Locators.ACCOUNT_LOGOUT_BUTTON).click

    def lk_is_visible(self):
        return self.is_visible(Locators.ACCOUNT_LK_BUTTON)
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class Locators:

# далее идет описание локаторов для элементов страницы

    # AGREEMENT_TITLE = (By.XPATH, '//*[@id="title"]/h1[1]')
    AGREEMENT_TITLE = (By.XPATH, "//*[text()[contains(., 'Публичная оферта')]]")

class AgreementHelper(BasePage):

    def agreement_is_visible(self):
        return self.is_visible(Locators.AGREEMENT_TITLE)
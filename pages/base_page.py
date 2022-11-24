from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://b2c.passport.rt.ru"


    def go_to_site(self):
        return self.driver.get(self.base_url)


    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f"not find{locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator), message=f"not find{locator}")

    def move_to_element(self, locator):
        element = self.find_element(locator)
        return ActionChains(self.driver).move_to_element(element).perform()

    def is_visible(self, locator):
            """ Check is the element visible or not. """

            element = self.find_element(locator)

            if element:
                return element.is_displayed()

            return False

    def switch_new(self):
        self.driver.switch_to.window(self.driver.window_handles[1])


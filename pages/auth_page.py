import config
from pages.base_page import BasePage
from selenium.webdriver.common.by import By



class Locators:

    # далее идет описание локаторов для элементов страницы

    AUTH_TITLE = (By.XPATH, "//*[text()[contains(., 'Авторизация')]]")
    AUTH_SWITCH_PHONE = (By.ID, 't-btn-tab-phone')
    AUTH_SWITCH_EMAIL = (By.ID, 't-btn-tab-mail')
    AUTH_SWITCH_LOGIN = (By.ID, 't-btn-tab-login')
    AUTH_SWITCH_LS = (By.ID, 't-btn-tab-ls')
    AUTH_USERNAME_FIELD = (By.ID, 'username')
    AUTH_USERNAME_PHONE = (By.XPATH, "//*[text()[contains(., 'Мобильный телефон')]]" )
    AUTH_USERNAME_EMAIL = (By.XPATH, "//*[text()[contains(., 'Электронная почта')]]")
    AUTH_USERNAME_LOGIN = (By.XPATH, "//*[text()[contains(., 'Логин')]]")
    AUTH_USERNAME_LS = (By.XPATH, "//*[text()[contains(., 'Лицевой счёт')]]")
    AUTH_PASS_FIELD = (By.ID, 'password')
    AUTH_PASS = (By.XPATH, "//*[text()[contains(., 'Пароль')]]" )
    AUTH_BTN = (By.ID, 'kc-login')
    AUTH_LINK_FORGOT_PASS = (By.ID, 'forgot_password')
    AUTH_FORGOT_PASS_RESET_BACK_BTN = (By.ID, 'reset-back')
    AUTH_FORGOT_PASS_TITLE = (By.XPATH, "//*[text()[contains(., 'Восстановление пароля')]]")
    AUTH_LINK_UA1 = (By.XPATH, "//*[text()[contains(., 'пользовательского соглашения')]]")
    AUTH_LINK_VK = (By.ID, 'oidc_vk')
    AUTH_LINK_OK = (By.ID, 'oidc_ok')
    AUTH_LINK_MAIL = (By.ID, 'oidc_mail')
    AUTH_LINK_GOOGLE = (By.ID, 'oidc_google')
    AUTH_LINK_YA = (By.ID, 'oidc_ya')
    AUTH_LINK_REG = (By.ID, 'kc-register')
    AUTH_REG = (By.XPATH, "//*[text()[contains(., 'Регистрация')]]")
    AUTH_LINK_CHAT = (By.XPATH,  "//*[text()[contains(., 'Чат')]]")
    AUTH_CHAT_BTN = (By.ID, 'widget_sendPrechat')
    AUTH_LINK_COOKIE = (By.XPATH, "//*[text()[contains(., 'Cookies')]]")
    AUTH_COOKIE = (By.XPATH, "//*[text()[contains(., 'Cookie')]]")
    AUTH_LINK_CP = (By.XPATH, "//*[text()[contains(., 'Политикой конфиденциальности')]]")
    AUTH_LINK_UA2 = (By.XPATH, "//*[text()[contains(., 'Пользовательским соглашением')]]")
    AUTH_LINK_SUPPORT_PHONE = (By.XPATH, "//*[text()[contains(., '8 800 100 0 800')]]")
    AUTH_LINK_VIBER = (By.XPATH, '//*[@id="widget_bar"]/div[3]/a[1]')
    AUTH_LINK_TELEGA = (By.XPATH, '//*[@id="widget_bar"]/div[3]/a[2]')
    AUTH_CHECKBOX = (By.XPATH, "//*[text()[contains(., 'Запомнить меня')]]")
    AUTH_ERROR_LOGIN_FORM = (By.XPATH, '//*[@id="form-error-message"]')


class AuthHelper(BasePage):
    def enter_username(self, username):
        username_field = self.find_element(Locators.AUTH_USERNAME_FIELD)
        username_field.click()
        username_field.send_keys(username)
        return username_field

    def enter_password(self, password):
        password_field = self.find_element(Locators.AUTH_PASS_FIELD)
        password_field.click()
        password_field.send_keys(password)
        return password_field


    def click_on_auth_button(self):
        return self.find_element(Locators.AUTH_BTN, time=5).click()

    def click_on_phone_swich(self):
        return self.find_element(Locators.AUTH_SWITCH_PHONE, time=5).click()

    def click_on_email_swich(self):
        return self.find_element(Locators.AUTH_SWITCH_EMAIL, time=5).click()

    def click_on_login_swich(self):
        return self.find_element(Locators.AUTH_SWITCH_LOGIN, time=5).click()

    def click_on_ls_swich(self):
        return self.find_element(Locators.AUTH_SWITCH_LS, time=5).click()

    def click_on_forgot_pass_link(self):
        return self.find_element(Locators.AUTH_LINK_FORGOT_PASS, time=5).click()

    def click_on_user_agreement_link_1(self):
        return self.find_element(Locators.AUTH_LINK_UA1, time=5).click()

    def click_on_user_agreement_link_2(self):
        return self.find_element(Locators.AUTH_LINK_UA2, time=5).click()

    def click_on_vk_link(self):
        return self.find_element(Locators.AUTH_LINK_VK, time=5).click()

    def click_on_ok_link(self):
        return self.find_element(Locators.AUTH_LINK_OK, time=5).click()

    def click_on_mail_link(self):
        return self.find_element(Locators.AUTH_LINK_MAIL, time=5).click()

    def click_on_google_link(self):
        return self.find_element(Locators.AUTH_LINK_GOOGLE, time=5).click()

    def click_on_ya_link(self):
        return self.find_element(Locators.AUTH_LINK_YA, time=5).click()

    def click_on_reg_link(self):
        return self.find_element(Locators.AUTH_LINK_REG, time=5).click()

    def click_on_cookie_link(self):
        return self.find_element(Locators.AUTH_LINK_COOKIE, time=5).click()

    def click_on_CP_link(self):
        return self.find_element(Locators.AUTH_LINK_CP, time=5).click()

    def click_on_support_phone_link(self):
        return self.find_element(Locators.AUTH_LINK_SUPPORT_PHONE, time=5).click()

    def click_on_chat_link(self):
        return self.find_element(Locators.AUTH_LINK_CHAT, time=15).click()

    def click_on_viber_link(self):
        self.move_to_element(Locators.AUTH_LINK_CHAT)
        return self.find_element(Locators.AUTH_LINK_VIBER, time=10).click()

    def click_on_telega_link(self):
        self.move_to_element(Locators.AUTH_LINK_CHAT)
        return self.find_element(Locators.AUTH_LINK_TELEGA, time=10).click()

    def click_on_checkbox(self):
        return self.find_element(Locators.AUTH_CHECKBOX, time=10).click()

    def click_on_reset(self):
        return self.find_element(Locators.AUTH_FORGOT_PASS_RESET_BACK_BTN, time=10).click()

    def error_is_visible(self):
        return self.is_visible(Locators.AUTH_ERROR_LOGIN_FORM)

    def cookie_is_visible(self):
        return self.is_visible(Locators.AUTH_COOKIE)

    def mobile_is_visible(self):
        return self.is_visible(Locators.AUTH_USERNAME_PHONE)

    def email_is_visible(self):
        return self.is_visible(Locators.AUTH_USERNAME_EMAIL)

    def login_is_visible(self):
        return self.is_visible(Locators.AUTH_USERNAME_LOGIN)

    def ls_is_visible(self):
        return self.is_visible(Locators.AUTH_USERNAME_LS)

    def forgot_pass_is_visible(self):
        return self.is_visible(Locators.AUTH_FORGOT_PASS_TITLE)

    def auth_is_visible(self):
        return self.is_visible(Locators.AUTH_TITLE)

    def chat_is_visible(self):
        return self.is_visible(Locators.AUTH_CHAT_BTN)

    def reg_is_visible(self):
        return self.is_visible(Locators.AUTH_REG)















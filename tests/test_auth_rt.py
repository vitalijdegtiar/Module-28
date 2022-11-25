# pytest -v --driver Chrome --driver-path chromedriver.exe  test_auth_rt.py
import allure
import time

import pytest

import config

from pages.auth_page import AuthHelper

from pages.account_page import AccountHelper

from pages.agreement_page import AgreementHelper


# икстура для составления красивого отчета
# @allure.story('test')
# @allure.feature('test ya')
# @allure.step('test searh')
def test_auth_phone(browser):
    auth_main_page = AuthHelper(browser)
    auth_main_page.go_to_site()
    auth_main_page.click_on_phone_swich()
    assert auth_main_page.mobile_is_visible()
    # auth_main_page.enter_username("Hello")
    # auth_main_page.click_on_auth_button()
    # elements = ya_search_page.check_nave_bar()
    # assert "Картинки" and "Видео" in elements
def test_auth_email(browser):
    auth_main_page = AuthHelper(browser)
    auth_main_page.go_to_site()
    auth_main_page.click_on_email_swich()
    assert auth_main_page.email_is_visible()


def test_auth_login(browser):
    auth_main_page = AuthHelper(browser)
    auth_main_page.go_to_site()
    auth_main_page.click_on_login_swich()
    assert auth_main_page.login_is_visible()


def test_auth_ls(browser):
    auth_main_page = AuthHelper(browser)
    auth_main_page.go_to_site()
    auth_main_page.click_on_ls_swich()
    assert auth_main_page.ls_is_visible()


def test_forgot_pass(browser):
    auth_main_page = AuthHelper(browser)
    auth_main_page.go_to_site()
    auth_main_page.click_on_forgot_pass_link()
    assert auth_main_page.forgot_pass_is_visible()

def test_forgot_pass_reset(browser):
    auth_main_page = AuthHelper(browser)
    auth_main_page.go_to_site()
    auth_main_page.click_on_forgot_pass_link()
    auth_main_page.click_on_reset()
    assert auth_main_page.auth_is_visible()


def test_user_agreement_1(browser):
    auth_main_page = AuthHelper(browser)
    agreement_page = AgreementHelper(browser)
    auth_main_page.go_to_site()
    auth_main_page.click_on_user_agreement_link_1()
    auth_main_page.switch_new()
    assert agreement_page.agreement_is_visible()

def test_user_agreement_2(browser):
    auth_main_page = AuthHelper(browser)
    agreement_page = AgreementHelper(browser)
    auth_main_page.go_to_site()
    auth_main_page.click_on_user_agreement_link_2()
    auth_main_page.switch_new()
    assert agreement_page.agreement_is_visible()


def test_chat(browser):
    auth_main_page = AuthHelper(browser)
    auth_main_page.go_to_site()
    auth_main_page.click_on_chat_link()
    assert auth_main_page.chat_is_visible()


def test_viber(browser):
    auth_main_page = AuthHelper(browser)
    auth_main_page.go_to_site()
    auth_main_page.click_on_viber_link()
    time.sleep(5)
    auth_main_page.driver.save_screenshot('viber_page.png')


def test_telega(browser):
    auth_main_page = AuthHelper(browser)
    auth_main_page.go_to_site()
    auth_main_page.click_on_telega_link()
    auth_main_page.driver.save_screenshot('telega_page.png')


def test_support_phone(browser):
    auth_main_page = AuthHelper(browser)
    auth_main_page.go_to_site()
    auth_main_page.click_on_support_phone_link()
    time.sleep(5)
    auth_main_page.driver.save_screenshot('Support_phone.png')

def test_registration(browser):
    auth_main_page = AuthHelper(browser)
    auth_main_page.go_to_site()
    auth_main_page.click_on_reg_link()
    assert auth_main_page.reg_is_visible()

def test_vk(browser):
    auth_main_page = AuthHelper(browser)
    auth_main_page.go_to_site()
    auth_main_page.click_on_vk_link()
    auth_main_page.driver.save_screenshot('VK_page.png')

def test_ok(browser):
    auth_main_page = AuthHelper(browser)
    auth_main_page.go_to_site()
    auth_main_page.click_on_ok_link()
    auth_main_page.driver.save_screenshot('OK_page.png')

def test_mail(browser):
    auth_main_page = AuthHelper(browser)
    auth_main_page.go_to_site()
    auth_main_page.click_on_mail_link()
    auth_main_page.driver.save_screenshot('Mail_page.png')

def test_google(browser):
    auth_main_page = AuthHelper(browser)
    auth_main_page.go_to_site()
    auth_main_page.click_on_google_link()
    auth_main_page.driver.save_screenshot('Google_page.png')

def test_ya(browser):
    auth_main_page = AuthHelper(browser)
    auth_main_page.go_to_site()
    auth_main_page.click_on_ya_link()
    auth_main_page.driver.save_screenshot('Ya_page.png')

def test_cookie(browser):
    auth_main_page = AuthHelper(browser)
    auth_main_page.go_to_site()
    auth_main_page.click_on_cookie_link()
    assert auth_main_page.cookie_is_visible()

def test_cp(browser):
    auth_main_page = AuthHelper(browser)
    agreement_page = AgreementHelper(browser)
    auth_main_page.go_to_site()
    auth_main_page.click_on_CP_link()
    auth_main_page.switch_new()
    assert agreement_page.agreement_is_visible()

def test_positive_auth_email(browser):
    auth_main_page = AuthHelper(browser)
    account_page = AccountHelper(browser)
    auth_main_page.go_to_site()
    auth_main_page.click_on_email_swich()
    auth_main_page.enter_username(config.positive_email)
    auth_main_page.enter_password(config.positive_password)
    auth_main_page.click_on_checkbox()
    auth_main_page.click_on_auth_button()
    assert account_page.lk_is_visible()
    time.sleep(5)
    account_page.logout()
    assert auth_main_page.auth_is_visible()



def test_negative_auth_email(browser):
    auth_main_page = AuthHelper(browser)
    auth_main_page.go_to_site()
    auth_main_page.click_on_email_swich()
    auth_main_page.enter_username(config.negative_email)
    auth_main_page.enter_password(config.positive_password)
    auth_main_page.click_on_checkbox()
    auth_main_page.click_on_auth_button()
    assert auth_main_page.error_is_visible()

def test_positive_auth_phone(browser):
    auth_main_page = AuthHelper(browser)
    account_page = AccountHelper(browser)
    auth_main_page.go_to_site()
    auth_main_page.click_on_phone_swich()
    auth_main_page.enter_username(config.positive_phone)
    auth_main_page.enter_password(config.positive_password)
    auth_main_page.click_on_checkbox()
    auth_main_page.click_on_auth_button()
    assert account_page.lk_is_visible()
    account_page.logout()
    assert auth_main_page.auth_is_visible()

def test_negative_auth_phone(browser):
    auth_main_page = AuthHelper(browser)
    auth_main_page.go_to_site()
    auth_main_page.click_on_email_swich()
    auth_main_page.enter_username(config.negative_phone)
    auth_main_page.enter_password(config.positive_password)
    auth_main_page.click_on_checkbox()
    auth_main_page.click_on_auth_button()
    assert auth_main_page.error_is_visible()

# pytest -v --driver Chrome --driver-path chromedriver.exe  test_auth_rt.py
import allure
import time

import pytest

import config

from pages.auth_page import AuthHelper

from pages.account_page import AccountHelper

from pages.agreement_page import AgreementHelper



def test_auth_phone(browser):
    auth_main_page = AuthHelper(browser)
    auth_main_page.go_to_site()
    auth_main_page.click_on_phone_swich()
    assert auth_main_page.mobile_is_visible()


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

def test_close_current_window(browser):
    auth_main_page = AuthHelper(browser)
    auth_main_page.close_current_window()

def test_user_agreement_2(browser):
    auth_main_page = AuthHelper(browser)
    agreement_page = AgreementHelper(browser)
    auth_main_page.go_to_site()
    auth_main_page.click_on_user_agreement_link_2()
    auth_main_page.switch_new()
    assert agreement_page.agreement_is_visible()

def test_close_current_window_2(browser):
    auth_main_page = AuthHelper(browser)
    auth_main_page.close_current_window()

def test_viber(browser):
    auth_main_page = AuthHelper(browser)
    auth_main_page.go_to_site()
    auth_main_page.click_on_viber_link()
    auth_main_page.switch_new()
    auth_main_page.driver.save_screenshot('viber_page.png')
    auth_main_page.close_current_window()

def test_telega(browser):
    auth_main_page = AuthHelper(browser)
    auth_main_page.go_to_site()
    auth_main_page.click_on_telega_link()
    auth_main_page.switch_new()
    auth_main_page.driver.save_screenshot('telega_page.png')
    auth_main_page.close_current_window()


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

def test_return_to_wnd_before_3(browser):
    auth_main_page = AuthHelper(browser)
    auth_main_page.close_current_window()

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

def test_logout(browser):
    auth_main_page = AuthHelper(browser)
    account_page = AccountHelper(browser)
    auth_main_page.go_to_site()
    account_page.logout()
    assert auth_main_page.auth_is_visible()

def test_negative_auth_login(browser):
    auth_main_page = AuthHelper(browser)
    auth_main_page.go_to_site()
    auth_main_page.click_on_login_swich()
    auth_main_page.enter_username(config.negative_login)
    auth_main_page.enter_password(config.positive_password)
    auth_main_page.click_on_checkbox()
    auth_main_page.click_on_auth_button()
    assert auth_main_page.error_is_visible()

def test_positive_logout(browser):
    auth_main_page = AuthHelper(browser)
    account_page = AccountHelper(browser)
    auth_main_page.go_to_site()
    auth_main_page.click_on_email_swich()
    auth_main_page.enter_username(config.positive_email)
    auth_main_page.enter_password(config.positive_password)
    auth_main_page.click_on_checkbox()
    auth_main_page.click_on_auth_button()
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

def test_logout_1(browser):
    auth_main_page = AuthHelper(browser)
    account_page = AccountHelper(browser)
    auth_main_page.go_to_site()
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

def test_negative_auth_ls(browser):
    auth_main_page = AuthHelper(browser)
    auth_main_page.go_to_site()
    auth_main_page.click_on_ls_swich()
    auth_main_page.enter_username(config.negative_ls)
    auth_main_page.enter_password(config.positive_password)
    auth_main_page.click_on_checkbox()
    auth_main_page.click_on_auth_button()
    assert auth_main_page.error_is_visible()

def test_chat(browser):
    auth_main_page = AuthHelper(browser)
    auth_main_page.go_to_site()
    auth_main_page.click_on_chat_link()
    assert auth_main_page.chat_is_visible()

# def test_close_chat(browser):
#     auth_main_page = AuthHelper(browser)
#     # auth_main_page.go_to_site()
#     # auth_main_page.click_on_chat_link()
#     time.sleep(5)
#     # auth_main_page.click_on_chat_btn()
#     time.sleep(5)
#     auth_main_page.click_on_close_chat_btn()
#     time.sleep(5)
#     assert auth_main_page.chat_is_visible()
#
# def test_support_phone(browser):
#     auth_main_page = AuthHelper(browser)
#     auth_main_page.go_to_site()
#     auth_main_page.click_on_support_phone_link()
#     time.sleep(5)
#     auth_main_page.driver.save_screenshot('Support_phone.png')
#     browser.escape()
#     time.sleep(5)
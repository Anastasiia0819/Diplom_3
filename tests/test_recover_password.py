import pytest
from selenium import webdriver
from src.config import Config
import allure
from locators.login_page_locators import LoginPageLocators
from locators.reset_password_page_locators import ResetPasswordPageLocators
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage
import time
from selenium.webdriver.support import expected_conditions


class TestRecoverPassword:
    @allure.title("Восстановление пароля")
    def test_recover_password(self, driver, create_and_delete_user):
        user_data = create_and_delete_user["user_data"]

        login_page = LoginPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)
        reset_password_page = ResetPasswordPage(driver)

        login_page.open_login_page()

        #проверка открытия login страницы
        current_url = login_page.get_current_url()
        expected_url = Config.login_url
        assert current_url == expected_url
        login_page.wait_recover_password_button()

        login_page.click_recover_password_button()
        assert forgot_password_page.get_current_url() == Config.forgot_password_url

        forgot_password_page.wait_title_recover_password()
        forgot_password_page.wait_recover_button_active()
        forgot_password_page.set_email_in_field(user_data["email"])
        forgot_password_page.click_recover_button()
        reset_password_page.wait_save_button()
        assert reset_password_page.get_current_url() == Config.reset_password_url
        reset_password_page.click_show_password_button()
        reset_password_page.wait_show_password_button_activ()
        element = reset_password_page.find_field_password_active()
        assert 'text' in element.get_attribute("type"), "Поле не подсветилось"





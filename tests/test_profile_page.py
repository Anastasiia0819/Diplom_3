import pytest
from selenium import webdriver
from src.config import Config
import allure
from locators.main_page_locators import MainPageLocators
from locators.profile_page_locators import ProfilePageLocators
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
import time
from selenium.webdriver.support import expected_conditions


class TestProfilePage:
    @allure.title("Переход на страницу Профиля")
    def test_open_profile_page(self, driver, create_and_delete_user, login):
        profile_page = ProfilePage(driver)
        main_page = MainPage(driver)
        main_page.wait_personal_account_button()
        main_page.click_personal_account_button()
        profile_page.wait_active_save_button()
        assert profile_page.get_current_url() == Config.profile_url

    @allure.title("Переход на страницу История заказов")
    def test_open_order_history_page(self, driver, create_and_delete_user, login):
        profile_page = ProfilePage(driver)
        profile_page.open_profile_page()
        assert profile_page.get_current_url() == Config.profile_url
        profile_page.wait_active_save_button()
        profile_page.click_history_order_button()
        profile_page.wait_history_order_button_active()
        active_button = profile_page.find_history_order_page_active()
        assert active_button is not None, "Элемент не выделился после клика"
        assert 'Account_link_active' in active_button.get_attribute("class"), "Элемент не выделился после клика"

    @allure.title("Выход из аккаунта")
    def test_logout(self, driver, create_and_delete_user, login):
        profile_page = ProfilePage(driver)
        profile_page.open_profile_page()
        assert profile_page.get_current_url() == Config.profile_url
        profile_page.wait_logout_button()
        profile_page.click_logout_button()
        assert profile_page.get_current_url() == Config.login_url


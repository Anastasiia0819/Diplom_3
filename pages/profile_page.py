from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.chrome.webdriver import WebDriver
import pytest
from locators.login_page_locators import LoginPageLocators
from locators.profile_page_locators import ProfilePageLocators
from selenium.webdriver.support.wait import WebDriverWait
import allure
from pages.base_page import BasePage
from src.config import Config


class ProfilePage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    #Открытие страницы
    @allure.step('open profile page')
    def open_profile_page(self):
        self.navigate(Config.profile_url)

    def get_current_url(self):
        return self.get_current_url_base()

    #ожидание активной кнопки Сохранить
    def wait_active_save_button(self):
        self.wait_for_element_visible(ProfilePageLocators.save_button)
        self.wait_element_to_be_clickable(ProfilePageLocators.save_button)

    @allure.step('Клик на кнопку История заказов')
    def click_history_order_button(self):
        self.click_element(ProfilePageLocators.history_orders_button)

    #ожидание выделения кнопки История заказов
    def wait_history_order_button_active(self):
        self.wait_for_element_visible(ProfilePageLocators.history_orders_button_active)

    #найти элемент выделения кнопки История заказов
    @allure.step('Вкладка "История заказов" активна')
    def find_history_order_page_active(self):
        return self.find_element(ProfilePageLocators.history_orders_button_active)

    #ожидание кнопки Выход из аккаунта
    def wait_logout_button(self):
        self.wait_for_element_visible(ProfilePageLocators.logout_button)
        self.wait_element_to_be_clickable(ProfilePageLocators.logout_button)

    @allure.step('Выход из аккаунта')
    def click_logout_button(self):
        self.click_element(ProfilePageLocators.logout_button)



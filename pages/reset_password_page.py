from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.chrome.webdriver import WebDriver
import pytest
from locators.reset_password_page_locators import ResetPasswordPageLocators
from selenium.webdriver.support.wait import WebDriverWait
import allure
from pages.base_page import BasePage
from src.config import Config


class ResetPasswordPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    #Открытие главной страницы
    @allure.step('open reset-password page')
    def open_main_page(self):
        self.navigate(Config.URL)

    def get_current_url(self):
        return self.get_current_url_base()

    #ожидание кнопки Сохранить
    def wait_save_button(self):
        self.wait_for_element_visible(ResetPasswordPageLocators.save_button)
        self.wait_element_to_be_clickable(ResetPasswordPageLocators.save_button)

    #клик по кнопке показать/скрыть пароль
    @allure.step("клик по кнопке показать/скрыть пароль")
    def click_show_password_button(self):
        self.click_element(ResetPasswordPageLocators.show_password_button)

    #ожидание подсвечивания поля ввода нового пароля
    @allure.step("подсвечиваниe поля ввода нового пароля")
    def wait_show_password_button_activ(self):
        self.wait_for_element_visible(ResetPasswordPageLocators.show_password_button_activ)

    @allure.step("найти подсвеченный элемент")
    def find_field_password_active(self):
        return self.find_element(ResetPasswordPageLocators.show_password_button_activ)



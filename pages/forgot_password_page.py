from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.chrome.webdriver import WebDriver
import pytest
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure
from pages.base_page import BasePage
from src.config import Config


class ForgotPasswordPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    #Открытие главной страницы
    @allure.step('open forgot-password page')
    def open_main_page(self):
        self.navigate(Config.URL)

    def get_current_url(self):
        return self.get_current_url_base()

    #ожидание заголовка "Восстановить пароль"
    def wait_title_recover_password(self):
        self.wait_for_element_visible(ForgotPasswordPageLocators.title_recover_password)

    #ожидание кнопки Восстановить
    def wait_recover_button_active(self):
        self.wait_for_element_visible(ForgotPasswordPageLocators.recover_button)
        self.wait_element_to_be_clickable(ForgotPasswordPageLocators.recover_button)

    #ввод в поле почты
    @allure.step("Ввод почты в поле")
    def set_email_in_field(self, email):
        self.enter_text(ForgotPasswordPageLocators.send_email_field, email)

    @allure.step("клик на кнопку 'восстановить'")
    def click_recover_button(self):
        self.click_element(ForgotPasswordPageLocators.recover_button)




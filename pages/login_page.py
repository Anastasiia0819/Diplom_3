"""
Восстановление пароля
- переход на страницу восстановления пароля по кнопке «Восстановить пароль»,
- ввод почты и клик по кнопке «Восстановить»,
- клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.
https://stellarburgers.nomoreparties.site/login
"""

from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.chrome.webdriver import WebDriver
import pytest
from locators.login_page_locators import LoginPageLocators
from selenium.webdriver.support.wait import WebDriverWait
import allure
from pages.base_page import BasePage
from src.config import Config


class LoginPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    #Открытие главной страницы
    @allure.step('open login page')
    def open_login_page(self):
        self.navigate(f"{Config.URL}login")

    def get_current_url(self):
        return self.get_current_url_base()

    #ожидание активной кнопки "восстановить пароль"
    def wait_recover_password_button(self):
        self.wait_for_element_visible(LoginPageLocators.recover_password_button)
        self.wait_element_to_be_clickable(LoginPageLocators.recover_password_button)

    @allure.step('клик на кнопку "восставить пароль"')
    def click_recover_password_button(self):
        self.click_element(LoginPageLocators.recover_password_button)





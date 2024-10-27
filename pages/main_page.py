from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.chrome.webdriver import WebDriver
import pytest
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.wait import WebDriverWait
import allure
from pages.base_page import BasePage
from src.config import Config


class MainPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    #Открытие главной страницы
    @allure.step('open main page')
    def open_login_page(self):
        self.navigate(Config.URL)

    def get_current_url(self):
        return self.get_current_url_base()

    #ожидание кнопки Личный кабинет
    def wait_personal_account_button(self):
        self.wait_for_element_visible(MainPageLocators.personal_account_button)
        self.wait_element_to_be_clickable(MainPageLocators.personal_account_button)

    # клик на кнопку Личный кабинет
    def click_personal_account_button(self):
        self.click_element(MainPageLocators.personal_account_button)

    #ожидание страницы с бургерами
    def wait_burgers_page(self):
        self.wait_for_elements_visible(MainPageLocators.burgers_page)

from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.chrome.webdriver import WebDriver
import pytest
from locators.main_page_locators import MainPageLocators
from locators.main_page_locators import ConstructorLocators
from selenium.webdriver.support.wait import WebDriverWait
import allure
from pages.base_page import BasePage
from src.config import Config
from selenium.common.exceptions import TimeoutException


class MainPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    #Открытие главной страницы
    @allure.step('open main page')
    def open_main_page(self):
        self.navigate(Config.URL)

    def get_current_url(self):
        return self.get_current_url_base()

    #ожидание кнопки Личный кабинет
    def wait_personal_account_button(self):
        self.wait_for_element_visible(MainPageLocators.personal_account_button)
        self.wait_element_to_be_clickable(MainPageLocators.personal_account_button)

    # клик на кнопку Личный кабинет
    @allure.step('Клик на Личный кабинет')
    def click_personal_account_button(self):
        self.wait_for_element_visible(MainPageLocators.personal_account_button)
        self.wait_element_to_be_clickable(MainPageLocators.personal_account_button)
        self.click_element(MainPageLocators.personal_account_button)

    # клик на кнопку Конструктор
    @allure.step('Клик на кнопку Конструктор')
    def click_constructor_button(self):
        self.click_element(MainPageLocators.constructor_button)

    #ожидание страницы с бургерами
    def wait_burgers_page(self):
        self.wait_for_elements_visible(MainPageLocators.burgers_page)

    # клик на кнопку Лента заказов
    @allure.step('Клик на кнопку Лента заказов')
    def click_order_feed_button(self):
        self.click_element(MainPageLocators.order_feed_button)

    @allure.step('Клик на иконку булки')
    def click_ingredient_bulka(self):
        self.click_element(ConstructorLocators.ingredient_bulka)

    #найти элемент булки
    def find_ingredient_bulka(self):
        return self.find_element(ConstructorLocators.ingredient_bulka)

    #ожидание открытия модалки с описанием ингридиента
    def wait_modal_page_ingredient(self):
        self.wait_for_element_visible(ConstructorLocators.open_modal_page_ingredient)

    @allure.step('Открылось модальное окно с описнаием ингридиента')
    def find_open_modal_page_ingredient(self):
        return self.find_element(ConstructorLocators.open_modal_page_ingredient)

    @allure.step('Кликнуть на закрыть в модальном окне')
    def click_close_button(self):
        self.click_element(ConstructorLocators.close_button)

    #проверка, ожидания что окно закрылось
    def wait_modal_disappears(self):
        try:
            self.wait_for_element_invisible(ConstructorLocators.open_modal_page_ingredient)
            return True
        except TimeoutException:
            return False

    #найти элемент корзины
    def find_basket(self):
        return self.find_element(ConstructorLocators.basket)

    def find_counter_0(self):
        return self.find_element(ConstructorLocators.counter_0)

    def find_counter_2(self):
        return self.find_element(ConstructorLocators.counter_2)

    @allure.step('Кликнуть на Оформить заказ')
    def click_made_order_button(self):
        self.click_element(MainPageLocators.offered_button)

    #ожидание модального окна
    def wait_modal_order(self):
        self.wait_for_element_visible(MainPageLocators.modal_page_order)

    #найти элемент номер заказа
    def find_number_order(self):
        return self.find_element(MainPageLocators.number_order)

# Ожидание обновления номера заказа
    def wait_for_order_number_to_update(self, initial_order_number):
        order_number_element = self.find_number_order()  # Найдите элемент с номером заказа
        self.wait_for_number_change(order_number_element, initial_order_number)


from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.chrome.webdriver import WebDriver
import pytest
from locators.feed_page_locators import FeedOrderPageLocators
from pages.history_order_page import HistoryOrderPage
from selenium.webdriver.support.wait import WebDriverWait
import allure
from pages.base_page import BasePage
from src.config import Config


class FeedPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    #Открытие главной страницы
    @allure.step('open main page')
    def open_feed_page(self):
        self.navigate(Config.order_feed_url)

    def get_current_url(self):
        return self.get_current_url_base()

    # ожидание заголовка лента заказов
    def wait_title(self):
        self.wait_for_element_visible(FeedOrderPageLocators.title_feed_order)

    @allure.step('Клик на кнопку Конструктор')
    def click_constructor_button(self):
        self.click_element(FeedOrderPageLocators.constructor_button)

    @allure.step('Клик на карточку заказа')
    def click_card_order(self):
        self.click_element(FeedOrderPageLocators.first_card_order)

    #ожидание открытия модального окна карточки заказа
    def wait_modal_page_order(self):
        self.wait_for_element_visible(FeedOrderPageLocators.modal_page_order)

    @allure.step('Клик на карточку заказа')
    def find_modal_page_order(self):
        return self.find_element(FeedOrderPageLocators.modal_page_order)

    @allure.step('Найти номер заказа из Истории заказа пользователя')
    def find_numbers_order_in_card_order(self):
        return self.find_element(FeedOrderPageLocators.numbers_order_in_card_order)

    @allure.step('при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def find_counter_done_all_time(self):
        return self.find_element(FeedOrderPageLocators.counter_done_all_time)

    def wait_for_order_number_to_update_done_all_tim(self, initial_order_number):
        order_number_element = self.find_counter_done_all_time  # Найдите элемент с номером заказа
        self.wait_for_number_change(order_number_element, initial_order_number)

    @allure.step('при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def find_counter_done_today(self):
        return self.find_element(FeedOrderPageLocators.counter_done_today)

    # Ожидание обновления номера заказа
    def wait_for_order_number_to_update_done_today(self, initial_order_number):
        order_number_element = self.find_counter_done_today()  # Найдите элемент с номером заказа
        self.wait_for_number_change(order_number_element, initial_order_number)

    @allure.step('после оформления заказа его номер появляется в разделе В работе')
    def find_numbers_order_in_work(self):
        return self.find_element(FeedOrderPageLocators.number_order_in_work).text


from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.chrome.webdriver import WebDriver
import pytest
from locators.history_order_page_locators import HistoryOrderPageLocators
from selenium.webdriver.support.wait import WebDriverWait
import allure
from pages.base_page import BasePage
from src.config import Config


class HistoryOrderPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def get_current_url(self):
        return self.get_current_url_base()

    #ожидание загрузки карточке заказов
    def wait_list_order(self):
        self.wait_for_element_visible(HistoryOrderPageLocators.list_card_order)

    #скролл до последней карточки списка
    def scroll_last_card(self):
        last_card = self.find_element(HistoryOrderPageLocators.last_card)
        self.scroll(last_card)
        self.wait_for_elements_visible(HistoryOrderPageLocators.last_card)
        self.wait_element_to_be_clickable(HistoryOrderPageLocators.last_card)

    @allure.step('Найти номер последнего заказа')
    def find_number_last_order(self):
        return self.find_element(HistoryOrderPageLocators.number_last_order_user).text

    @allure.step('Клик на кнопку Лента заказов')
    def click_feed_order_button(self):
        self.click_element(HistoryOrderPageLocators.order_feed_button)


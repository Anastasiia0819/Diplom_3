import pytest
from selenium import webdriver
from src.config import Config
import allure
from locators.main_page_locators import MainPageLocators
from locators.main_page_locators import ConstructorLocators
from locators.feed_page_locators import FeedOrderPageLocators
from pages.main_page import MainPage
from pages.feed_page import FeedPage
from selenium.webdriver import ActionChains


class TestMadeOrder:
    @allure.title("Информация о ингредиенте")
    def test_open_and_close_modal_about_ingredient(self, driver, create_and_delete_user, login):
        main_page = MainPage(driver)
        main_page.wait_burgers_page()
        main_page.click_ingredient_bulka()
        main_page.wait_modal_page_ingredient()
        open_modal = main_page.find_open_modal_page_ingredient()
        assert open_modal.is_displayed(),  "Модальное окно с описанием ингредиента не открылось"
        main_page.click_close_button()
        main_page.wait_modal_disappears()
        assert main_page.wait_modal_disappears(), "Модальное окно не закрылось"

    @allure.title("Добавление ингредиента в корзину")
    def test_add_ingredient_in_basket(self, driver, create_and_delete_user, login):
        main_page = MainPage(driver)
        main_page.wait_burgers_page()
        ingredient = main_page.find_ingredient_bulka()
        basket = main_page.find_basket()
        actions = ActionChains(driver)
        actions.drag_and_drop(ingredient, basket).perform()
        counter = main_page.find_counter_2()
        assert counter.is_displayed()

    @allure.title("Оформление заказа")
    def test_made_order(self, driver, create_and_delete_user, login):
        main_page = MainPage(driver)
        main_page.wait_burgers_page()
        main_page.click_made_order_button()
        main_page.wait_modal_order()
        number_order_text = main_page.find_number_order().text
        number_order = main_page.find_number_order()
        assert number_order_text is not None
        assert number_order.is_displayed(), "Номер заказа не отображается в модальном окне"




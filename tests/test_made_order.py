import pytest
from selenium import webdriver
import allure
from pages.main_page import MainPage
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

        #перенос ингредиента в корзину
        ingredient = main_page.find_ingredient_bulka()
        basket = main_page.find_basket()
        actions = ActionChains(driver)
        actions.drag_and_drop(ingredient, basket).perform()
        counter = main_page.find_counter_2()
        assert counter.is_displayed()

        #клик на Оформить заказ
        main_page.click_made_order_button()

        #ожидание модальное окно заказа
        main_page.wait_modal_order()

        # При открытии модалки ожидаем, что номер заказа равен 9999
        order_number_static = main_page.find_number_order()
        initial_order_number = "9999"
        assert order_number_static.text == initial_order_number, "Номер заказа не отображается как '9999' при открытии"

        #ожидание актуального номера заказа, отличного от initial_order_number
        main_page.wait_for_order_number_to_update(initial_order_number)

        #Проверка, что номер заказа изменился с статичного значения
        updated_order_number = order_number_static.text
        assert updated_order_number != initial_order_number, "Номер заказа не обновился на актуальный"

        number_order = main_page.find_number_order()
        assert updated_order_number is not None
        assert number_order.is_displayed(), "Номер заказа не отображается в модальном окне"




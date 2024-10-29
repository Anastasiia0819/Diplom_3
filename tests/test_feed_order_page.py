import pytest
from selenium import webdriver
from src.config import Config
import allure
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.feed_page import FeedPage
from pages.history_order_page import HistoryOrderPage
import time


class TestFeedOrderPage:
    @allure.title("Карточка заказа")
    def test_open_modal_page_order(self, driver, create_and_delete_user, login):
        feed_page = FeedPage(driver)
        feed_page.open_feed_page()
        time.sleep(3)
        assert feed_page.get_current_url() == Config.order_feed_url
        feed_page.click_card_order()
        feed_page.wait_modal_page_order()
        modal_card_order = feed_page.find_modal_page_order()
        assert modal_card_order.is_displayed(), "Модальное окно с деталями заказа не открылось"

    @allure.title('Заказ из раздела «История заказов» отображается в «Лента заказов»')
    def test_show_order_user_in_feed_page(self, driver, create_and_delete_user, login, make_order):
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        history_order = HistoryOrderPage(driver)
        feed_page = FeedPage(driver)

        assert login is not None, "Авторизация не выполнена"
        number_order = make_order()

        main_page.wait_burgers_page()
        main_page.wait_personal_account_button()
        main_page.click_personal_account_button()
        profile_page.wait_active_save_button()
        assert profile_page.get_current_url() == Config.profile_url

        profile_page.click_history_order_button()
        time.sleep(3)
        assert history_order.get_current_url() == Config.history_order_url

        history_order.wait_list_order()
        history_order.scroll_last_card()
        time.sleep(3)

        #найти актуальный номер заказа
        number_order_actual = history_order.find_number_last_order()
        assert number_order_actual is not None, "Номер последнего заказа не найден в Истории заказов"

        #перейти на страницу Лента заказов
        history_order.click_feed_order_button()
        feed_page.wait_title()
        assert feed_page.get_current_url() == Config.order_feed_url

        #найти полученный заказ и проверить, что они одинаковые
        number_order_feed_order = feed_page.find_numbers_order_in_card_order().text
        assert number_order_actual == number_order_feed_order, "Номер заказа в Ленте заказов не совпадает с номером из Истории заказов"

    @allure.title('Проверка, что после оформления заказа его номер появляется в разделе В работе')
    def test_number_order_show_in_work(self, driver, create_and_delete_user, login, make_order):
        feed_page = FeedPage(driver)
        main_page = MainPage(driver)
        number_order = make_order()

        main_page.wait_burgers_page()
        main_page.click_order_feed_button()
        feed_page.wait_title()
        assert feed_page.get_current_url() == Config.order_feed_url

        number_order_in_work = feed_page.find_numbers_order_in_work().lstrip("0") #удалить лидирующий 0
        assert number_order_in_work == number_order

    @allure.title('Проверка, что при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_after_create_new_order_counter_rise_one_all_time(self, driver, create_and_delete_user, login, make_order):
        feed_page = FeedPage(driver)
        main_page = MainPage(driver)
        #сохранить значение текущее на странице Лента заказов
        feed_page.open_feed_page()
        feed_page.wait_title()
        assert feed_page.get_current_url() == Config.order_feed_url
        counter_quantity_orders = int(feed_page.find_counter_done_all_time().text)
        assert counter_quantity_orders is not None

        # оформить новый заказ
        main_page.open_main_page()
        main_page.wait_burgers_page()
        number_order = make_order()
        assert number_order is not None

        # проверить, что увеличился на 1
        feed_page.open_feed_page()
        feed_page.wait_title()
        #значение счетчика после заказа
        counter_quantity_orders_after_made_order = int(feed_page.find_counter_done_all_time().text)
        assert counter_quantity_orders_after_made_order == counter_quantity_orders + 1, "Номер заказа не увеличился"

    @allure.title('Проверка, что при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_after_create_new_order_counter_rise_one_today(self, driver, create_and_delete_user, login, make_order):
        feed_page = FeedPage(driver)
        main_page = MainPage(driver)
        #сохранить значение текущее на странице Лента заказов
        feed_page.open_feed_page()
        feed_page.wait_title()
        assert feed_page.get_current_url() == Config.order_feed_url
        counter_quantity_orders = int(feed_page.find_counter_done_today().text)
        assert counter_quantity_orders is not None

        # оформить новый заказ
        main_page.open_main_page()
        main_page.wait_burgers_page()
        number_order = make_order()
        assert number_order is not None

        # проверить, что увеличился на 1
        feed_page.open_feed_page()
        feed_page.wait_title()
        #значение счетчика после заказа
        counter_quantity_orders_after_made_order = int(feed_page.find_counter_done_today().text)
        assert counter_quantity_orders_after_made_order == counter_quantity_orders + 1, "Номер заказа не увеличился"



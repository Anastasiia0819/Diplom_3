import requests
from src.config import Config
import json
from src.helpers import get_random_data_user
import pytest
from selenium import webdriver
from locators.login_page_locators import LoginPageLocators
from pages.login_page import LoginPage
from pages.main_page import MainPage
from selenium.webdriver import ActionChains
import time

"""
@pytest.fixture(params=["chrome", "firefox"], scope="function")
def driver(request):
    browser_name = request.param
    browser = None

    if browser_name == "chrome":
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        browser = webdriver.Firefox()
    else:
        raise ValueError("Invalid value")

    browser.maximize_window()
    browser.get(Config.URL)
    yield browser

    browser.quit()
"""


@pytest.fixture
def driver():
    chrome = webdriver.Chrome()
    chrome.maximize_window()
    chrome.get(Config.URL)
    yield chrome
    chrome.quit()


@pytest.fixture
def create_and_delete_user():
    email, password, name = get_random_data_user()
    user_data = {
        "email": email,
        "password": password,
        "name": name
    }
    #создание пользователя
    create_response = requests.post(f"{Config.URL}api/auth/register", json=user_data)
    assert create_response.status_code == 200, f"Пользователь не был создан, код ответа: {create_response.status_code}, текст: {create_response.text}"

    response_data = create_response.json()

    #получить токен (из ответа создания пользователя)
    token = create_response.json()["accessToken"]
    assert token, f"Токен не был получен: {create_response.text}"

    # передать данные пользователя и токен в тест
    yield {
        "user_data": user_data,
        "response_data": response_data,
        "token": token
    }
    #Удаление пользователя после теста
    headers = {"Authorization": token}
    delete_response = requests.delete(f"{Config.URL}api/auth/user", headers=headers)
    assert delete_response.status_code == 202, f"Ошибка удаления пользователя, статус: {delete_response.status_code}, текст: {delete_response.text}"


@pytest.fixture
def login(driver, create_and_delete_user):
    user_data = create_and_delete_user["user_data"]
    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    login_page.open_login_page()
    login_page.enter_email(user_data["email"])
    login_page.enter_password(user_data["password"])
    login_page.click_login_button()
    main_page.wait_burgers_page()
    main_page.wait_personal_account_button()
    assert login_page.get_current_url() == Config.URL, "Авторизация не выполнена"

    # Возвращаем статус успешного логина
    return True


@pytest.fixture()
def make_order(driver, create_and_delete_user, login):
    def _make_order():
        main_page = MainPage(driver)
        main_page.wait_burgers_page()

        # перенос ингредиента в корзину
        ingredient = main_page.find_ingredient_bulka()
        basket = main_page.find_basket()
        actions = ActionChains(driver)
        actions.drag_and_drop(ingredient, basket).perform()
        counter = main_page.find_counter_2()
        assert counter.is_displayed()

        # клик на Оформить заказ
        main_page.click_made_order_button()

        # ожидание модальное окно заказа
        main_page.wait_modal_order()

        # При открытии модалки ожидаем, что номер заказа равен 9999
        order_number_static = main_page.find_number_order()
        initial_order_number = "9999"
        assert order_number_static.text == initial_order_number, "Номер заказа не отображается как '9999' при открытии"

        # ожидание актуального номера заказа, отличного от initial_order_number
        main_page.wait_for_order_number_to_update(initial_order_number)

        # Проверка, что номер заказа изменился с статичного значения
        updated_order_number = order_number_static.text
        assert updated_order_number != initial_order_number, "Номер заказа не обновился на актуальный"

        number_order = main_page.find_number_order()
        assert updated_order_number is not None
        assert number_order.is_displayed(), "Номер заказа не отображается в модальном окне"
        main_page.click_close_button()
        return updated_order_number
    return _make_order




"""
Личный кабинет  (войти в аккаунт)

- переход по клику на «Личный кабинет»,
- переход в раздел «История заказов»,
- выход из аккаунта. (переход на страницу login)
https://stellarburgers.nomoreparties.site/account/profile
"""

from selenium.webdriver.common.by import By


class ProfilePageLocators:

    save_button = (By.XPATH, ".//button[contains(@class, 'button_button_type_primary')]") #кнопка Сохранить
    history_orders_button = (By.XPATH, ".//a[contains(@class, 'Account_link') and text()='История заказов']") #кнопка история заказов
    history_orders_button_active = (By.XPATH, ".//a[contains(@class, 'Account_link_active')]")
    logout_button = (By.XPATH, ".//button[@type='button' and text()='Выход']")  # кнопка выход(на странице Личный кабинет)

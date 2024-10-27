"""
Проверка основного функционала

- переход по клику на «Конструктор»,
- переход по клику на «Лента заказов»,
- если кликнуть на ингредиент, появится всплывающее окно с деталями,
- всплывающее окно закрывается кликом по крестику,
- при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента
- залогиненный пользователь может оформить заказ
https://stellarburgers.nomoreparties.site/
"""

from selenium.webdriver.common.by import By


class MainPageLocators:
    personal_account_button = By.XPATH, ".//a[@href='/account']"  # кнопка Личный кабинет
    burgers_page = By.XPATH, ".//div[contains(@class, 'BurgerIngredients_ingredients__menuContainer')]"  # отображение страницу с бургерами

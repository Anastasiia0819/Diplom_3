from selenium.webdriver.common.by import By


class MainPageLocators:
    personal_account_button = (By.XPATH, ".//a[@href='/account']")  # кнопка Личный кабинет
    burgers_page = (By.XPATH, ".//div[contains(@class, 'BurgerIngredients_ingredients__menuContainer')]")  # отображение страницу с бургерами
    constructor_button = (By.XPATH, ".//a[contains(@class, 'AppHeader_header__link') and @href='/']")
    offered_button = (By.XPATH, './/button[contains(@class,"button_button_type_primary")]')  # кнопка Оформить заказ
    order_feed_button = (By.XPATH, ".//a[@href='/feed']")#кнопка Лента заказов
    modal_page_order = (By.XPATH, ".//div[contains(@class, 'Modal_modal__contentBox')]")#модальное окно заказа
    number_order = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title_shadow')]")#номер заказа на модальном окне


class ConstructorLocators:
    ingredient_bulka = (By.XPATH, ".//a[@href = '/ingredient/61c0c5a71d1f82001bdaaa6d']")
    open_modal_page_ingredient = (By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]/div[contains(@class, 'Modal_modal__container')]") #модалка просле клика на ингридиент
    close_button = (By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]/div[contains(@class, 'Modal_modal__container')]/button[@type='button']") #кнопка закрыть на модалке
    basket = (By.XPATH, ".//ul[contains(@class, 'BurgerConstructor_basket')]") #корзина куда переносить ингридиенты
    counter_0 = (By.XPATH,".//a[@href = '/ingredient/61c0c5a71d1f82001bdaaa6d']/div[contains(@class, 'counter_default')]/p[contains(@class, 'counter_counter') and text()='0']") #счетчик у булки 0
    counter_2 = (By.XPATH, ".//a[@href = '/ingredient/61c0c5a71d1f82001bdaaa6d']/div[contains(@class, 'counter_default')]/p[contains(@class, 'counter_counter') and text()='2']")#счетчик у булки 2 после переноса


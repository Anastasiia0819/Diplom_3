#Раздел «Лента заказов»

from selenium.webdriver.common.by import By


class FeedOrderPageLocators:
    title_feed_order = (By.XPATH, ".//h1[contains(@class, 'text_type_main-large')]")#залоголов Лента заказов
    constructor_button = (By.XPATH, ".//a[contains(@class, 'AppHeader_header__link') and @href='/']") #кнопка Конструктор
    first_card_order = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_list')]/li[1]")#1-ая карточка списка
    modal_page_order = (By.XPATH, ".//div[contains(@class, 'Modal_orderBox')]") #модальное окно заказа
    counter_done_all_time = (By.XPATH, ".//p[contains(@class, 'text_type_main-medium') and text()='Выполнено за все время:']/following-sibling::p[contains(@class, 'OrderFeed_number')]") #счетчик
    counter_done_today = (By.XPATH, ".//p[contains(@class, 'text_type_main-medium') and text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'OrderFeed_number')]")
    number_order_in_work = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady')]/li[contains(@class, 'text_type_digits-default')]")#номер заказа в блоке "В работе"
    numbers_order_in_card_order = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_list')]/li[1]/a[contains(@class, 'OrderHistory_link')]/div[contains(@class, 'OrderHistory_textBox')]/p[contains(@class, 'text_type_digits-default')]") #номер заказа на 1 карточке (сверху)


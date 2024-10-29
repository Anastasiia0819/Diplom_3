from selenium.webdriver.common.by import By


class HistoryOrderPageLocators:
    number_last_order_user = (By.XPATH, ".//ul[contains(@class, 'OrderHistory_profileList')]/li[last()]/a[contains(@class, 'OrderHistory')]/div[contains(@class, 'OrderHistory')][1]/p[contains(@class,'text_type_digits-default')]") #номер последнего заказа
    list_card_order = (By.XPATH, ".//ul[contains(@class, 'OrderHistory_profileList')]") #список карточек заказа
    last_card = (By.XPATH, ".//ul[contains(@class, 'OrderHistory_profileList')]/li[last()]")
    order_feed_button = (By.XPATH, ".//a[@href='/feed']")  # кнопка Лента заказов

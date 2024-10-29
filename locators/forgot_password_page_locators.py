#страница "восставить пароль"

from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    title_recover_password = (By.XPATH, ".//div[contains(@class, 'Auth_login')]/h2[text()='Восстановление пароля']") #название заголовка "Восставновление пароля"
    send_email_field = (By.XPATH, ".//input[contains(@class, 'text input')]") #поле для введение почты
    recover_button = (By.XPATH, ".//button[contains(@class, 'button_button_type_primary')]") #кнопка "восставновить"

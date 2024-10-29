#страница сброса пароля

from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:
    title_forgot_password = (By.XPATH, ".//div[contains(@class, 'Auth_login')]/h2[text()='Восстановление пароля']") #название заголовка "Восставновление пароля"
    send_password_field = (By.XPATH, ".//input[contains(@class, 'text input') and @type='password' ]") #поле для ввода нового пароля
    show_password_button = (By.XPATH, ".//div[contains(@class, 'input__icon')]") #глазик (скрыть/показать пароль)
    show_password_button_activ = (By.XPATH, ".//input[@type='text' and contains(@class, 'text_type_main-default')]")  # подсвечено поле Пароль
    show_password_button_default = (By.XPATH, ".//input[@type='password' and contains(@class, 'text_type_main-default')]") # не подсвечено поле Пароль
    save_button = (By.XPATH, ".//button[text()='Сохранить']") #кнопка Сохранить



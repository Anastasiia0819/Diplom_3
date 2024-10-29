#страница login

from selenium.webdriver.common.by import By


class LoginPageLocators:
    recover_password_button = (By.XPATH, './/a[@href="/forgot-password"]') #кнопка "Восстановить пароль"
    email_field = By.XPATH, ".//input[@name='name']"  # заполнение поля Email
    password_field = By.XPATH, ".//input[@name='Пароль']"  # заполнение поля Пароль
    login_button = By.XPATH, ".//button[text() = 'Войти']"

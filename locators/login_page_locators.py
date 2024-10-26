#страница login

from selenium.webdriver.common.by import By


class LoginPageLocators:
    recover_password_button = (By.XPATH, './/a[@href="/forgot-password"]') #кнопка "Восстановить пароль"

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.remote.webdriver import WebDriver
#from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def navigate(self, url):
        self.driver.get(url)

    # Получение текущего URL страницы
    def get_current_url_base(self):
        return self.driver.current_url

#проверка наличия элемента
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))

#клик на элемент
    def click_element(self, locator, timeout=10):
        self.find_element(locator, timeout).click()

    #вставить текст в поле
    def enter_text(self, locator, text, timeout=10):
        self.find_element(locator, timeout).send_keys(text)

    #ожидание элемента
    def wait_for_element_visible(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

        # ожидание элементов
    def wait_for_elements_visible(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_all_elements_located(locator))

#ожидание кликабельности элемента
    def wait_element_to_be_clickable(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))

    #скролл
    def scroll(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    #проверка ожидание, пока элемент станет невидимым
    def wait_for_element_invisible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.invisibility_of_element_located(locator))

    #ожидание элемента отличного от изначального (используется в номере заказа)
    def wait_for_number_change(self, element, initial_number, timeout=30):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: element.text != initial_number)
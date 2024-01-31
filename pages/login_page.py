from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from base.base_class import Base
from utilites.logger import Logger


class Login_page(Base):
    url = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    username = "//input[@id='user-name']"
    password = "//input[@id='password']"
    button_login = "//input[@id='login-button']"
    main_word = "//span[@class='title']"

    # Getters

    def get_username(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.username)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_button_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_login)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))
    # Actions

    def input_username(self, username):
        self.get_username().send_keys(username)
        print("Input username")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_button_login(self):
        self.get_button_login().click()
        print("Input button_login")

    # Methods

    def authorization(self):
        with allure.step("authorization"):
            Logger.add_start_step(method="authorization")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.input_username("standard_user")
            self.input_password("secret_sauce")
            self.click_button_login()
            self.assert_word(self.get_main_word(), 'Products')
            Logger.add_end_step(url=self.driver.current_url, method="authorization")

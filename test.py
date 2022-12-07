import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Locators
close_modal_login = (By.XPATH, '//button[@class="_2KpZ6l _2doB4z"]')
input_search = (By.NAME, "q")
filter_options = (By.CLASS_NAME, "_10UF8M")
product_price = (By.XPATH, '//div[@class="_30jeq3 _1_WHN1"]')
add_to_cart = (By.XPATH, '//button[@text="ADD TO CART"]')


class Methods:
    TIME_OUT = 30

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator):
        WebDriverWait(self.driver, self.TIME_OUT).until(EC.visibility_of_element_located(locator)).click()

    def send_text(self, locator, text):
        """ Se coloca texto en un input, recibe como parámetro el texto  """
        WebDriverWait(self.driver, self.TIME_OUT).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def click_by_text(self, locator, text):
        """ Función para dar clic en un elemento según el texto """
        WebDriverWait(self.driver, self.TIME_OUT).until(EC.visibility_of_element_located(locator))
        elements = self.driver.find_elements(*locator)
        for element in elements:
            print(element.text)
            if text == element.text:
                element.click()

    def scroll_page(self):
        self.driver.execute_script("window.scrollTo(0, 500);")
        time.sleep(3)


class TestCart(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('./chromedriver')
        cls.methods = Methods(cls.driver)
        cls.driver.maximize_window()
        cls.driver.get("http://flipkart.com/")

    def setUp(self) -> None:
        pass

    def test_cart(self):
        self.methods.click_element(close_modal_login)
        self.methods.send_text(input_search, 'iPhone 13')
        self.methods.send_text(input_search, Keys.ENTER)
        self.methods.click_by_text(filter_options, "Price -- Low to High")
        self.methods.scroll_page()
        self.methods.click_by_text(product_price, "₹32,990")
        new_tab = self.driver.current_window_handle

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

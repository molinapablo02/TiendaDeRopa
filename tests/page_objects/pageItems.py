from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

class PageItems:
    def __init__(self, my_driver):

        self.orange_button = 'color_1'
        self.order = (By.ID, 'selectProductSort')
        self.checkbox = (By.CLASS_NAME, 'checkbox')
        self.color_check = (By.CLASS_NAME, 'color-option  ')
        self.casual_dresses_link = (By.CLASS_NAME, 'subcategory-name')
        self.driver = my_driver

    def click_orange_button(self):
        self.driver.find_element_by_id(self.orange_button).click()

    def select_by_text(self, text):

        order = Select(self.driver.find_element(*self.order))
        order.select_by_visible_text(text)

    def select_by_value(self, text):
        order = Select(self.driver.find_element(*self.order))
        order.select_by_value(text)

    def select_by_index(self,number):
        order = Select(self.driver.find_element(*self.order))
        order.select_by_index(number)

    def click_checkbox(self, number):
        self.driver.find_elements(*self.checkbox)[number].click()

    def click_colors(self, number):
        self.driver.find_elements(*self.color_check)[number].click()

    def click_casual_dresses_link(self):
        self.driver.find_element(*self.casual_dresses_link).click()
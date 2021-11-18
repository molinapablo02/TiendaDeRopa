from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class PageItem:
    def __init__(self, my_driver):
        self.driver = my_driver
        self.quantity = 'quantity_wanted'
        self.plus = 'icon-plus'
        self.printed_dress = (By.XPATH, "(//*[@title='Printed Dress'])")
        self.order = (By.ID, 'group_1')
        self.add_button = (By.NAME, 'Submit')
        self.checkout_button = (By.CLASS_NAME, 'icon-chevron-right right')

    def enter_quantity(self, quantity):
        self.driver.find_element_by_id(self.quantity).clear()
        self.driver.find_element_by_id(self.quantity).send_keys(quantity)

    def click_plus_button(self, quantity):
        for i in range(quantity):
            self.driver.find_element_by_class_name(self.plus).click()

    def get_number_of_element(self):
        #retorna un string porque el value es string
        return self.driver.find_element_by_id(self.quantity).get_attribute('value')

    def click_printed_dress(self):
        self.driver.find_elements(*self.printed_dress)[2].click()

    def select_size_L(self, number):
        order = Select(self.driver.find_element(*self.order))
        order.select_by_index(number)

    def click_add_to_cart(self):
        self.driver.find_element(*self.add_button).click()

    def proceed_to_checkout(self):
        self.driver.find_element(*self.checkout_button).click()


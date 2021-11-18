#si reciebiera algo por parametro ahi si tendria q poner los parentesis
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

class PageIndex:
    def __init__(self, my_driver):
        #self.query_top = 'search_query_top'
        #self.query_button = 'submit_search'

        self.query_top = (By.ID, 'search_query_top')
        self.query_button = (By.NAME, 'submit_search')
        self.dresses_link = (By.XPATH, '//*[@title="Dresses"]')

        #self.dresses_link = (By.LINK_TEXT, 'Dresses')
        self.driver = my_driver

    def search(self, item):
        try:
            search_box = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.query_top))
            search_box.send_keys(item)
            search_button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.query_button))
            search_button.click()

        except:
                print("no se encuentra el elemento")



    def click_dresses(self):
        #como hay dos elementos llamados igual (dresses) agarra el primero, que no es visible, y me da error.
        #entonces hago un array de webelements de esos elementos con el find ELEMENTS y agarro la posicion [1] que es el visible y q necesito
        self.driver.find_elements(*self.dresses_link)[1].click()



        #self.driver.find_element(*self.query_top).send_keys(item)
        #self.driver.find_element(*self.query_button).click()
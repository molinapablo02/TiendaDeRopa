import unittest
from selenium import webdriver
import time

#De la CLASE pageIndex importar la clase llamada PageIndex

from tests.page_objects.pageIndex import PageIndex
from tests.page_objects.pageItems import PageItems
from tests.page_objects.pageItem import PageItem

from selenium.webdriver.chrome.options import Options


class SearchCases(unittest.TestCase):
    #@classmethod
    #def setUpClass(cls):
     #   print('creando base de datos...')
      #  print('base de datos creada...')

    #def tearDownClass(cls):
     #   print('eliminando nuestra base de datos...')
      #  print('base de datos elimanada')

    def setUp(self):
        option = Options()
        option.add_argument("start-maximized")
        #option.add_argument("--headless")

        self.driver = webdriver.Chrome('tests/drivers/chromedriver.exe', options=option)
        self.driver.get('http://automationpractice.com/index.php')

        self.driver.implicitly_wait(10)
        self.index_Page = PageIndex(self.driver)
        self.items_page = PageItems(self.driver)
        self.item_page = PageItem(self.driver)


    #para saltear test
    @unittest.skip("not needed now")
    def test_search_find_tshirts(self):
        self.index_Page.search('t-shirt')
        time.sleep(3)

    @unittest.skip("not needed now")
    def test_tarea(self):
        self.index_Page.search('t-shirt')
        self.items_page.click_orange_button()
        self.item_page.enter_quantity('25')
        self.item_page.click_plus_button(3)
        number = self.item_page.get_number_of_element()
        self.assertTrue(number == '28')

    @unittest.skip("not needed now")
    def test_selection(self):
        self.index_Page.search('t-shirt')
        self.items_page.select_by_text('Product Name: A to Z')
        self.items_page.select_by_value('reference:asc')
        self.items_page.select_by_index(3)

    def test_select_dresses_options(self):
        self.index_Page.click_dresses()
        self.items_page.click_casual_dresses_link()
        self.item_page.click_printed_dress()
        self.item_page.enter_quantity(5)
        self.item_page.select_size_L(2)
        self.item_page.click_add_to_cart()

        #self.items_page.click_checkbox(1)
        #self.items_page.click_checkbox(4)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

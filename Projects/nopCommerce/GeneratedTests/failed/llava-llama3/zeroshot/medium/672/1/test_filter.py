from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class TestLibraryThingFiltering(unittest.TestCase):
    def setUp(self):
        chromedriver = ChromeDriverManager().install()
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_filter_books_by_size_medium(self):
        # Open the homepage
        self.driver.get("http://max/")
        
        # Click on the "Search" link from the top navigation
        search_link = self.driver.find_element_by_name('search')
        ActionChains(self.driver).move_to_element(search_link).perform()
        search_link.click()

        # Enter the search term and perform the search
        search_bar = self.driver.find_element_by_name('searchTerm')
        search_bar.send_keys("book")
        search_bar.send_keys(Keys.RETURN)

        # Locate and interact with the price range slider
        WebDriverWait(self.driver, 20).until(lambda x: x.current_url().include("price"))
        WebDriverWait(self.driver, 20).until(lambda x: self.assertTrue(self.driver.title_text() != ""))
        
        # Verify that the filtered URL includes the price parameter
        self.assertTrue(self.driver.current_url().include("price"))

if __name__ == '__main__':
    unittest.main()
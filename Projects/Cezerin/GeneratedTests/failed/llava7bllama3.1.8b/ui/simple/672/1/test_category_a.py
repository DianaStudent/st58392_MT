from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestOnlineStore(unittest.TestCase):

    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000")

    def test_main_components(self):
        # Check the main UI components are present and visible

        # Logo
        logo = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//img[@src='logo.png']")))
        self.failUnless(logo.is_displayed(), "Logo is not displayed")

        # Search icon
        search_icon = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//i[@class='search-icon']")))
        self.failUnless(search_icon.is_displayed(), "Search icon is not displayed")

        # Buy now button
        buy_now_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='buy-now-button']")))
        self.failUnless(buy_now_button.is_displayed(), "Buy now button is not displayed")

    def test_category_a_link(self):
        # Check that the link to category A is present and clickable

        category_a_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/category-a']")))
        self.failUnless(category_a_link.is_displayed(), "Category A link is not displayed")
        category_a_link.click()

        # Check that we are on the correct page
        current_url = self.driver.current_url
        self.assertEqual(current_url, 'http://localhost:3000/category-a')

    def test_category_a_1_link(self):
        # Check that the link to category A 1 is present and clickable

        category_a_1_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/category-a-1']")))
        self.failUnless(category_a_1_link.is_displayed(), "Category A 1 link is not displayed")
        category_a_1_link.click()

        # Check that we are on the correct page
        current_url = self.driver.current_url
        self.assertEqual(current_url, 'http://localhost:3000/category-a-1')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_ui_elements(self):
        # Open the page
        self.driver.get('http://localhost/')

        # Wait for navigation links to be visible
        nav_links = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//nav/a")))
        self.assertEqual(len(nav_links), 2)

        # Wait for search bar and input field to be visible
        search_bar = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search...']")))

        # Click on the "Tables" link
        tables_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'tables')))
        tables_link.click()

        # Wait for table products to be visible
        tables_products = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Tables']")))
        self.assertEqual(tables_products.text, 'Tables')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
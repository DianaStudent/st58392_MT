import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CategoryATest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.base_url = "http://localhost:3000/category-a"
        self.driver.get(self.base_url)

    def test_ui_elements_present(self):
        driver = self.driver

        # Wait for header
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.TAG_NAME, 'header'))
        )

        # Check logo link
        logo_link = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'a.logo-image'))
        )
        self.assertIsNotNone(logo_link)

        # Check search input
        search_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.search-input'))
        )
        self.assertIsNotNone(search_input)

        # Check category breadcrumb
        breadcrumb = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav.breadcrumb'))
        )
        self.assertIsNotNone(breadcrumb)

        # Check product list
        products = WebDriverWait(driver, 20).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div.products div.product-name'))
        )
        self.assertGreater(len(products), 0, "No products found")

        # Check filter button (mobile)
        filter_button = driver.find_element(By.CSS_SELECTOR, 'button.button.is-fullwidth')
        self.assertTrue(filter_button.is_displayed())

        # Check sort dropdown
        sort_dropdown = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'select'))
        )
        self.assertIsNotNone(sort_dropdown)

        # Check footer
        footer = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.TAG_NAME, 'footer'))
        )
        self.assertIsNotNone(footer)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
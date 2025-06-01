import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class CategoryATest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost:3000/category-a")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Verify header logo is present and visible
        header_logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.logo-image")))
        self.assertTrue(header_logo.is_displayed(), "Header logo is not displayed")

        # Verify navigation links are present and visible
        nav_links = driver.find_elements(By.CSS_SELECTOR, ".nav-level-0 li .cat-parent a")
        self.assertEqual(len(nav_links), 3, "Not all navigation links are present")
        for link in nav_links:
            self.assertTrue(link.is_displayed(), f"Navigation link '{link.text}' is not displayed")

        # Verify search input is present and visible
        search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-input")))
        self.assertTrue(search_input.is_displayed(), "Search input is not displayed")

        # Verify 'Sort' dropdown is present and visible
        sort_dropdown = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".select select")))
        self.assertTrue(sort_dropdown.is_displayed(), "Sort dropdown is not displayed")

        # Verify product listings are present and visible
        products = driver.find_elements(By.CSS_SELECTOR, ".products .product-caption")
        self.assertEqual(len(products), 2, "Not all products are displayed")
        for product in products:
            self.assertTrue(product.is_displayed(), "Product is not displayed")

        # Interact with the 'Sort' dropdown
        sort_dropdown.click()
        option_newest = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "option[value='-date_created']")))
        option_newest.click()

        # Check UI does not throw error after interaction
        body = driver.find_element(By.TAG_NAME, "body")
        self.assertFalse("error" in body.text.lower(), "UI displays an error after interaction")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
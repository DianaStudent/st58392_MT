import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCategoryAPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.wait = WebDriverWait(self.driver, 20)

    def test_elements_presence_and_interaction(self):
        driver = self.driver
        wait = self.wait

        # Check for header
        try:
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        except Exception:
            self.fail("Header is missing.")

        # Check for navigation links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/']")))
            category_a_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category-a']")))
            category_b_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category-b']")))
            category_c_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category-c']")))
        except Exception:
            self.fail("One or more navigation links are missing.")

        # Check for search input
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.search-input')))
        except Exception:
            self.fail("Search input is missing.")

        # Check for sort dropdown
        try:
            sort_dropdown = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'select')))
        except Exception:
            self.fail("Sort dropdown is missing.")

        # Check for product links
        try:
            product_a_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category-a/product-a']")))
            product_b_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category-a/product-b']")))
        except Exception:
            self.fail("One or more product links are missing.")

        # Check for footer
        try:
            footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
        except Exception:
            self.fail("Footer is missing.")

        # Try interacting with search input and check no errors occur
        try:
            search_input.send_keys("test")
        except Exception:
            self.fail("Unable to interact with search input.")

        # Check Empty Cart UI
        try:
            cart_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Your cart is empty')]")))
        except Exception:
            self.fail("Empty cart message is missing.")

        # Try clicking on a product link
        try:
            product_a_link.click()
            wait.until(EC.url_contains("/product-a"))
        except Exception:
            self.fail("Unable to interact with product link.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
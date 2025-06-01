import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestHomePageUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:3000")

    def test_home_page_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Verify header elements
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
            self.assertIsNotNone(header)

            logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.logo-image")))
            self.assertIsNotNone(logo)

            # Verify categories
            category_a = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Category A")))
            self.assertIsNotNone(category_a)

            category_b = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Category B")))
            self.assertIsNotNone(category_b)

            category_c = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Category C")))
            self.assertIsNotNone(category_c)

            # Verify search field
            search_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.search-input")))
            self.assertIsNotNone(search_box)
            
            # Verify best sellers and products
            best_sellers = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.title.is-4.has-text-centered")))
            self.assertIsNotNone(best_sellers)

            product_a = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Product A")))
            self.assertIsNotNone(product_a)

            product_b = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Product B")))
            self.assertIsNotNone(product_b)

            # Verify footer elements
            footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "footer")))
            self.assertIsNotNone(footer)

        except Exception as e:
            self.fail(f"UI element not found or not visible: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
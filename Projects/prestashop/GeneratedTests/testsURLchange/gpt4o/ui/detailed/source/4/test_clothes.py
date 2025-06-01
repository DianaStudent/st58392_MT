import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestClothesPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/3-clothes")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver

        # Wait for the header to be visible
        header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
        self.assertIsNotNone(header, "Header is missing or not visible")

        # Check for the presence and visibility of main elements
        try:
            # Navigation elements
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))

            # Main sections
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".block-category.card.card-block")))
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".subcategory-heading")))
            self.wait.until(EC.visibility_of_element_located((By.ID, "products")))

            # Interaction buttons
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-unstyle.select-title")))
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".wishlist-button-add")))

            # Input fields
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='s']")))

            # Footer
            footer = self.wait.until(EC.visibility_of_element_located((By.ID, "footer")))
            self.assertIsNotNone(footer, "Footer is missing or not visible")

            # Interact with a button to confirm UI reaction
            sort_by_button = driver.find_element(By.CSS_SELECTOR, ".btn-unstyle.select-title")
            sort_by_button.click()

            # Confirm dropdown visibility
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".dropdown-menu")))
        
        except Exception as e:
            self.fail(f"Some UI elements are missing or not visible: {str(e)}")

if __name__ == "__main__":
    unittest.main()
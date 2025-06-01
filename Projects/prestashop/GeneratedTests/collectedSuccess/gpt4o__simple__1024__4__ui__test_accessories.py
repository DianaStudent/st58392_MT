import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService

class TestAccessoriesPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/6-accessories")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        
        # Verify that header elements are visible
        self.assertTrue(self.wait.until(EC.visibility_of_element_located((By.ID, "header"))), "Header is not visible")
        
        # Verify that top menu links are visible
        for link_text in ["Home", "Clothes", "Accessories", "Art"]:
            self.assertTrue(
                self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text))),
                f"{link_text} link is not visible"
            )

        # Verify language selector
        self.assertTrue(self.wait.until(EC.visibility_of_element_located((By.ID, "_desktop_language_selector"))), "Language selector is not visible")

        # Verify Sign in button
        self.assertTrue(self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in"))), "Sign in button is not visible")

        # Verify Cart visibility
        self.assertTrue(self.wait.until(EC.visibility_of_element_located((By.ID, "_desktop_cart"))), "Cart icon is not visible")

        # Verify Page Title is visible
        self.assertTrue(self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1"))), "Page title is not visible")
        
        # Verify some product items are visible
        self.assertTrue(self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product-miniature"))), "No products are visible")
        
        # Verify that footer is visible
        self.assertTrue(self.wait.until(EC.visibility_of_element_located((By.ID, "footer"))), "Footer is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check visibility of headers
        self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
        
        # Check visibility of footer
        self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "footer")))

        # Check navigation links
        nav_links = [
            (By.LINK_TEXT, "Category A"),
            (By.LINK_TEXT, "Category B"),
            (By.LINK_TEXT, "Category C")
        ]

        for link in nav_links:
            self.wait.until(EC.visibility_of_element_located(link))

        # Check search input field
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-input")))

        # Check search icon
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-icon-search")))

        # Check for cart icon
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "cart-button")))

        # Check for banner and best sellers section
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "home-slider")))
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "products")))

        # Interact with UI elements
        # Click on the first bullet in slider
        slider_bullet = driver.find_element(By.CSS_SELECTOR, ".image-gallery-bullet")
        slider_bullet.click()

        # Confirm UI reacts visually
        # Check if active class is set on first bullet after click
        active_bullet = driver.find_element(By.CSS_SELECTOR, ".image-gallery-bullet.active")
        self.assertIsNotNone(active_bullet, "Slider bullet did not become active.")

        # Assert that no required element is missing by checking some key text elements
        self.assertTrue(driver.find_element(By.CLASS_NAME, "title").is_displayed(), "Best Sellers title is not visible.")
        
        # Check product elements
        product_name = driver.find_element(By.CLASS_NAME, "product-name")
        product_price = driver.find_element(By.CLASS_NAME, "product-price")

        self.assertTrue(product_name.is_displayed(), "Product name is not visible.")
        self.assertTrue(product_price.is_displayed(), "Product price is not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService

class UITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_ui_elements(self):
        driver = self.driver
        
        # Wait for header to be visible
        header = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "header-area"))
        )
        
        # Check header elements
        self.assertTrue(header.is_displayed(), "Header is not visible.")

        # Wait for navigation links
        nav_links = WebDriverWait(driver, 20).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//nav//a"))
        )

        # Check navigation links
        expected_links = ['Home', 'Tables', 'Chairs']
        nav_texts = [link.text for link in nav_links]
        for link in expected_links:
            self.assertIn(link, nav_texts, f"Navigation link '{link}' is missing.")

        # Wait for footer to be visible
        footer = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "footer-area"))
        )
        
        # Check footer
        self.assertTrue(footer.is_displayed(), "Footer is not visible.")

        # Check and click 'Accept' button in cookie consent
        accept_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "rcc-confirm-button"))
        )
        self.assertTrue(accept_button.is_displayed(), "Accept cookies button is not visible.")
        accept_button.click()

        # Verify interaction
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.ID, "rcc-confirm-button"))
        )

        # Check product display
        products = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "product-wrap"))
        )
        self.assertTrue(products.is_displayed(), "Product list is not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
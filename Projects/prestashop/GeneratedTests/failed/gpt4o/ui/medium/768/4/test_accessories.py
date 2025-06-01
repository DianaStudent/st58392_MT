from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestAccessoriesPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/6-accessories")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_ui_elements(self):
        try:
            # Check presence of the header
            header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
            self.assertTrue(header.is_displayed(), "Header is not visible")

            # Check presence of the navigation links
            nav_links = [
                "http://localhost:8080/en/3-clothes",
                "http://localhost:8080/en/6-accessories",
                "http://localhost:8080/en/9-art",
            ]
            for link in nav_links:
                nav_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//a[@href='{link}']")))
                self.assertTrue(nav_element.is_displayed(), f"Navigation link {link} is not visible")

            # Check presence of search input
            search_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "s")))
            self.assertTrue(search_input.is_displayed(), "Search input is not visible")

            # Check presence of the cart button
            cart_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart")))
            self.assertTrue(cart_button.is_displayed(), "Cart button is not visible")

            # Check presence of the sign-in link
            sign_in_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
            self.assertTrue(sign_in_link.is_displayed(), "Sign in link is not visible")

            # Interacting with an element, click on the first product to view its details
            first_product = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-title a")))
            first_product.click()

            # Verify the page updates visually by checking presence of the product details
            product_details = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product-description")))
            self.assertTrue(product_details.is_displayed(), "Product details are not visible after clicking product")

        except Exception as e:
            self.fail(f"Test failed due to missing element: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestClothesPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/3-clothes")

    def test_ui_elements_presence(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Check for header
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
            self.assertTrue(header.is_displayed(), "Header is not visible.")

            # Check for contact link
            contact_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Contact us")))
            self.assertTrue(contact_link.is_displayed(), "Contact link is not visible.")

            # Check for search input
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='s'][type='text']")))
            self.assertTrue(search_input.is_displayed(), "Search input is not visible.")

            # Check for language selector
            language_selector = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".language-selector button")))
            self.assertTrue(language_selector.is_displayed(), "Language selector is not visible.")

            # Check for cart
            cart = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#_desktop_cart .header")))
            self.assertTrue(cart.is_displayed(), "Cart is not visible.")

            # Check for product list
            product_list = wait.until(EC.visibility_of_element_located((By.ID, "js-product-list")))
            self.assertTrue(product_list.is_displayed(), "Product list is not visible.")

            # Interact with an element
            contact_link.click()
            wait.until(EC.url_contains("contact-us"))

        except Exception as e:
            self.fail(f"Test failed: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
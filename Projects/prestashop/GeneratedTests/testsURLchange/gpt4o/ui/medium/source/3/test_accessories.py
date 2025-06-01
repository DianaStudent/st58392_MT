import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestAccessoriesPage(unittest.TestCase):
    def setUp(self):
        # Initialize the WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_ui_elements_present_and_interactive(self):
        driver = self.driver
        driver.get("http://localhost:8080/en/6-accessories")

        try:
            # Check for header elements
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "header")))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "category")))

            # Check for navigation links
            nav_links = [
                (By.LINK_TEXT, "Home"),
                (By.LINK_TEXT, "Clothes"),
                (By.LINK_TEXT, "Accessories"),
                (By.LINK_TEXT, "Art"),
                (By.XPATH, "//a[@title='Log in to your customer account']"),
            ]
            for by, value in nav_links:
                elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((by, value)))
                self.assertTrue(elem.is_displayed())

            # Check for category header
            category_header = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Accessories')]"))
            )
            self.assertTrue(category_header.is_displayed())

            # Check for 'Contact us' link
            contact_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Contact us"))
            )
            self.assertTrue(contact_link.is_displayed())

            # Check for search input
            search_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search our catalog']"))
            )
            self.assertTrue(search_input.is_displayed())

            # Interact with the search input
            search_input.send_keys("Mug")

            # Check for 'Cart' button
            cart_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//span[@class='cart-products-count']"))
            )
            self.assertTrue(cart_button.is_displayed())

            # Interact with the 'Cart' button
            cart_button.click()

            # Validate no errors and cart remains visible
            self.assertTrue(cart_button.is_displayed())

        except Exception as e:
            self.fail(f"Test failed due to missing or non-interactive element: {e}")

    def tearDown(self):
        # Close the WebDriver
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
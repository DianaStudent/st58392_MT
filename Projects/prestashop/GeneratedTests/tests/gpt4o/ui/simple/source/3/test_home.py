import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class TestUIPresence(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check the presence of the header
        try:
            wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except:
            self.fail("Header not found or not visible.")

        # Check the presence of the contact link
        try:
            wait.until(EC.visibility_of_element_located((By.ID, "_desktop_contact_link")))
        except:
            self.fail("Contact link not found or not visible.")

        # Check the presence of the language selector
        try:
            wait.until(EC.visibility_of_element_located((By.ID, "_desktop_language_selector")))
        except:
            self.fail("Language selector not found or not visible.")

        # Check the presence of the user info (Sign in)
        try:
            wait.until(EC.visibility_of_element_located((By.ID, "_desktop_user_info")))
        except:
            self.fail("User info (Sign in) not found or not visible.")

        # Check the presence of the shopping cart
        try:
            wait.until(EC.visibility_of_element_located((By.ID, "_desktop_cart")))
        except:
            self.fail("Shopping cart not found or not visible.")

        # Check the presence of the top menu
        try:
            wait.until(EC.visibility_of_element_located((By.ID, "_desktop_top_menu")))
        except:
            self.fail("Top menu not found or not visible.")

        # Check the presence of the search widget
        try:
            wait.until(EC.visibility_of_element_located((By.ID, "search_widget")))
        except:
            self.fail("Search widget not found or not visible.")

        # Check the presence of the carousel
        try:
            wait.until(EC.visibility_of_element_located((By.ID, "carousel")))
        except:
            self.fail("Carousel not found or not visible.")
        
        # Check the presence of the featured products section
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "featured-products")))
        except:
            self.fail("Featured products section not found or not visible.")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
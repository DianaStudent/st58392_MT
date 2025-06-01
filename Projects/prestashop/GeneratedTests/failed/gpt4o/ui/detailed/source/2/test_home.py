from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver
        
        # Verify header elements
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
            language_dropdown = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "language-selector")))
            sign_in = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
            cart = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "cart-products-count")))

            self.assertIsNotNone(header)
            self.assertIsNotNone(language_dropdown)
            self.assertIsNotNone(sign_in)
            self.assertIsNotNone(cart)
        except:
            self.fail("Header elements are not visible")

        # Verify menu items
        try:
            clothes_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
            accessories_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
            art_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))

            self.assertIsNotNone(clothes_link)
            self.assertIsNotNone(accessories_link)
            self.assertIsNotNone(art_link)
        except:
            self.fail("Menu items are not visible")

        # Interact with the language selector
        try:
            language_button = driver.find_element(By.CSS_SELECTOR, "button.btn-unstyle")
            language_button.click()
            
            language_options = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "dropdown-menu")))
            self.assertIsNotNone(language_options)
        except:
            self.fail("Language selector is not functional")

        # Verify search input field
        try:
            search_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "s")))
            self.assertIsNotNone(search_input)
        except:
            self.fail("Search input field is not visible")

        # Verify and interact with product carousel
        try:
            carousel = self.wait.until(EC.visibility_of_element_located((By.ID, "carousel")))
            self.assertIsNotNone(carousel)

            next_button = driver.find_element(By.CSS_SELECTOR, "a.right.carousel-control")
            next_button.click()
        except:
            self.fail("Product carousel is not functional")

        # Verify footer elements
        try:
            footer = self.wait.until(EC.visibility_of_element_located((By.ID, "footer")))
            newsletter_input = driver.find_element(By.NAME, "email")
            self.assertIsNotNone(footer)
            self.assertIsNotNone(newsletter_input)
        except:
            self.fail("Footer elements are not visible")

if __name__ == "__main__":
    unittest.main()
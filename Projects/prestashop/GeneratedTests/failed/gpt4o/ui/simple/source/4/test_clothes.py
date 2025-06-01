from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class ClothesPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/3-clothes")
        self.wait = WebDriverWait(self.driver, 20)

    def test_elements_visibility(self):
        driver = self.driver
        wait = self.wait

        # Check header
        try:
            wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except:
            self.fail("Header is not visible")

        # Check language selector
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "language-selector-wrapper")))
        except:
            self.fail("Language selector is not visible")

        # Check contact us link
        try:
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Contact us")))
        except:
            self.fail("Contact us link is not visible")

        # Check sign in link
        try:
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
        except:
            self.fail("Sign in link is not visible")

        # Check cart link
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping-cart")))
        except:
            self.fail("Cart link is not visible")

        # Check search bar
        try:
            wait.until(EC.visibility_of_element_located((By.NAME, "s")))
        except:
            self.fail("Search bar is not visible")

        # Check categories
        try:
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Men")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Women")))
        except:
            self.fail("Categories are not visible")

        # Check product listings
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "products")))
        except:
            self.fail("Product listings are not visible")

        # Check footer
        try:
            wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        except:
            self.fail("Footer is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
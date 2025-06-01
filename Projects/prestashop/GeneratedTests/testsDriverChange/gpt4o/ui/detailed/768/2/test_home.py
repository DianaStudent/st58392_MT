import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check Header
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except:
            self.fail("Header not found or not visible")

        # Check Footer
        try:
            footer = self.wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        except:
            self.fail("Footer not found or not visible")

        # Check Navigation Links
        try:
            clothes_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
            accessories_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
            art_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))
        except:
            self.fail("Navigation links not found or not visible")

        # Check Contact Us
        try:
            contact_us_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Contact us']")))
        except:
            self.fail("Contact us link not found or not visible")

        # Check Login and Register
        try:
            login_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@title='Log in to your customer account']")))
            register_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Create account")))
        except:
            self.fail("Login or Register links not found or not visible")

        # Check Search Widget
        try:
            search_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='text' and @name='s']")))
        except:
            self.fail("Search input not found or not visible")

        # Click and interact with the Search Widget
        search_input.send_keys("test")
        search_input.clear()

        # Verify Popular Products Section
        try:
            popular_products_section = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Popular Products']")))
        except:
            self.fail("Popular Products section not found or not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
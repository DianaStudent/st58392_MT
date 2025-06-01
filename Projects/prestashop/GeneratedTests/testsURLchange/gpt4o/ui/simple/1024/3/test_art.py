import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestArtPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/9-art")

    def test_ui_elements(self):
        driver = self.driver

        try:
            # Wait for and check the header
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "header"))
            )
            
            # Check for the "Contact us" link
            contact_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[text()='Contact us']"))
            )
            self.assertIsNotNone(contact_link)

            # Check for the "Sign in" link
            sign_in_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[@title='Log in to your customer account']"))
            )
            self.assertIsNotNone(sign_in_link)

            # Check for the "Cart" link
            cart_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "shopping-cart"))
            )
            self.assertIsNotNone(cart_link)

            # Check for the "Art" category title
            category_title = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//h1[text()='Art']"))
            )
            self.assertIsNotNone(category_title)

            # Check the search input field
            search_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search our catalog']"))
            )
            self.assertIsNotNone(search_input)

            # Check the newsletter subscription
            newsletter_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Your email address']"))
            )
            self.assertIsNotNone(newsletter_input)

            # Check for the footer presence
            footer = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "footer"))
            )
            self.assertIsNotNone(footer)

        except Exception as e:
            self.fail(f"A required UI element is missing: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
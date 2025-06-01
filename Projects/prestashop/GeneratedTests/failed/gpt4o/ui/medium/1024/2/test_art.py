from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class ArtPageUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/9-art")

    def test_presence_of_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Verify navigation links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="http://localhost:8080/en/"]')))
            clothes_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="http://localhost:8080/en/3-clothes"]')))
            accessories_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="http://localhost:8080/en/6-accessories"]')))
            art_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="http://localhost:8080/en/9-art"]')))
            login_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href^="http://localhost:8080/en/login"]')))
            register_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="http://localhost:8080/en/registration"]')))
            self.assertTrue(home_link.is_displayed())
            self.assertTrue(clothes_link.is_displayed())
            self.assertTrue(accessories_link.is_displayed())
            self.assertTrue(art_link.is_displayed())
            self.assertTrue(login_link.is_displayed())
            self.assertTrue(register_link.is_displayed())
        except Exception as e:
            self.fail(f"One or more navigation links are not present or visible: {str(e)}")

        # Verify search input
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Search our catalog"]')))
            self.assertTrue(search_input.is_displayed())
        except Exception as e:
            self.fail(f"Search input is not present or visible: {str(e)}")

        # Verify "Contact us" link
        try:
            contact_us_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="http://localhost:8080/en/contact-us"]')))
            self.assertTrue(contact_us_link.is_displayed())
        except Exception as e:
            self.fail(f"Contact us link is not present or visible: {str(e)}")

        # Verify product list
        try:
            products_list = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.js-product')))
            self.assertTrue(len(products_list) > 0)
        except Exception as e:
            self.fail(f"Product list is not present or visible: {str(e)}")

        # Interact with one or two elements
        try:
            # Click "Sign in" link
            login_link.click()
            wait.until(EC.url_contains("login"))
            self.assertIn("login", driver.current_url)
        except Exception as e:
            self.fail(f"Error interacting with page elements: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
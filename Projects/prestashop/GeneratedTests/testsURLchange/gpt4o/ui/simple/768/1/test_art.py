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
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_visibility(self):
        driver = self.driver
        wait = self.wait

        # Verify header is visible
        try:
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
            self.assertTrue(header.is_displayed(), "Header is not visible")
        except Exception as e:
            self.fail(f"Header not found: {str(e)}")

        # Verify search form is visible
        try:
            search_widget = wait.until(EC.visibility_of_element_located((By.ID, "search_widget")))
            self.assertTrue(search_widget.is_displayed(), "Search widget is not visible")
        except Exception as e:
            self.fail(f"Search widget not found: {str(e)}")

        # Verify 'Contact us' link is visible
        try:
            contact_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Contact us")))
            self.assertTrue(contact_link.is_displayed(), "'Contact us' link is not visible")
        except Exception as e:
            self.fail(f"'Contact us' link not found: {str(e)}")

        # Verify 'Sign in' link is visible
        try:
            sign_in_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
            self.assertTrue(sign_in_link.is_displayed(), "'Sign in' link is not visible")
        except Exception as e:
            self.fail(f"'Sign in' link not found: {str(e)}")

        # Verify list of products is visible
        try:
            product_list = wait.until(EC.visibility_of_element_located((By.ID, "js-product-list")))
            self.assertTrue(product_list.is_displayed(), "Product list is not visible")
        except Exception as e:
            self.fail(f"Product list not found: {str(e)}")

        # Verify footer is visible
        try:
            footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
            self.assertTrue(footer.is_displayed(), "Footer is not visible")
        except Exception as e:
            self.fail(f"Footer not found: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
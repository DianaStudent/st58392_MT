import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestArtPageUI(unittest.TestCase):

    def setUp(self):
        # Initialize the Chrome driver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/en/9-art")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Verify header is present
        try:
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
            self.assertTrue(header.is_displayed())
        except:
            self.fail("Header not found or not visible")

        # Verify Art category link is present
        try:
            art_link = wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Art")))
            self.assertTrue(art_link.is_displayed())
        except:
            self.fail("Art link not found or not visible")

        # Verify Sign in link is present
        try:
            sign_in_link = wait.until(
                EC.visibility_of_element_located((By.XPATH, "//a[@title='Log in to your customer account']"))
            )
            self.assertTrue(sign_in_link.is_displayed())
        except:
            self.fail("Sign in link not found or not visible")

        # Verify Search input field is present
        try:
            search_input = wait.until(
                EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Search']"))
            )
            self.assertTrue(search_input.is_displayed())
        except:
            self.fail("Search input field not found or not visible")

        # Verify products are present
        try:
            products = wait.until(
                EC.visibility_of_element_located((By.ID, "js-product-list"))
            )
            self.assertTrue(products.is_displayed())
        except:
            self.fail("Products section not found or not visible")

        # Verify Footer is present
        try:
            footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
            self.assertTrue(footer.is_displayed())
        except:
            self.fail("Footer not found or not visible")

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
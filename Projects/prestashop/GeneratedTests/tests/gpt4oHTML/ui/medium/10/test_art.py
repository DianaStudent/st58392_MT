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
        wait = WebDriverWait(driver, 20)

        # Check presence of main UI components
        try:
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
            footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
            main_content = wait.until(EC.visibility_of_element_located((By.ID, "main")))
            cart_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping-cart")))
            search_form = wait.until(EC.visibility_of_element_located((By.ID, "search_widget")))
            products_list = wait.until(EC.visibility_of_element_located((By.ID, "js-product-list")))
        except Exception as e:
            self.fail(f"Missing main UI components: {str(e)}")

        # Interaction: Click on the 'Contact us' link and check the page transition
        try:
            contact_us_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Contact us")))
            contact_us_link.click()
            wait.until(EC.url_contains("/contact-us"))
        except Exception as e:
            self.fail(f"Interaction with UI components failed: {str(e)}")

        # Verify no errors in the UI
        try:
            page_source = driver.page_source
            self.assertNotIn("error", page_source.lower(), "UI contains errors.")
        except Exception as e:
            self.fail(f"Error verification failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
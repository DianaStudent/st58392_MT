from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestWebsiteUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check logo
        try:
            logo = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "logo-image")))
            self.assertTrue(logo.is_displayed(), "Logo is not visible.")
        except Exception as e:
            self.fail(f"Logo check failed: {str(e)}")

        # Check search input
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-input")))
            self.assertTrue(search_input.is_displayed(), "Search input is not visible.")
        except Exception as e:
            self.fail(f"Search input check failed: {str(e)}")

        # Check cart button
        try:
            cart_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "cart-button")))
            self.assertTrue(cart_button.is_displayed(), "Cart button is not visible.")
        except Exception as e:
            self.fail(f"Cart button check failed: {str(e)}")

        # Check navigation links
        categories = ["Category A", "Category B", "Category C"]
        for category in categories:
            try:
                category_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, category)))
                self.assertTrue(category_link.is_displayed(), f"Category link '{category}' is not visible.")
            except Exception as e:
                self.fail(f"Category link '{category}' check failed: {str(e)}")

        # Check image gallery
        try:
            gallery = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "image-gallery")))
            self.assertTrue(gallery.is_displayed(), "Image gallery is not visible.")
        except Exception as e:
            self.fail(f"Image gallery check failed: {str(e)}")

        # Check best sellers section
        try:
            best_sellers_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
            self.assertEqual(best_sellers_title.text, "BEST SELLERS", "Best sellers title is incorrect or not visible.")
        except Exception as e:
            self.fail(f"Best sellers section check failed: {str(e)}")

        # Check footer
        try:
            footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "section-footer")))
            self.assertTrue(footer.is_displayed(), "Footer is not visible.")
        except Exception as e:
            self.fail(f"Footer check failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
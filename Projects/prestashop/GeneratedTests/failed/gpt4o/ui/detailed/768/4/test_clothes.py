from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestClothesPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/3-clothes")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check header visibility
        header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
        self.assertTrue(header.is_displayed())

        # Check footer visibility
        footer = self.wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        self.assertTrue(footer.is_displayed())

        # Check navigation menu
        nav_menu = self.wait.until(EC.visibility_of_element_located((By.ID, "_desktop_top_menu")))
        self.assertTrue(nav_menu.is_displayed())

        # Check search input field
        search_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "s")))
        self.assertTrue(search_input.is_displayed())

        # Check for buttons
        cart_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping-cart")))
        self.assertTrue(cart_button.is_displayed())

        sign_in_button = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
        self.assertTrue(sign_in_button.is_displayed())

        # Check for subcategories section
        subcategories = self.wait.until(EC.visibility_of_element_located((By.ID, "subcategories")))
        self.assertTrue(subcategories.is_displayed())

        # Check for products
        products = self.wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "product-miniature")))
        self.assertTrue(len(products) > 0)

        # Interaction: Click on the first product's quick view
        quick_view_button = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".js-product-miniature .quick-view")
        ))
        quick_view_button.click()

        # Check if quick view opened, expect some overlay/modal by common practice
        quick_view_modal = self.wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "wishlist-modal")
        ))
        self.assertTrue(quick_view_modal.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
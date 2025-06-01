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
        self.driver.get("http://localhost:3000/category-a-1")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Verify the header logo is present and visible
        try:
            logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.logo-image")))
        except:
            self.fail("Logo is not visible")

        # Confirm the presence of navigation links
        try:
            category_a_link = wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//a[text()='Category A']")
            ))
            subcategory_1_link = wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//a[text()='Subcategory 1']")
            ))
        except:
            self.fail("Navigation links are missing or not visible")

        # Verify the search input is present and visible
        try:
            search_input = wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "input.search-input")
            ))
        except:
            self.fail("Search input is not visible")

        # Confirm the presence of the sorting dropdown
        try:
            sort_dropdown = wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "select")
            ))
        except:
            self.fail("Sort dropdown is not visible")

        # Confirm the presence of the cart icon
        try:
            cart_button = wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "span.cart-button")
            ))
        except:
            self.fail("Cart button is not visible")

        # Interact with elements - Click the search button
        try:
            search_icon = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "img.search-icon-search")
            ))
            search_icon.click()
        except:
            self.fail("Failed to interact with search element")

        # Verify that interactive element (e.g., cart button) does not cause errors
        try:
            cart_button.click()
            cart_content = wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "div.mini-cart")
            ))
            self.assertTrue("Your cart is empty" in cart_content.text)
        except:
            self.fail("Interaction with cart button failed")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
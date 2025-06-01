from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get('http://localhost:3000/category-a-1')

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check for navigation links
        try:
            category_a_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category-a']")))
            category_b_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category-b']")))
            category_c_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category-c']")))
        except:
            self.fail("Navigation links are missing or not visible")

        # Check for the search input and icon
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-input")))
            search_icon = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-icon-search")))
        except:
            self.fail("Search elements are missing or not visible")

        # Check for the cart button
        try:
            cart_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "cart-button")))
        except:
            self.fail("Cart button is missing or not visible")

        # Check for the category title
        try:
            category_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "category-title")))
        except:
            self.fail("Category title is missing or not visible")

        # Interact with a dropdown and verify change in UI
        try:
            sort_dropdown = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "select")))
            sort_dropdown.click()
            price_low_high_option = wait.until(EC.visibility_of_element_located((By.XPATH, "//option[@value='price']")))
            price_low_high_option.click()

            # Verify the selected option
            self.assertEqual(price_low_high_option.text, "Price low to high", "Sort option not changed correctly")
        except:
            self.fail("Dropdown interaction failed or UI did not update")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
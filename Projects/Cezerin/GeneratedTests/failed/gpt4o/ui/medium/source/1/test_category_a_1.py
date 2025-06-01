from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCategoryPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a-1")

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Verify navigation links
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category-a']")))
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category-a-1']")))  # Active
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category-a-2']")))
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category-a-3']")))

            # Verify sort dropdown
            sort_dropdown = wait.until(EC.visibility_of_element_located((By.XPATH, "//select")))
            self.assertIsNotNone(sort_dropdown, "Sort dropdown not found or not visible")

            # Verify search input
            search_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='text'][@class='search-input']")))
            self.assertIsNotNone(search_input, "Search input not found or not visible")

            # Verify cart button
            cart_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='cart-button']/img[@alt='cart']")))
            self.assertIsNotNone(cart_button, "Cart button not found or not visible")

            # Interact with elements: sort products
            sort_dropdown.click()
            sort_option = wait.until(EC.visibility_of_element_located((By.XPATH, "//option[@value='price']")))
            sort_option.click()

            # Verify that interacting with sort does not cause UI errors (simple placeholder check)
            try:
                wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            except:
                self.fail("Interacting with sort dropdown caused UI errors")

        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")


if __name__ == "__main__":
    unittest.main()
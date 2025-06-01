import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("data:text/html;charset=utf-8," + html_data["html"])
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # 1. Verify that the header is visible
        header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        self.assertTrue(header.is_displayed(), "Header is not visible.")

        # Verify that the footer is visible
        footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
        self.assertTrue(footer.is_displayed(), "Footer is not visible.")

        # Verify that the navigation is visible
        navigation = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'primary-nav')))
        self.assertTrue(navigation.is_displayed(), "Primary navigation is not visible.")

        # 2. Verify presence and visibility of input fields, buttons, labels, and sections
        search_input = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-input')))
        self.assertTrue(search_input.is_displayed(), "Search input is not visible.")

        cart_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'cart-button')))
        self.assertTrue(cart_button.is_displayed(), "Cart button is not visible.")

        sort_dropdown = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'select')))
        self.assertTrue(sort_dropdown.is_displayed(), "Sort dropdown is not visible.")

        # 3. Interact with key UI elements
        logo_link = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'logo-image')))
        logo_link.click()

        current_page = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Subcategory 1']")))
        self.assertTrue(current_page.is_displayed(), "Failed to navigate to the expected page.")

        # 4. Confirm UI reaction
        sort_titles = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'sort-title')))
        self.assertGreaterEqual(len(sort_titles), 1, "Sort titles are missing.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    html_data = {
        "html": "<html lang=\"en\"><head>\n..."
    }
    unittest.main()
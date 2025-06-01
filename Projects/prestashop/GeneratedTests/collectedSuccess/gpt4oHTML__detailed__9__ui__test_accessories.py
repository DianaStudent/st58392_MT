import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestAccessoriesPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/6-accessories")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_visibility(self):
        driver = self.driver
        wait = self.wait

        # Check header existence and visibility
        header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        self.assertTrue(header.is_displayed(), "Header is not visible")

        # Check footer existence and visibility
        footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        self.assertTrue(footer.is_displayed(), "Footer is not visible")

        # Check navigation existence and visibility
        nav = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-nav")))
        self.assertTrue(nav.is_displayed(), "Navigation is not visible")

        # Check input fields in the search widget
        search_input = wait.until(EC.visibility_of_element_located((By.NAME, "s")))
        self.assertTrue(search_input.is_displayed(), "Search input field is not visible")

        # Check presence of buttons and their visibility
        cart_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping-cart")))
        self.assertTrue(cart_button.is_displayed(), "Cart button is not visible")

        sign_in_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
        self.assertTrue(sign_in_link.is_displayed(), "Sign-in link is not visible")

        # Check categories list items
        categories_list = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "category-top-menu")))
        categories_items = categories_list.find_elements(By.TAG_NAME, "li")
        self.assertTrue(len(categories_items) > 0, "Categories items are missing")

        # Interact with a navigation link and check reaction
        accessories_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Accessories")))
        accessories_link.click()

        # Validate that clicking has resulted in a page navigation
        current_url = driver.current_url
        self.assertEqual(current_url, "http://localhost:8080/en/6-accessories", "URL does not match expected after click interaction")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
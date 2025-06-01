import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestArtPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/9-art")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Verify navigation links
        try:
            home_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            category_link = driver.find_element(By.LINK_TEXT, "Art")
            self.assertTrue(home_link.is_displayed())
            self.assertTrue(category_link.is_displayed())
        except Exception as e:
            self.fail(f"Navigation links not visible: {e}")

        # Verify presence of main header, search, and cart
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
            cart_info = driver.find_element(By.CLASS_NAME, "shopping-cart")
            search_input = driver.find_element(By.NAME, "s")
            self.assertTrue(header.is_displayed())
            self.assertTrue(cart_info.is_displayed())
            self.assertTrue(search_input.is_displayed())
        except Exception as e:
            self.fail(f"Main components not visible: {e}")

        # Verify product listing presence
        try:
            product_list = self.wait.until(EC.presence_of_element_located((By.ID, "products")))
            self.assertTrue(product_list.is_displayed())
        except Exception as e:
            self.fail(f"Product list not visible: {e}")

    def test_click_button_interaction(self):
        driver = self.driver

        try:
            # Click on "Sort by" dropdown and select "Name, A to Z"
            sort_by_dropdown = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "select-title")))
            sort_by_dropdown.click()

            name_a_to_z = self.wait.until(
                EC.element_to_be_clickable(
                    (By.LINK_TEXT, "Name, A to Z")
                )
            )
            name_a_to_z.click()

            # Verify the UI updates - This is a placeholder check
            # In a real-world situation, we'd check for specific UI changes
            products = driver.find_element(By.CSS_SELECTOR, ".products")
            self.assertTrue(products.is_displayed())
        except Exception as e:
            self.fail(f"Interaction with elements failed: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
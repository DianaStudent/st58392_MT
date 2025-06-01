import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class TestAccessoriesPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/6-accessories")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check presence of key UI elements
        try:
            # Header elements
            home_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@href, '/en/')]")))
            clothes_link = driver.find_element(By.XPATH, "//a[contains(@href, '/en/3-clothes')]")
            accessories_link = driver.find_element(By.XPATH, "//a[contains(@href, '/en/6-accessories')]")
            art_link = driver.find_element(By.XPATH, "//a[contains(@href, '/en/9-art')]")
            login_link = driver.find_element(By.XPATH, "//a[contains(@href, '/en/login')]")

            # Page specific elements
            header = driver.find_element(By.TAG_NAME, 'h1')
            self.assertEqual(header.text, "Accessories")

            search_input = driver.find_element(By.NAME, "s")
            self.assertTrue(search_input.is_displayed())

            wishlist_button = driver.find_element(By.CLASS_NAME, "wishlist-button-add")
            self.assertTrue(wishlist_button.is_displayed())

        except Exception as e:
            self.fail(f"UI element missing or not visible: {e}")

        # Interact with elements
        try:
            search_input.clear()
            search_input.send_keys("Mug" + Keys.RETURN)

            # Check if search result updates
            updated_header = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'There are')]")))
            self.assertIn("products", updated_header.text)  
            
        except Exception as e:
            self.fail(f"Interaction failed: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
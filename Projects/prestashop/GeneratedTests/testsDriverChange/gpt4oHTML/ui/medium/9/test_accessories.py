from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/6-accessories")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check for the key navigation links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="http://localhost:8080/en/"]')))
            clothes_link = driver.find_element(By.CSS_SELECTOR, 'a[href="http://localhost:8080/en/3-clothes"]')
            accessories_link = driver.find_element(By.CSS_SELECTOR, 'a[href="http://localhost:8080/en/6-accessories"]')
            art_link = driver.find_element(By.CSS_SELECTOR, 'a[href="http://localhost:8080/en/9-art"]')
            self.assertTrue(home_link.is_displayed())
            self.assertTrue(clothes_link.is_displayed())
            self.assertTrue(accessories_link.is_displayed())
            self.assertTrue(art_link.is_displayed())
        except:
            self.fail("Navigation links are missing or not visible.")

        # Check for interactive elements (button example)
        try:
            # Verify the search input is present
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="s"]')))
            self.assertTrue(search_input.is_displayed())

            # Interact with a button (e.g., wishlist button)
            wishlist_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'wishlist-button-add')))
            wishlist_button.click()

            # Check if the UI updates visually
            # Assuming there's an update in the wishlist indication or so
            wishlist_toast = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'wishlist-toast')))
            self.assertTrue(wishlist_toast.is_displayed())
        except:
            self.fail("Interactive elements are missing or do not cause UI updates.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestWebsiteUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/6-accessories")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Check header, footer, and navigation
            wait.until(EC.visibility_of_element_located((By.ID, 'header')))
            wait.until(EC.visibility_of_element_located((By.ID, 'footer')))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav.header-nav')))

            # Check presence and visibility of input fields and buttons
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="s"]')))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.btn-unstyle')))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.wishlist-button-add')))
            
            # Check the presence of main sections
            wait.until(EC.visibility_of_element_located((By.ID, 'category')))
            wait.until(EC.visibility_of_element_located((By.ID, 'content-wrapper')))
            wait.until(EC.visibility_of_element_located((By.ID, 'subcategories')))
            wait.until(EC.visibility_of_element_located((By.ID, 'products')))

            # Click a button and verify the UI response
            cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#_desktop_cart .header')))
            cart_button.click()

            # Confirm that a specific UI reaction occurs
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.blockcart')))

        except Exception as e:
            self.fail(f"A required UI element is missing or not visible: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
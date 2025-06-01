from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


class TestWebsiteUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.implicitly_wait(10)

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check main UI components
        try:
            # Check header elements
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'logo')))
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Home']")))
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Tables']")))
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Chairs']")))
            
            # Check Cookie Consent
            cookie_button = wait.until(EC.visibility_of_element_located((By.ID, 'rcc-confirm-button')))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'CookieConsent')))

            # Check footer elements
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'footer-area')))
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Contact']")))
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Login']")))
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Register']")))

            # Interact with Cookie Consent button
            cookie_button.click()

            # Check product interaction
            product_add_to_cart = wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//button[@title='Add to cart']")))
            product_add_to_cart.click()

            # Verify cart update
            cart_count = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'count-style')))
            self.assertNotEqual(cart_count.text, '0', "Cart did not update after adding a product.")
        
        except Exception as e:
            self.fail(f"UI Test failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
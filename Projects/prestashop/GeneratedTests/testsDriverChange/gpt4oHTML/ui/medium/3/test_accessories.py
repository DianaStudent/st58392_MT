import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIComponents(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_navigation_and_ui_elements(self):
        driver = self.driver

        # Verify presence of main navigation links
        home_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Home')))
        clothes_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Clothes')))
        accessories_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Accessories')))
        art_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Art')))

        self.assertTrue(home_link.is_displayed(), "Home link is not visible")
        self.assertTrue(clothes_link.is_displayed(), "Clothes link is not visible")
        self.assertTrue(accessories_link.is_displayed(), "Accessories link is not visible")
        self.assertTrue(art_link.is_displayed(), "Art link is not visible")

        # Verify presence of interactive elements
        search_input = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[aria-label="Search"]')))
        cart_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div#_desktop_cart .header')))
        sign_in_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[title="Log in to your customer account"]')))

        self.assertTrue(search_input.is_displayed(), "Search input is not visible")
        self.assertTrue(cart_button.is_displayed(), "Cart button is not visible")
        self.assertTrue(sign_in_button.is_displayed(), "Sign in button is not visible")

        # Interact with an element
        cart_button.click()

        # Check that clicking the cart button results in visible UI update (cart preview becomes active)
        try:
            cart_preview_active = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "cart-preview.inactive"))
            )
        except:
            self.fail("UI did not update as expected after clicking the cart button.")

        # Verify that interacting with elements doesn't cause errors in the UI
        try:
            # Example: clicking the "Home" link
            home_link.click()
            self.assertEqual(driver.current_url, "http://localhost:8080/en/", "Did not navigate to Home page as expected.")
        except Exception as e:
            self.fail(f"Error occurred during UI interaction: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
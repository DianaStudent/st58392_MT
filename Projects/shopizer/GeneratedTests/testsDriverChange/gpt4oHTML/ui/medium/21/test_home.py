import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class TestUIProcess(unittest.TestCase):

    def setUp(self):
        # Setup Chrome WebDriver using webdriver-manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait
        
        # Confirm presence of key interface elements
        try:
            # Check for logo
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.logo a img")))
            # Check for navigation links
            nav_links = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".main-menu nav ul li a")))
            self.assertTrue(len(nav_links) > 0)

            # Check for presence of "Home", "Tables", "Chairs" links
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))

            # Check for "Accept" cookies button
            cookies_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            self.assertTrue(cookies_button.is_displayed())

            # Check presence of product elements
            product_elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-wrap-2")))
            self.assertTrue(len(product_elements) > 0)

            # Interact with "Accept" cookies button
            cookies_button.click()

            # Verify no errors on executing the event
            ActionChains(driver).move_to_element(nav_links[0]).perform()

        except Exception as e:
            self.fail(f"Test failed due to missing or non-visible element: {str(e)}")

    def tearDown(self):
        # Close the WebDriver
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
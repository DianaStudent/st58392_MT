import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestWebsiteElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/en/")

    def tearDown(self):
        self.driver.quit()

    def test_elements_visibility(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Verify presence of navigation links
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))

            # Verify presence of 'Sign in' button
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))

            # Verify presence of search input
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[aria-label='Search']")))

            # Verify presence of 'Contact us' link
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Contact us")))

            # Verify presence of banner
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img[alt='']")))

            # Verify presence of popular products section
            wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Popular Products')]")))

            # Interact with the search input
            search_input = driver.find_element(By.CSS_SELECTOR, "input[aria-label='Search']")
            search_input.send_keys("Mug")
            
            # Verify interactive behavior by clicking 'Sign in' and ensuring navigation to login occurs
            sign_in_link = driver.find_element(By.LINK_TEXT, "Sign in")
            sign_in_link.click()

            # Wait for login page to load
            wait.until(EC.url_contains("http://localhost:8080/en/login"))

        except Exception as e:
            self.fail(f"Test failed due to missing element or interaction error: {e}")

if __name__ == "__main__":
    unittest.main()
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestClothingPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/3-clothes")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Check presence of navigation links
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            clothes_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
            accessories_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
            art_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))

            # Check the presence of the search input field
            search_input = wait.until(EC.visibility_of_element_located((By.NAME, "s")))

            # Check presence of buttons
            sign_in_button = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
            cart_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart")))

            # Check for the presence of the header title
            header_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.h1")))
            
            # Interact with "Sign in" button
            sign_in_button.click()
            login_input = wait.until(EC.visibility_of_element_located((By.ID, "login-form")))

            # Check that navigating to login page is successful
            self.assertIn("login", driver.current_url)

        except Exception as e:
            self.fail(f"Test failed due to missing element: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
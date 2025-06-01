import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_home_page_ui(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open the page
        driver.get("http://max/")

        # Step 2: Confirm presence of key interface elements
        try:
            # Check the presence of navigation links
            home_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Home page']")))
            self.assertTrue(home_link.is_displayed(), "Home page link is not visible")

            # Check presence of register and login links
            register_link = driver.find_element(By.CLASS_NAME, "ico-register")
            login_link = driver.find_element(By.CLASS_NAME, "ico-login")
            self.assertTrue(register_link.is_displayed(), "Register link is not visible")
            self.assertTrue(login_link.is_displayed(), "Login link is not visible")

            # Check the presence of a search box
            search_input = driver.find_element(By.ID, "small-searchterms")
            self.assertTrue(search_input.is_displayed(), "Search input is not visible")

            # Check presence of button and banners
            search_button = driver.find_element(By.CLASS_NAME, "search-box-button")
            banner_image1 = driver.find_element(By.CSS_SELECTOR, "img[src='http://max/images/thumbs/0000001_banner_1.webp']")
            banner_image2 = driver.find_element(By.CSS_SELECTOR, "img[src='http://max/images/thumbs/0000002_banner_2.webp']")
            self.assertTrue(search_button.is_displayed(), "Search button is not visible")
            self.assertTrue(banner_image1.is_displayed(), "Banner image 1 is not visible")
            self.assertTrue(banner_image2.is_displayed(), "Banner image 2 is not visible")

        except Exception as e:
            self.fail(f"Failed to confirm presence of key UI elements due to: {str(e)}")

        # Step 3: Interact with elements
        try:
            search_input.clear()
            search_input.send_keys("example search")
            search_button.click()

            # Check the UI updates visually i.e., new URL
            wait.until(EC.url_contains("search?q=example+search"))
            self.assertIn("search?q=example+search", driver.current_url, "Search did not navigate to the correct URL")

        except Exception as e:
            self.fail(f"Failed to interact with UI or verify changes due to: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
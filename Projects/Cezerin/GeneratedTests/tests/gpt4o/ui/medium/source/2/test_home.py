import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class HomePageUITests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:3000")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Check logo presence
            logo = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'logo-image')))
            self.assertTrue(logo.is_displayed(), "Logo is not visible")

            # Check category links
            categories = ["Category A", "Category B", "Category C"]
            for category in categories:
                element = wait.until(EC.visibility_of_element_located(
                    (By.LINK_TEXT, category)
                ))
                self.assertTrue(element.is_displayed(), f"{category} link is not visible")

            # Check search input and button
            search_input = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-input')))
            self.assertTrue(search_input.is_displayed(), "Search input is not visible")

            # Check banner presence
            banner = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'home-slider')))
            self.assertTrue(banner.is_displayed(), "Banner is not visible")

            # Interact with Category A link
            category_a_link = driver.find_element(By.LINK_TEXT, "Category A")
            category_a_link.click()

            # Verify navigation to Category A
            wait.until(EC.url_contains("/category-a"))
            self.assertIn("/category-a", driver.current_url, "Failed to navigate to Category A")

        except Exception as e:
            self.fail(str(e))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
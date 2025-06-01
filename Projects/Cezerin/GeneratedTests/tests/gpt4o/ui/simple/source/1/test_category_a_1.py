import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        # Set up the WebDriver
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:3000/category-a-1")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Check header
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
            self.assertTrue(header.is_displayed(), "Header is not visible")

            # Check logo
            logo = driver.find_element(By.CSS_SELECTOR, "a.logo-image")
            self.assertTrue(logo.is_displayed(), "Logo is not visible")

            # Check search box
            search_box = driver.find_element(By.CLASS_NAME, "search-input")
            self.assertTrue(search_box.is_displayed(), "Search input is not visible")

            # Check category links
            for link_text in ["Category A", "Category B", "Category C"]:
                link = driver.find_element(By.LINK_TEXT, link_text)
                self.assertTrue(link.is_displayed(), f"{link_text} link is not visible")

            # Check sort selection
            sort_select = driver.find_element(By.CSS_SELECTOR, "select")
            self.assertTrue(sort_select.is_displayed(), "Sort selection is not visible")

            # Check footer
            footer = driver.find_element(By.TAG_NAME, "footer")
            self.assertTrue(footer.is_displayed(), "Footer is not visible")

            # Check footer links
            for link_text in ["About", "Blog", "Terms of Service", "Privacy Policy"]:
                link = driver.find_element(By.LINK_TEXT, link_text)
                self.assertTrue(link.is_displayed(), f"{link_text} link in footer is not visible")

        except Exception as e:
            self.fail(f"Failed to find a UI element: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
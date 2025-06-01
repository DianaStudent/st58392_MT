import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/3-clothes")

    def test_ui_elements(self):
        driver = self.driver

        try:
            # Verify header is visible
            header = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "header"))
            )

            # Verify footer is visible
            footer = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "footer"))
            )

            # Verify main navigation is visible
            main_nav = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "top-menu"))
            )

            # Verify search input is visible
            search_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "s"))
            )

            # Verify cart icon is visible
            cart_icon = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "shopping-cart"))
            )

            # Verify sign in link is visible
            sign_in_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Sign in"))
            )
            
            # Verify categories are visible
            clothes_category = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Clothes"))
            )
            accessories_category = driver.find_element(By.LINK_TEXT, "Accessories")

            # Verify subcategories are visible
            subcategories_list = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "subcategories-list"))
            )

            # Verify the newsletter subscription button is visible
            subscribe_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "submitNewsletter"))
            )

            # Click on sign in button to ensure UI interaction works
            sign_in_link.click()
            WebDriverWait(driver, 20).until(
                EC.url_contains("login")
            )

        except Exception as e:
            self.fail(f"Test failed due to missing element or interaction failure: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
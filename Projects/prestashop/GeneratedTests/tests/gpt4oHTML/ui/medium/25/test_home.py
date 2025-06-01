import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestDemoWebsite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_ui_elements(self):
        driver = self.driver

        try:
            # Wait and check for presence of key interface elements
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "header"))
            )

            # Check top menu links
            clothes_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Clothes"))
            )
            accessories_link = driver.find_element(By.LINK_TEXT, "Accessories")
            art_link = driver.find_element(By.LINK_TEXT, "Art")

            # Check account links
            login_link = driver.find_element(By.LINK_TEXT, "Sign in")

            # Check input fields
            search_input = driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Search"]')

            # Check buttons
            wishlist_buttons = driver.find_elements(By.CLASS_NAME, "wishlist-button-add")
            if not wishlist_buttons:
                self.fail("Wishlist buttons are not present.")

            # Check banners
            banners = driver.find_elements(By.CLASS_NAME, "carousel-item")
            if not banners:
                self.fail("Carousel banners are not present.")

            # Interactions
            clothes_link.click()
            WebDriverWait(driver, 20).until(EC.url_contains("3-clothes"))

            # Checking if UI updates do not cause errors
            cart_icon = driver.find_element(By.CLASS_NAME, "shopping-cart")
            if not cart_icon.is_displayed():
                self.fail("Cart icon is not displayed after interaction.")

        except Exception as e:
            self.fail(f"The test failed due to the following exception: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
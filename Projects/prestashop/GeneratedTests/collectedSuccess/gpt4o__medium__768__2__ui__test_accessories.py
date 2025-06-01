import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class AccessoriesPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/6-accessories")

    def test_ui_elements_present(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check presence of navigation links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            clothes_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
            accessories_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
            art_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))
        except Exception as e:
            self.fail(f"Navigation link missing: {str(e)}")

        # Check presence of buttons
        try:
            sign_in_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@title='Log in to your customer account']")))
            cart_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='blockcart cart-preview inactive']")))
        except Exception as e:
            self.fail(f"Button missing: {str(e)}")

        # Check presence of search input
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search our catalog']")))
        except Exception as e:
            self.fail(f"Search input missing: {str(e)}")

        # Interact with the search bar and verify no errors in the UI
        search_input.send_keys("mug")
        search_input.submit()

        try:
            results = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'products')]")))
        except Exception as e:
            self.fail(f"Search result area did not display correctly: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
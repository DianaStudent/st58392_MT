import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check main navigation links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Home']")))
            tables_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Tables']")))
            chairs_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Chairs']")))
        except:
            self.fail("Navigation links are missing or not visible.")

        # Check header elements
        try:
            logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".logo img")))
        except:
            self.fail("Logo is missing or not visible.")

        # Check product action buttons
        try:
            add_to_cart_buttons = wait.until(EC.visibility_of_all_elements_located(
                (By.XPATH, "//button[@title='Add to cart']")
            ))
        except:
            self.fail("Add to cart buttons are missing or not visible.")

        # Confirm presence of interactive elements like cookie consent
        try:
            cookie_consent = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            cookie_consent.click()
        except:
            self.fail("Cookie consent button is missing or not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
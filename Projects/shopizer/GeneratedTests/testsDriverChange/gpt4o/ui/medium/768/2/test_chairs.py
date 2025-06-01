import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PageElementsTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver

        # Wait for key elements to be visible
        try:
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".logo a")))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "nav ul li a[href='/']")))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/category/tables']")))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/category/chairs']")))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/login']")))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/register']")))

            # Check the presence of elements
            self.assertTrue(driver.find_element(By.CSS_SELECTOR, ".logo a").is_displayed())
            self.assertTrue(driver.find_element(By.CSS_SELECTOR, "nav ul li a[href='/']").is_displayed())
            self.assertTrue(driver.find_element(By.CSS_SELECTOR, "a[href='/category/tables']").is_displayed())
            self.assertTrue(driver.find_element(By.CSS_SELECTOR, "a[href='/category/chairs']").is_displayed())
            self.assertTrue(driver.find_element(By.CSS_SELECTOR, "a[href='/login']").is_displayed())
            self.assertTrue(driver.find_element(By.CSS_SELECTOR, "a[href='/register']").is_displayed())

            # Test interaction with the button
            accept_cookies_btn = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_btn.click()

            # Verify UI updates visually, e.g., cookie consent disappears
            WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, "CookieConsent")))

        except:
            self.fail("UI components test failed. Some elements might be missing or not visible.")

if __name__ == '__main__':
    unittest.main()
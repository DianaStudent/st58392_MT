import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")

    def test_verify_page_elements(self):
        # Navigation links
        nav_links = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "nav a")))
        self.assertEqual(len(nav_links), 5)

        # Inputs and buttons
        inputs_buttons = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".form-control, .btn")))
        self.assertGreaterEqual(len(inputs_buttons), 3)

        # Banners
        banners = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".banner")))
        self.assertGreaterEqual(len(banners), 1)

    def test_interact_with_elements(self):
        # Click a button and check that the UI updates visually
        button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#login-btn")))
        button.click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".form-control")))

    def test_verify_interactive_elements_do_not_cause_errors(self):
        # Check that interactive elements do not cause errors in the UI
        try:
            self.driver.find_element_by_css_selector("#login-btn").click()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".form-control")))
        except Exception as e:
            self.fail(f"Interactive element caused an error: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
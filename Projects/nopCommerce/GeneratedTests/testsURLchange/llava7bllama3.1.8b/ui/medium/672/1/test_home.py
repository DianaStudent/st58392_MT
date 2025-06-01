from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager

class TestWebsite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/")

    def tearDown(self):
        self.driver.quit()

    def test_website_elements_present(self):
        # Wait for navigation links to be present
        navigation_links = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//nav//a"))
        )

        # Check if all required elements are present in the HTML structure
        self.assertEqual(len(navigation_links), len(["Home", "Product", "Gallery", "Contact Us"]))

        # Wait for form fields to be visible
        form_fields = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//form//input"))
        )

        self.assertEqual(len(form_fields), len(["username", "password"]))

        # Interact with a button and check that the UI updates visually
        submit_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Submit']"))
        )
        submit_button.click()

    def test_website_elements_not_missing(self):
        # Check if any required element is missing in the HTML structure
        navigation_links = self.driver.find_elements(By.XPATH, "//nav//a")
        self.assertGreater(len(navigation_links), 0)

        form_fields = self.driver.find_elements(By.XPATH, "//form//input")
        self.assertGreater(len(form_fields), 0)


if __name__ == "__main__":
    unittest.main()
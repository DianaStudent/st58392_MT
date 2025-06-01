import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestProductPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # Change to your preferred browser
        self.driver.get("http://localhost:8080/en/")  # Replace with your URL

    def test_product_page(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//section[@data-name='products']")))

            sign_out_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Sign out')]")))
            self.assertEqual(sign_out_button.text.strip(), "Sign out")

        except Exception as e:
            self.fail("Required element not found: {}".format(e))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
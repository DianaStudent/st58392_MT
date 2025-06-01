import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestUIProcess(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check navigation links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home page")))
            new_products_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "New products")))
            my_account_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "My account")))
            self.assertTrue(home_link.is_displayed())
            self.assertTrue(new_products_link.is_displayed())
            self.assertTrue(my_account_link.is_displayed())
        except:
            self.fail("Key navigation links are missing.")

        # Check header elements
        try:
            header_logo = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-logo")))
            search_box = wait.until(EC.visibility_of_element_located((By.ID, "small-search-box-form")))
            self.assertTrue(header_logo.is_displayed())
            self.assertTrue(search_box.is_displayed())
        except:
            self.fail("Header elements like logo or search box are missing.")

        # Interact with a button and verify UI update
        try:
            newsletter_button = wait.until(EC.visibility_of_element_located((By.ID, "newsletter-subscribe-button")))
            newsletter_button.click()

            # Verify if the UI updates visually
            newsletter_result_block = wait.until(EC.visibility_of_element_located((By.ID, "newsletter-result-block")))
            self.assertTrue(newsletter_result_block.is_displayed(), "UI did not update after button click")
        except:
            self.fail("Interaction with button did not behave as expected or some elements are missing.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
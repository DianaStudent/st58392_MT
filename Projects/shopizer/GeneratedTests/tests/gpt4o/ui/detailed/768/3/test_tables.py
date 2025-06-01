import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class ShopizerUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header visibility
        header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-area")))
        if not header.is_displayed():
            self.fail("Header is not visible.")

        # Confirm navigation links are present in header
        navigation_links = ["Home", "Tables", "Chairs"]
        for link_text in navigation_links:
            link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
            if not link.is_displayed():
                self.fail(f"Navigation link '{link_text}' is not visible.")

        # Check footer visibility
        footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer-area")))
        if not footer.is_displayed():
            self.fail("Footer is not visible.")

        # Check button presence and click functionality (e.g., Accept Cookies button)
        cookies_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
        cookies_button.click()

        # Assert button action has taken place
        # (If there's supposed to be a visual change due to cookies acceptance, it should be checked here)

        # Check sections and labels
        sections = ["breadcrumb-area", "shop-area"]
        for section_class in sections:
            section = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, section_class)))
            if not section.is_displayed():
                self.fail(f"Section '{section_class}' is not visible.")

        # Check for presence and functionality of 'Add to cart' buttons
        add_to_cart_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Add to cart')]")
        if not add_to_cart_buttons:
            self.fail("Add to cart buttons are not found.")
        for button in add_to_cart_buttons:
            if not button.is_displayed():
                self.fail("An 'Add to cart' button is not visible.")

        # Check form fields and interaction (search or subscribe field if present)
        try:
            email_input = driver.find_element(By.NAME, "email")
            if not email_input.is_displayed():
                self.fail("Email input field is not visible.")
        except Exception as e:
            self.fail("Email input field is missing.")

if __name__ == "__main__":
    unittest.main()
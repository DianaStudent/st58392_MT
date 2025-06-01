from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from unittest import TestCase

class TestHomePage(TestCase):

    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        cls.driver = webdriver.Chrome(options=options)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get("http://example.com")  # replace with the actual URL

    def test_homepage_elements_present_and_visible(self):

        # Ensure structural elements are visible
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//header")))
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//footer")))

        # Check presence and visibility of input fields
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='search']"))))
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='search']"))))

        # Check presence and visibility of buttons
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to Cart']"))))
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Add to Cart']"))))

        # Check presence and visibility of links
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/about']"))))
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/about']"))))

        # Check presence and visibility of sections
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//section[@id='hero']"))))
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//section[@id='hero']"))))

    def test_homepage_interactions_and_visual_feedback(self):
        # Interact with key UI elements
        add_to_cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to Cart']")))
        add_to_cart_button.click()

        # Confirm that the UI reacts visually
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='alert-success']"))))

    def test_homepage_required_elements_present(self):
        required_elements = ["header", "footer", "input[name='search']", "button[text()='Add to Cart']", "a[href='/about']", "section[id='hero']"]
        for element in required_elements:
            try:
                WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, f"//{element}")))
            except TimeoutException as e:
                self.fail(f"Required element '{element}' is missing")

if __name__ == "__main__":
    unittest.main()
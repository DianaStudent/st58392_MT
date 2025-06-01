from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from unittest import TestCase

class TestMaxWebsite(TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.driver.get("http://max/")

    def test_ui_elements(self):
        # Check header presence
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[@class='title']"))
        )

        # Check navigation links presence
        nav_links = self.driver.find_elements(By.XPATH, "//ul[@class='navlinks']/li")
        for link in nav_links:
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, f"//a[text()='{link.text}']"))
            )

        # Check input fields and buttons presence
        self.driver.find_elements(By.XPATH, "//input[@name='email']")
        self.driver.find_elements(By.XPATH, "//button[@class='btn btn-primary']")

        # Click on a button to confirm UI reaction
        button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary']"))
        )
        button.click()

        # Assert that no required element is missing
        self.assertTrue(len(nav_links) > 0)
        self.assertTrue(len(self.driver.find_elements(By.XPATH, "//input[@name='email']")) > 0)

    def tearDown(self):
        self.driver.quit()
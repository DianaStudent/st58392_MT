from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
# Check that the main UI components are present:
for product in products:
    self.assertTrue(product is not None)
    self.assertTrue(len(product.find_elements_by_tag_name('li')) > 0)

if __name__ == '__main__':
    unittest.main()
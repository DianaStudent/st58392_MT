# Check that the main UI components are present:
for product in products:
    self.assertTrue(product is not None)
    self.assertTrue(len(product.find_elements_by_tag_name('li')) > 0)

if __name__ == '__main__':
    unittest.main()
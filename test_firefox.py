from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import pytest

# Headless mode for CI/CD
options = Options()
options.headless = True

# Use geckodriver installed on Jenkins server
service = Service("/usr/local/bin/geckodriver")
driver = webdriver.Firefox(service=service, options=options)

# Test your live web app on port 81
driver.get("http://192.168.77.137:81/")

# Example test: check page title
print("Page title:", driver.title)
assert "Expected Title" in driver.title  # replace with actual expected title

# Add more Selenium assertions as needed
# Example:
# assert "Welcome" in driver.page_source

driver.quit()

from selenium import webdriver
import random
import time

driver = webdriver.Chrome()
driver.get("https://www.example.com")

# Generate a random number of scrolls between 5 and 10
num_scrolls = random.randint(5, 10)

# Loop to scroll the page multiple times
for _ in range(num_scrolls):
    # Generate a random offset between 100 and 500
    random_offset = random.randint(100, 500)
    
    # Smooth scroll down by the random offset
    js_script = f"window.scrollTo({{ top: window.scrollY + {random_offset}, behavior: 'smooth' }});"
    driver.execute_script(js_script)
    
    # Generate a random delay between 1 and 5 seconds
    random_delay = random.uniform(1, 5)
    
    # Wait for the random delay
    time.sleep(random_delay)

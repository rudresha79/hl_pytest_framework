
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import json
import pyautogui

# Initialize WebDriver
driver = webdriver.Edge()

# Open a webpage
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  # 🔹 Change this to your target webpage

# Function to capture element properties
def get_element_properties(element):
    # Get element attributes
    attributes = driver.execute_script("""
        var items = {}; 
        for (var index = 0; index < arguments[0].attributes.length; ++index) {
            items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value;
        }
        return items;
    """, element)

    # Get element CSS properties
    css_properties = driver.execute_script("""
        var styles = window.getComputedStyle(arguments[0]);
        var items = {};
        for (var i = 0; i < styles.length; i++) {
            items[styles[i]] = styles.getPropertyValue(styles[i]);
        }
        return items;
    """, element)

    return {"attributes": attributes, "css_properties": css_properties}
while driver.current_window_handle :
    # Wait for user to hover over an element and click it
    print("🔹 Hover over the element and click to capture its properties...")
    time.sleep(3)  # Give time to hover

    # Detect mouse click location
    x, y = pyautogui.position()
    print(f"Mouse clicked at: ({x}, {y})")

    # Find the element at the clicked position using JavaScript
    element = driver.execute_script("""
        return document.elementFromPoint(arguments[0], arguments[1]);
    """, x, y)

    # If an element is found, get properties
    if element:
        properties = get_element_properties(element)

        # Print properties
        print("🔹 Captured Element Properties:")
        print(json.dumps(properties, indent=4))

        # Save to a JSON file
        with open("../practice/captured_element_properties.json", "w") as file:
            json.dump(properties, file, indent=4)

        print("✅ Element properties saved to 'captured_element_properties.json'")

    else:
        print("❌ No element found at the clicked position.")

# Close WebDriver
driver.quit()

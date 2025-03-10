import json
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Edge()
driver.get("https://sp3test.claritysystemsinc.com/#/login")  # 🔹 Change this to your target webpage
driver.maximize_window()
time.sleep(3)  # Allow page to load

# Function to get XPath of an element
def get_xpath(element):
    return driver.execute_script("""
        function getElementXPath(element) {
            if (element.id !== '') return 'id("' + element.id + '")';
            if (element === document.body) return element.tagName;
            var index = 0;
            var siblings = element.parentNode.childNodes;
            for (var i = 0; i < siblings.length; i++) {
                var sibling = siblings[i];
                if (sibling === element) return getElementXPath(element.parentNode) + '/' + element.tagName + '[' + (index + 1) + ']';
                if (sibling.nodeType === 1 && sibling.tagName === element.tagName) index++;
            }
        }
        return getElementXPath(arguments[0]);
    """, element)

# Function to extract element properties
def extract_element_properties(element):
    if not element.is_displayed():  # 🔹 Ignore hidden elements
        return None

    tag_name = element.tag_name
    inner_text = element.text.strip()

    # Get element attributes
    attributes = driver.execute_script("""
        var items = {}; 
        for (var index = 0; index < arguments[0].attributes.length; ++index) {
            items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value;
        }
        return items;
    """, element)

    # Get CSS properties
    css_properties = driver.execute_script("""
        var styles = window.getComputedStyle(arguments[0]);
        var items = {};
        for (var i = 0; i < styles.length; i++) {
            items[styles[i]] = styles.getPropertyValue(styles[i]);
        }
        return items;
    """, element)

    # Get XPath
    xpath = get_xpath(element)

    return {
        "Tag Name": tag_name,
        "Inner Text": inner_text,
        "Attributes": json.dumps(attributes, indent=2),  # Store attributes as JSON string
        "CSS Properties": json.dumps(css_properties, indent=2),
        "XPath": xpath
    }

time.sleep(20)
# Extract all visible elements
all_elements = driver.find_elements(By.XPATH, "//*")
elements_data = []

for element in all_elements:
    try:
        properties = extract_element_properties(element)
        if properties:
            elements_data.append(properties)
    except:
        pass  # Skip elements that cause errors

# Convert to Pandas DataFrame
df = pd.DataFrame(elements_data)

# Save to Excel
df.to_excel("elements_data.xlsx", index=False)

print(f"✅ Successfully extracted {len(elements_data)} visible elements.")
print("📁 Data saved to 'elements_data.xlsx'.")

# Close WebDriver
driver.quit()

import time
import json
import tkinter as tk
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Initialize WebDriver to attach to an already opened browser
options = Options()
options.add_experimental_option("debuggerAddress", "localhost:9222")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def get_element_properties():
    """Captures the properties of the active element."""
    try:
        active_element = driver.switch_to.active_element
        tag_name = active_element.tag_name
        attributes = driver.execute_script(
            'var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) '
            '{ items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;',
            active_element)
        element_data = {
            "Tag Name": tag_name,
            "Attributes": attributes
        }
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, json.dumps(element_data, indent=4))
    except Exception as e:
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, f"Error: {str(e)}")

# Create GUI Window
root = tk.Tk()
root.title("Web Spy Tool")
root.geometry("400x300")

capture_button = tk.Button(root, text="Capture Element Properties", command=get_element_properties)
capture_button.pack(pady=10)

text_box = tk.Text(root, height=10, width=50)
text_box.pack()

root.mainloop()

driver.quit()

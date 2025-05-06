import time

from selenium import webdriver

driver = webdriver.Edge()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
js = driver.execute_script

while driver.current_window_handle :
    time.sleep(5)
    driver.execute_script("""
        document.addEventListener('contextmenu', function(ev) {
            ev.preventDefault();
        });
    """)
    e = driver.switch_to.active_element

    executor1 = driver.execute_script
    aa3 = executor1("""
        var items = {};
        for (var index = 0; index < arguments[0].attributes.length; ++index) {
            items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value;
        }
        return items;
    """, e)

    if aa3 is not None:
        str1 = str(aa3)
        print(str1)


time.sleep(20)
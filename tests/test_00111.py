import time

import pytest
from selenium import webdriver

@pytest.fixture
def sample_data():
    #return {"name": "Alice", "age": 30}
    driver = webdriver.Edge()
    #return webdriver.Edge()
    yield driver
    driver.quit()

data  =[1,2]
@pytest.mark.parametrize("data",data)
def test_example(sample_data,data):
    # assert sample_data["name"] == "Alice"
    # assert sample_data["age"] == 30
    driver = sample_data
    driver.get("https://google.com")
    print(data)

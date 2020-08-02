"""
Basic level:
1. Fill all fields in forms except "picture" 
2. Click on [Submit] button
3. Validate inputed data in modal window
Site: https://demoqa.com/automation-practice-form


"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def test_form():
    TEST_DATA = {
        'First_Name': 'test123',
        'Last_Name': 'test45',
        'Email': 'test123@gmail.com',
        'Mobile_Number': '0636190886',
        'Current_Address': 'Ukraine, Kyiv',
        'Check': 'Thanks for submitting the form'
    }

    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/automation-practice-form")
    time.sleep(2)

    driver.find_element_by_css_selector("#firstName").send_keys(TEST_DATA['First_Name'])
    driver.find_element_by_css_selector("#lastName").send_keys(TEST_DATA['Last_Name'])
    driver.find_element_by_css_selector("#userEmail").send_keys(TEST_DATA['Email'])
    driver.find_element_by_css_selector('[for="gender-radio-1"]').click()
    driver.find_element_by_css_selector("#userNumber").send_keys(TEST_DATA['Mobile_Number'])
    driver.find_element_by_id("dateOfBirthInput").clear()
    driver.find_element_by_id("dateOfBirthInput").send_keys(Keys.LEFT_CONTROL, "a")
    driver.find_element_by_id("dateOfBirthInput").send_keys("15 nov 2000", Keys.ENTER)
    driver.find_element_by_css_selector('#subjectsInput').send_keys("Ma")
    driver.find_element_by_css_selector('#subjectsInput').send_keys(Keys.TAB)
    driver.find_element_by_css_selector('[for="hobbies-checkbox-1"]').click()
    driver.find_element_by_css_selector("#currentAddress").send_keys(TEST_DATA['Current_Address'])
    driver.find_element_by_css_selector("[id='react-select-3-input']").send_keys("Haryana", Keys.ENTER)
    driver.find_element_by_css_selector("[id='react-select-4-input']").send_keys("Karnal", Keys.ENTER)

    driver.find_element_by_css_selector("#submit").click()
    time.sleep(3)
    assert "Thanks for submitting the form" in driver.page_source
    driver.quit()

test_form()
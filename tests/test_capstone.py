import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_launch_and_verify_title(driver):
    driver.get("http://the-internet.herokuapp.com/")
    assert driver.title == "The Internet"


def test_ab_testing_and_verify_text(driver):
    driver.get("http://the-internet.herokuapp.com/")
    driver.find_element(By.LINK_TEXT, "A/B Testing").click()
    # Wait for the page to load and check the text
    h3_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h3"))
    )
    assert h3_element.text == "A/B Test Variation 1"


def test_dropdown_and_select_option(driver):
    driver.get("http://the-internet.herokuapp.com/")
    driver.find_element(By.LINK_TEXT, "Dropdown").click()
    dropdown = Select(driver.find_element(By.ID, "dropdown"))
    dropdown.select_by_visible_text("Option 1")
    selected_option = dropdown.first_selected_option
    assert selected_option.text == "Option 1"


def test_verify_frames_links(driver):
    driver.get("http://the-internet.herokuapp.com/")
    driver.find_element(By.LINK_TEXT, "Frames").click()
    nested_frames_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Nested Frames"))
    )
    assert nested_frames_link.is_displayed()
    iframe_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "iFrame"))
    )
    assert iframe_link.is_displayed()

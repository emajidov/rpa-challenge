from RPA.Browser.Selenium import Selenium
import logging

from SeleniumLibrary.errors import ElementNotFound


def open_the_website(url):
    browser_lib = Selenium()
    browser_lib.open_available_browser(url)
    return browser_lib


def click_element(driver, element_identifier, stage_name):
    logging.debug(stage_name)
    try:
        driver.click_element(element_identifier)
    except ElementNotFound as e:
        logging.debug(str(e))
        logging.info(f"Could not find element to click while {stage_name}")


def find_element(driver, element_identifier, stage_name):
    logging.debug(stage_name)
    element = None
    try:
        element = driver.find_element(element_identifier)
    except ElementNotFound as e:
        logging.debug(str(e))
        logging.info(f"Could not find elements while {stage_name}")
    finally:
        return element


def find_elements(driver, element_identifier, stage_name):
    logging.debug(stage_name)
    elements = []
    try:
        elements = driver.find_elements(element_identifier)
    except ElementNotFound as e:
        logging.debug(str(e))
        logging.info(f"Could not find elements while {stage_name}")
    finally:
        return elements


def press_keys(driver, element_identifier, key_to_press, stage_name):
    logging.debug(stage_name)
    try:
        driver.press_keys(element_identifier, key_to_press)
    except ElementNotFound as e:
        logging.debug(str(e))
        logging.info(f"Could not press key {key_to_press} for element while {stage_name}")


def input_text(driver, element_identifier, text_to_input, stage_name):
    logging.debug(stage_name)
    try:
        driver.input_text(element_identifier, text_to_input)
    except ElementNotFound as e:
        logging.debug(str(e))
        logging.info(f"Could not input text: {text_to_input} for element to click while {stage_name}")

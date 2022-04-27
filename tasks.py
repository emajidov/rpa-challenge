from SeleniumLibrary.errors import ElementNotFound
from utils import write_to_excel, count_search_term, contains_money_amount, build_start_date
import logging
from actions import open_the_website, click_element, find_element, find_elements, input_text, press_keys

logging.basicConfig(level="INFO")


def search_for(browser_lib, term, category, month):
    browser_lib.maximize_browser_window()
    click_element(browser_lib, "xpath://button[@data-test-id='search-button']", "searching search input")
    input_text(browser_lib, "name:query", term, "entering search term")
    press_keys(browser_lib, "name:query", "ENTER", "pressing enter for search")

    # select latest one
    click_element(browser_lib, "xpath://select[@data-testid='SearchForm-sortBy']", "sorting recent results")
    click_element(browser_lib, "xpath://option[@value='newest']", "clicking newest button in sort by")

    # start selecting date
    click_element(browser_lib, "xpath://button[@type='button' and @data-testid='search-date-dropdown-a']",
                  "clicking date filter")
    click_element(browser_lib, "xpath://button[@type='button' and @aria-label='Specific Dates']", "entering date range")
    start_date = build_start_date(month)
    input_text(browser_lib, "id:startDate", start_date, "entering start date for newses")
    press_keys(browser_lib, "id:startDate", "ENTER", "pressing enter for start date")
    press_keys(browser_lib, "id:endDate", "ENTER", "pressing enter for end date")

    # select category
    click_element(browser_lib, "xpath://button[@data-testid='search-multiselect-button']", "clicking category dropdown")
    category_inputs = find_elements(browser_lib, "xpath://ul//li//button", "finding elements for categories")

    for category_input in category_inputs:
        if category_input.get_property("value").lower().startswith(category.lower()):
            category_input.click()
            break

    click_element(browser_lib, "xpath://button[@data-testid='search-multiselect-button']", "finished category select")

    # click to first element
    results = find_element(browser_lib, "xpath://ol[@data-testid='search-results']", "trying to find results list")
    results.find_elements_by_tag_name('a')[0].click()

    # start reading content of the news
    title = find_element(browser_lib, "xpath://h1[@data-testid='headline']", "reading title").text
    date = find_element(browser_lib, "xpath://div//time", "reading news date").text
    try:
        description = find_element(browser_lib, "id:article-summary", "reading description").text
    except ElementNotFound as e:
        logging.info("Description not found for the given article")
        description = ""
    image_filename = find_element(browser_lib, "tag:figcaption", "reading image caption").text

    result = {
        "title": title,
        "date": date,
        "description": description,
        "image_filename": image_filename
    }
    browser_lib.close_browser()
    return result


# Define a main() function that calls the other functions in order:
def main():
    browser_lib = open_the_website("https://nytimes.com")
    try:
        search_term = "music"
        result = search_for(browser_lib, search_term, "Arts", 2)

        search_term_counts = count_search_term(result['title'], result['description'], search_term)
        money_amount_exist = contains_money_amount(result['title'], result['description'])
        write_to_excel(result['title'], result['date'], result['description'], result['image_filename'],
                       search_term_counts, money_amount_exist)
    except Exception as e:
        logging.debug(str(e))
        logging.info("Unhandled exception happened")
    finally:
        pass
        browser_lib.close_all_browsers()


# Call the main() function, checking that we are running as a stand-alone script:
if __name__ == "__main__":
    main()

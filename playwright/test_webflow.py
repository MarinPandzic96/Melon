from playwright.async_api import Page
from playwright.sync_api import Playwright, expect


def test_webflow(playwright: Playwright, browser_instance):
    browser_instance.goto("https://mostar.api.demo.ch.melon.market/")
    browser_instance.wait_for_load_state("networkidle")

    browser_instance.get_by_role("row", name="00.01.02 Kanzlei A CHF 1'850").locator("span").nth(1).click()
    with browser_instance.context.expect_page() as new_page_info:
        browser_instance.locator("div.button", has_text="Apply").click()

    # Get the new page
    new_page = new_page_info.value

    # Wait for new page to load
    new_page.wait_for_load_state("networkidle")

    new_page.get_by_text('Start').click()
    new_page.locator("#parking-true").click()
    new_page.get_by_text('Save and next').click()

    new_page.locator('#field-household_type').click()
    new_page.get_by_text('couple household with child').click()
    new_page.locator("#pets-false").click()
    new_page.locator("#music_instruments-false").click()
    new_page.locator("#smoking-true").click()

    new_page.locator('#field-relocation_reason').click()
    new_page.get_by_text('Change of life situation').click()

    new_page.locator("#securities_options-deposit").click()

    new_page.locator('#field-source').click()
    new_page.get_by_text('Facebook').click()

    # browser_instance.wait_for_timeout(8000)

    new_page.get_by_text('Save and next').click()
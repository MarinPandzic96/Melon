from playwright.async_api import Page
from playwright.sync_api import Playwright

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

    browser_instance.wait_for_timeout(3000)
from playwright.async_api import Page
from playwright.sync_api import Playwright, expect


def test_webflow(playwright: Playwright, browser_instance):
    browser_instance.goto("https://mostar.api.demo.ch.melon.market/")
    browser_instance.wait_for_load_state("networkidle")

    browser_instance.get_by_role("row", name="00.01.02 Kanzlei A CHF 1'850").locator("span").nth(1).click()
    with browser_instance.context.expect_page() as new_page_info:
        browser_instance.locator("div.button", has_text="Apply").click()

    new_page = new_page_info.value

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

    new_page.get_by_text('Save and next').click()


    new_page.locator('#create-new-adult').click()

    new_page.locator('#field-title').click()
    new_page.get_by_text('Ms.').click()
    new_page.fill('#field-firstname','Hans')
    new_page.fill('#field-name', 'Tester')

    new_page.locator('#field-date_of_birth').click()

    new_page.locator("div.months-options").locator("input[placeholder='Search...']").click()
    new_page.get_by_text(' December ').click()
    new_page.locator("div.years-options").locator("input[placeholder='Search...']").click()
    new_page.get_by_text(' 1996 ').click()
    new_page.click("td:has-text('24')")

    new_page.locator('#field-civil_status').click()
    new_page.get_by_text('married').click()

    new_page.locator('#field-nation').click()
    new_page.locator('#KM').click()

    new_page.locator('#field-permit').click()
    new_page.locator('#B').click()
    #new_page.get_by_text(' (B) Residence permit ').click()

    new_page.locator('#field-tenant_type').click()
    new_page.locator('#main_tenant').click()
    #new_page.get_by_text(' Main tenant ').click()

    new_page.fill('#field-phone','781234567')
    new_page.fill('#field-email', 'melontest@maildrop.cc')
    new_page.fill('#confirm-field-email', 'melontest@maildrop.cc')

    new_page.fill('#field-street_nr', 'Test 10')
    new_page.fill('#field-postcode', '12345')
    new_page.fill('#field-city', 'Glasgow')
    new_page.locator('#field-country').click()
    new_page.locator("#DE").click()

    new_page.locator('#field-living_since').click()
    new_page.locator("div.months-options").locator("input[placeholder='Search...']").click()
    new_page.get_by_text(' December ').click()
    new_page.locator("div.years-options").locator("input[placeholder='Search...']").click()
    new_page.get_by_text(' 2000 ').click()
    new_page.click("td:has-text('24')")

    new_page.locator("#field-employment_quota").click()
    new_page.locator("#unemployed").click()
    new_page.locator("#securities-certificat").click()
    new_page.locator("#field-agreement_references").click()

    new_page.locator("#submit-nested-form").click()

    #browser_instance.wait_for_timeout(10000)


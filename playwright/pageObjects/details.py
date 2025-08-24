from playwright.sync_api import expect


class DetailsPage:
    def __init__(self, page):
        self.page = page

    def checkDetails(self, test_data):
        adult_1 = test_data["adult_1"]
        adult_2 = test_data["adult_2"]
        child = test_data["child"]

        self._checkAdult(adult_1)
        self._checkAdult(adult_2)
        self._checkChild(child)

        #Add more validation for data

    def _checkAdult(self, adult):
        adult_name = adult["firstname"] + " " + adult["lastname"]
        self.page.locator(".adult", has_text=adult_name).click()

        expect(self.page.locator(".sidepanel-main-body")).to_be_visible()

        expect(self.page.locator("#title-value")).to_contain_text(adult['tittle'])
        expect(self.page.locator("#firstname-value")).to_contain_text(adult['firstname'])
        expect(self.page.locator("#name-value")).to_contain_text(adult['lastname'])
        reversed_date = '.'.join(adult["birth_date"].split('-')[::-1])
        expect(self.page.locator("#date_of_birth-value")).to_contain_text(reversed_date)
        expect(self.page.locator("#civil_status-value")).to_contain_text(adult['civil_status'])
        expect(self.page.locator("#nation-value")).to_contain_text(adult['nation'])
        expect(self.page.locator("#permit-value")).to_contain_text(adult["permit_value"])

        full_phone = adult["calling_code"] + adult["cellphone"]
        expect(self.page.locator("#phone-value")).to_contain_text(full_phone)
        expect(self.page.locator("#email-value")).to_contain_text(adult["email"])

        expect(self.page.locator("#street_nr-value")).to_contain_text(adult["address"])
        expect(self.page.locator("#postcode-value")).to_contain_text(adult["postcode"])
        expect(self.page.locator("#city-value")).to_contain_text(adult["city"])
        expect(self.page.locator("#country-value")).to_contain_text(adult["country_value"])
        reversed_date_2 = '.'.join(adult["living_date"].split('-')[::-1])
        expect(self.page.locator("#living_since-value")).to_contain_text(reversed_date_2)

        expect(self.page.locator("#employment_quota-value")).to_contain_text(adult["employment_value"])

        expect(self.page.locator("#securities-value")).to_contain_text(adult["credit_check_value"])

        self.page.locator("#close-sidepanel").click()

    def _checkChild(self, child):
        child_name = child["firstname"] + " " + child["lastname"]
        self.page.locator(".child", has_text=child_name).click()

        expect(self.page.locator(".sidepanel-main-body")).to_be_visible()

        expect(self.page.locator("#firstname-value")).to_contain_text(child['firstname'])
        expect(self.page.locator("#name-value")).to_contain_text(child['lastname'])

        reversed_date = '.'.join(child["birth_date"].split('-')[::-1])
        expect(self.page.locator("#date_of_birth-value")).to_contain_text(reversed_date)

        expect(self.page.locator("#days_present-value")).to_contain_text(child['nights'])

        self.page.locator("#close-sidepanel").click()
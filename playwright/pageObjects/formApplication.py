from playwright.sync_api import expect


class FormApplication:
    def __init__(self, page):
        self.page = page

    def objectStep(self, apartment):
        #add this to data set

        self.page.get_by_text('Start').click()
        self.page.locator("#parking-true").click()
        self.page.get_by_text('Save and next').click()

    def houseHoldStep(self):
        # add this to data set

        self.page.locator('#field-household_type').click()
        self.page.get_by_text('couple household with child').click()
        self.page.locator("#pets-false").click()
        self.page.locator("#music_instruments-false").click()
        self.page.locator("#smoking-true").click()

        self.page.locator('#field-relocation_reason').click()
        self.page.get_by_text('Change of life situation').click()

        self.page.locator("#securities_options-deposit").click()

        self.page.locator('#field-source').click()
        self.page.get_by_text('Facebook').click()

        self.page.get_by_text('Save and next').click()
        expect(self.page.locator(".input-errors")).to_have_count(0)

    def addAdult(self,adult_data):
        self.page.locator('#create-new-adult').click()

        self.page.locator('#field-title').click()
        self.page.get_by_text(adult_data["tittle"]).click()
        self.page.fill('#field-firstname', adult_data["firstname"])
        self.page.fill('#field-name', adult_data["lastname"])

        birth_date = adult_data["birth_date"]
        day = birth_date.split("-")[2]
        month = birth_date.split("-")[1].lstrip("0")
        month_number = int(month) - 1
        year = birth_date.split("-")[0]

        self.page.locator('#field-date_of_birth').click()

        self.page.locator("div.months-options").locator("input[placeholder='Search...']").click()
        self.page.locator(f'[id="{month_number}"]').click()
        self.page.locator("div.years-options").locator("input[placeholder='Search...']").click()
        self.page.locator(f'[id="{year}"]').click()
        self.page.click(f"td:has-text('{day}')")

        self.page.locator('#field-civil_status').click()
        self.page.locator(f'[id="{adult_data["civil_status"]}"]').click()

        self.page.locator('#field-nation').click()
        self.page.locator(f'[id="{adult_data["nationality"]}"]').click()

        self.page.locator('#field-permit').click()
        self.page.locator(f'[id="{adult_data["permit"]}"]').click()

        self.page.locator('#field-tenant_type').click()
        self.page.locator(f'[id="{adult_data["tenant_type"]}"]').click()

        clean_dial_code = adult_data["calling_code"].lstrip('+')

        self.page.locator(".iti__flag-container").first.click()
        self.page.click(f'[data-dial-code="{clean_dial_code}"]')


        self.page.fill('#field-phone', adult_data["cellphone"])
        self.page.fill('#field-email', adult_data["email"])
        self.page.fill('#confirm-field-email', adult_data["email"])

        self.page.fill('#field-street_nr', adult_data['address'])
        self.page.fill('#field-postcode', adult_data['postcode'])
        self.page.fill('#field-city',  adult_data['city'])
        self.page.locator('#field-country').click()
        self.page.locator(f'[id="{adult_data["country"]}"]').click()

        living_date = adult_data["living_date"]
        living_day = living_date.split("-")[2]
        living_month = living_date.split("-")[1]
        living_month_number = int(living_month) - 1
        living_year = living_date.split("-")[0]

        self.page.locator('#field-living_since').click()
        self.page.locator("div.months-options").locator("input[placeholder='Search...']").click()
        self.page.locator(f'[id="{living_month_number}"]').click()
        self.page.locator("div.years-options").locator("input[placeholder='Search...']").click()
        self.page.locator(f'[id="{living_year}"]').click()
        self.page.click(f"td:has-text('{living_day}')")

        self.page.locator("#field-employment_quota").click()
        self.page.locator(f'[id="{adult_data["employment"]}"]').click()
        self.page.locator(f'[id="{adult_data["credit_check"]}"]').click()
        self.page.locator("#field-agreement_references").click()

        self.page.locator("#submit-nested-form").click()
        expect(self.page.locator(".input-errors")).not_to_be_visible()

    def addChild(self,child_data):
        self.page.locator('#create-new-child').click()
        self.page.fill('#field-firstname', child_data['firstname'])
        self.page.fill('#field-name', child_data['lastname'])

        self.page.locator('[id="field-date_of_birth"]').click()
        birth_date = child_data["birth_date"]
        day = birth_date.split("-")[2]
        month = birth_date.split("-")[1].lstrip("0")
        month_number = int(month) - 1
        year = birth_date.split("-")[0]
        self.page.locator("div.months-options").locator("input[placeholder='Search...']").click()
        self.page.locator(f'[id="{month_number}"]').click()
        self.page.locator("div.years-options").locator("input[placeholder='Search...']").click()
        self.page.locator(f'[id="{year}"]').click()
        self.page.click(f"td:has-text('{day}')")

        self.page.fill('#field-days_present', child_data['nights'])

        self.page.locator('#submit-nested-form').click()
        expect(self.page.locator(".input-errors")).not_to_be_visible()

    def finishPeopleStep(self):
        expect(self.page.locator("#create-new-adult")).to_be_visible()
        self.page.locator('[id=application-btn-submit]').click()

    def summaryStep(self):
        #add a check for apartment and people

        self.page.check('#field-agreement_penalty')
        self.page.check('#field-agreement_truth')
        self.page.check('#field-agreement_privacy')

        self.page.locator('#application-btn-submit').click()
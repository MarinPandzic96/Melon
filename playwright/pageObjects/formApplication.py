class FormApplication:
    def __init__(self, page):
        self.page = page

    def objectStep(self):
        self.page.get_by_text('Start').click()
        self.page.locator("#parking-true").click()
        self.page.get_by_text('Save and next').click()

    def houseHoldStep(self):
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

    def addAdult(self,adult_data):
        self.page.locator('#create-new-adult').click()

        self.page.locator('#field-title').click()
        self.page.get_by_text(adult_data["tittle"]).click()
        self.page.fill('#field-firstname', adult_data["firstname"])
        self.page.fill('#field-name', adult_data["lastname"])

        birth_date = adult_data["birth_date"]  # "1990-05-15"
        day = birth_date.split("-")[2]  # "15"
        month = birth_date.split("-")[1].lstrip("0")  # "05"
        month_number = int(month) - 1
        year = birth_date.split("-")[0]  # "1990"

        self.page.locator('#field-date_of_birth').click()

        self.page.locator("div.months-options").locator("input[placeholder='Search...']").click()
        self.page.locator(f'[id="{month_number}"]').click()
        self.page.locator("div.years-options").locator("input[placeholder='Search...']").click()
        self.page.locator(f'[id="{year}"]').click()
        self.page.click(f"td:has-text('{day}')")

        self.page.locator('#field-civil_status').click()
        self.page.locator(f'[id="{adult_data['civil_status']}"]').click()

        self.page.locator('#field-nation').click()
        self.page.locator(f'[id="{adult_data['nationality']}"]').click()

        self.page.locator('#field-permit').click()
        self.page.locator(f'[id="{adult_data['permit']}"]').click()
        # new_page.get_by_text(' (B) Residence permit ').click()

        self.page.locator('#field-tenant_type').click()
        self.page.locator(f'[id="{adult_data['tenant_type']}"]').click()
        #self.page.locator('#main_tenant').click()
        # new_page.get_by_text(' Main tenant ').click()

        self.page.fill('#field-phone', adult_data['cellphone'])
        self.page.fill('#field-email', adult_data['email'])
        self.page.fill('#confirm-field-email', adult_data['email'])

        self.page.fill('#field-street_nr', adult_data['address'])
        self.page.fill('#field-postcode', adult_data['postcode'])
        self.page.fill('#field-city',  adult_data['city'])
        self.page.locator('#field-country').click()
        #self.page.locator("#DE").click()
        self.page.locator(f'[id="{adult_data['country']}"]').click()

        living_date = adult_data["living_date"]
        living_day = living_date.split("-")[2]
        #living_month = living_date.split("-")[1].lstrip("0")
        living_month = living_date.split("-")[1]
        living_month_number = int(living_month) - 1
        living_year = living_date.split("-")[0]

        self.page.locator('#field-living_since').click()
        self.page.locator("div.months-options").locator("input[placeholder='Search...']").click()
        self.page.locator(f'[id="{living_month_number}"]').click()
        self.page.locator("div.years-options").locator("input[placeholder='Search...']").click()
        self.page.locator(f'[id="{living_year}"]').click()
        self.page.click(f"td:has-text('{living_day}')")

        self.page.wait_for_timeout(10000)
        #self.page.locator("div.months-options").locator("input[placeholder='Search...']").click()
        #self.page.get_by_text(' December ').click()
        #self.page.locator("div.years-options").locator("input[placeholder='Search...']").click()
        #self.page.get_by_text(' 2000 ').click()
        #self.page.click("td:has-text('24')")

        self.page.locator("#field-employment_quota").click()
        #self.page.locator("#unemployed").click()
        self.page.locator(f'[id="{adult_data["employment"]}"]').click()
        self.page.locator(f'[id="{adult_data["credit_check"]}"]').click()
        #self.page.locator("#securities-certificat").click()
        self.page.locator("#field-agreement_references").click()

        self.page.locator("#submit-nested-form").click()
        #self.page.wait_for_timeout(20000)

    def addChild(self,child_data):
        self.page.locator('#create-new-child').click()
        self.page.fill('#field-firstname', child_data['firstname'])
        self.page.fill('#field-name', child_data['lastname'])

        #self.page.locator('#field-date_of_birth').click()
        self.page.locator('[id="field-date_of_birth"]').click()
        birth_date = child_data["birth_date"]  # "1990-05-15"
        day = birth_date.split("-")[2]  # "15"
        month = birth_date.split("-")[1].lstrip("0")  # "05"
        month_number = int(month) - 1
        year = birth_date.split("-")[0]  # "1990"

        self.page.locator("div.months-options").locator("input[placeholder='Search...']").click()
        self.page.locator(f'[id="{month_number}"]').click()
        self.page.locator("div.years-options").locator("input[placeholder='Search...']").click()
        self.page.locator(f'[id="{year}"]').click()
        self.page.click(f"td:has-text('{day}')")

        self.page.fill('#field-days_present', child_data['nights'])

        self.page.wait_for_timeout(8000)

        self.page.locator('#submit-nested-form').click()
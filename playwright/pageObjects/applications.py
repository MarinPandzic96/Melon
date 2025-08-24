from playwright.sync_api import expect

from .details import DetailsPage


class ApplicationsPage:
    def __init__(self, page):
        self.page = page

    def checkValidData(self, test_data ):
        #self.page.wait_for_timeout(5000)
        #self.page.wait_for_load_state("load")
        expect(self.page.locator(".main-table")).to_be_visible()
        rows = self.page.locator("table tbody tr").all()
        apartment = test_data['apartment']
        adult_1 = test_data["adult_1"]
        adult_2 = test_data["adult_2"]
        adult_1_name = adult_1["firstname"] + " " + adult_1["lastname"]
        adult_2_name = adult_2["firstname"] + " " + adult_2["lastname"]
        for row in rows:
            expected_apartment = row.locator("td.priorities").text_content()
            expected_adults = row.locator("td.adults").text_content()
            names = expected_adults.strip().split('  ')
            if len(names) == 1:
                first_name = names[0].strip()
                if expected_apartment.strip() == apartment["tittle"]:
                    if first_name == adult_1_name:
                        row.locator(".detail-column-items i").nth(1).click()
                        detailsPage = DetailsPage(self.page)
                        return detailsPage

            elif len(names) == 2:
                first_name = names[0].strip()
                second_name = names[1].strip()
                if expected_apartment.strip() == apartment["tittle"]:
                    if first_name == adult_1_name and second_name == adult_2_name:
                        row.locator(".detail-column-items i").nth(1).click()
                        detailsPage = DetailsPage(self.page)
                        return detailsPage

        self.page.wait_for_timeout(5000)
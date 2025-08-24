from .applications import ApplicationsPage


class HomePage:
    def __init__(self, page):
        self.page = page

    def navigateToApplications(self):
        self.page.locator('span.menu-item-label', has_text=" Applications " ).click()
        applicationsPage = ApplicationsPage(self.page)
        return applicationsPage
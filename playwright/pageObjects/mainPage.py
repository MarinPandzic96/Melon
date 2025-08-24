from .formApplication import FormApplication


class MainPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://mostar.api.demo.ch.melon.market/")

    def selectApartment(self,apartment):
        self.page.get_by_role("row", name=f"{apartment['tittle']}").locator("span").nth(1).click()
        with self.page.context.expect_page() as new_page_info:
            self.page.locator("div.button", has_text="Apply").click()
        formApplicationPage = FormApplication(new_page_info.value)
        return formApplicationPage
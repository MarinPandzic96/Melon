from playwright.sync_api import expect

from .home import HomePage


class LoginPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://mostar.demo.ch.melon.market/login")

    def logIn(self, user):
        self.page.locator("div.inputs-wrapper input").nth(0).fill(user["name"])  # First (index 0)
        self.page.locator("div.inputs-wrapper input").nth(-1).fill(user["password"])

        self.page.locator("div.btn", has_text="Login").click()

        expect(self.page.locator(".input-errors")).not_to_be_visible()

        homePage = HomePage(self.page)
        return homePage
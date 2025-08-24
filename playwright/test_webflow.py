from pageObjects.mainPage import MainPage
from pageObjects.login import LoginPage

def test_submittingData(browser_instance,test_data):
    mainPage = MainPage(browser_instance)
    mainPage.navigate()
    formApplicationPage = mainPage.selectApartment(test_data['apartment'])
    formApplicationPage.objectStep(test_data['apartment'])
    formApplicationPage.houseHoldStep()
    formApplicationPage.addAdult(test_data["adult_1"])
    formApplicationPage.addAdult(test_data["adult_2"])
    formApplicationPage.addChild(test_data["child"])
    formApplicationPage.finishPeopleStep()
    formApplicationPage.summaryStep()

def test_loginAndCheckData(browser_instance, test_data):
    loginPage = LoginPage(browser_instance)
    loginPage.navigate()
    homePage = loginPage.logIn(test_data['user'])
    applicationPage = homePage.navigateToApplications()
    detailsPage = applicationPage.checkValidData(test_data)
    detailsPage.checkDetails(test_data)

